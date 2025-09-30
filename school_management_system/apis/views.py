from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from django.db.models import (
    Count,
    Avg,
    Max,
    Sum,
    Subquery,
    OuterRef,
    Case,
    When,
    Value,
    IntegerField,
    CharField,
    DecimalField,
    Window,
    F,
)

from school_management_system.models import School, Student, Teacher, Course, ExamResult


class SchoolStatsAPIView(RetrieveAPIView):
    queryset = School.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        school = (
            self.get_queryset()
            .filter(id=pk)
            .annotate(
                total_students=Count("students", distinct=True),
                total_teachers=Count("teachers", distinct=True),
                total_courses=Count("teachers__courses", distinct=True),
                avg_marks=Avg("students__results__marks"),
            )
            .values(
                "id",
                "name",
                "city",
                "total_students",
                "total_teachers",
                "total_courses",
                "avg_marks",
            )
            .first()
        )
        return Response(school)


class TeacherCoursesAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        teacher = (
            self.get_queryset()
            .filter(id=pk)
            .values("id", "name", "school__name")
            .first()
        )

        courses = []
        for course in (
            Teacher.objects.get(id=pk).courses.prefetch_related("students").all()
        ):
            courses.append(
                {
                    "course": course.name,
                    "students": list(course.students.values("id", "name")),
                }
            )

        data = {
            "teacher": teacher,
            "courses": courses,
        }
        return Response(data)


class StudentReportAPIView(RetrieveAPIView):
    queryset = Student.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        student = self.get_queryset().get(id=pk)

        results = student.results.values("course__name", "marks", "date")
        avg_marks = student.results.aggregate(avg=Avg("marks"))["avg"] or 0

        data = {
            "student": student.name,
            "school": student.school.name,
            "results": list(results),
            "average_marks": avg_marks,
            "status": "Pass" if avg_marks >= 50 else "Fail",
        }
        return Response(data)


class SchoolReportAPIView(RetrieveAPIView):

    def retrieve(self, request, *args, **kwargs):
        data = {}

        data["schools_with_student_count"] = list(
            School.objects.annotate(total_students=Count("students")).values(
                "name", "total_students"
            )
        )

        data["teacher_avg_marks"] = list(
            Teacher.objects.annotate(avg_marks=Avg("courses__results__marks")).values(
                "name", "avg_marks"
            )
        )

        top_student = (
            Student.objects.annotate(total=Sum("results__marks"))
            .order_by("-total")
            .values("name", "total")
            .first()
        )
        data["top_student"] = top_student

        data["course_max_marks"] = list(
            Course.objects.annotate(max_marks=Max("results__marks")).values(
                "name", "max_marks"
            )
        )

        latest_result = ExamResult.objects.filter(student=OuterRef("pk")).order_by(
            "-date"
        )
        students_with_latest = Student.objects.annotate(
            latest_marks=Subquery(latest_result.values("marks")[:1])
        ).values("name", "latest_marks")
        data["students_latest_result"] = list(students_with_latest)

        data["student_pass_fail"] = list(
            Student.objects.annotate(
                status=Case(
                    When(results__marks__gte=50, then=Value("Pass")),
                    default=Value("Fail"),
                    output_field=CharField(),
                )
            ).values("name", "status")
        )

        data["student_running_total"] = list(
            ExamResult.objects.annotate(
                running_total=Window(
                    expression=Sum("marks"),
                    partition_by=[F("student")],
                    order_by=F("date").asc(),
                )
            ).values("student__name", "marks", "running_total", "date")
        )

        return Response(data)

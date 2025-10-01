from rest_framework.generics import RetrieveAPIView
from rest_framework.response import Response
from django.db.models import (
    Count,
    Avg,
)

from school.models import School, Student, Teacher, Course, ExamResult
from school.utils import generate_school_report

class SchoolStatsRetrieveAPIView(RetrieveAPIView):
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
        )

        return Response(school)


class TeacherCourseRetrieveAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        teacher = self.get_queryset().filter(id=pk).values("id", "name", "school__name")
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


class StudentReportRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        student = self.get_queryset().get(id=pk)
        results = student.results.values(
            "course__name",
            "marks",
            "date",
        )
        avg_marks = student.results.aggregate(avg=Avg("marks"))["avg"] or 0

        data = {
            "student": student.name,
            "school": student.school.name,
            "results": list(results),
            "average_marks": avg_marks,
            "status": "Pass" if avg_marks >= 50 else "Fail",
        }

        return Response(data)


class SchoolReportRetrieveAPIView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        data = generate_school_report()

        return Response(data)

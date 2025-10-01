from django.db.models import (
    Count,
    Avg,
    Sum,
    Max,
    Case,
    When,
    Value,
    CharField,
    OuterRef,
    Subquery,
    F,
    Window,
)

from school.models import School, Teacher, Student, Course, ExamResult


def generate_school_report():
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

    latest_result = ExamResult.objects.filter(student=OuterRef("pk")).order_by("-date")
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

    return data

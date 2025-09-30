from django.urls import path
from school_management_system.apis.views import (
    SchoolStatsAPIView,
    TeacherCoursesAPIView,
    StudentReportAPIView,
    SchoolReportAPIView,
)

urlpatterns = [
    path(
        "schools/<int:pk>/stats/", SchoolStatsAPIView.as_view(), name="school-stats-api"
    ),
    path(
        "teachers/<int:pk>/courses/",
        TeacherCoursesAPIView.as_view(),
        name="teacher-courses-api",
    ),
    path(
        "students/<int:pk>/report/",
        StudentReportAPIView.as_view(),
        name="student-report-api",
    ),
    path("stats/", SchoolReportAPIView.as_view(), name="school-report-api"),
]

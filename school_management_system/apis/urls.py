from django.urls import path

from school_management_system.apis.views import (
    SchoolStatsRetrieveAPIView,
    TeacherCourseRetrieveAPIView,
    StudentReportRetrieveAPIView,
    SchoolReportRetrieveAPIView,
)


urlpatterns = [
    path(
        "school/<int:pk>/stats/",
        SchoolStatsRetrieveAPIView.as_view(),
        name="school-stats-api"
    ),
    path(
        "teacher/<int:pk>/courses/",
        TeacherCourseRetrieveAPIView.as_view(),
        name="teacher-courses-api",
    ),
    path(
        "student/<int:pk>/report/",
        StudentReportRetrieveAPIView.as_view(),
        name="student-report-api",
    ),
    path(
        "stats/",
        SchoolReportRetrieveAPIView.as_view(),
        name="school-report-api"
    ),
]

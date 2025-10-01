from django.urls import path

from school.apis.views import (
    SchoolStatsRetrieveAPIView,
    TeacherCourseRetrieveAPIView,
    StudentReportRetrieveAPIView,
    SchoolReportRetrieveAPIView,
)


urlpatterns = [
    path(
        "school/<int:pk>/stats/",
        SchoolStatsRetrieveAPIView.as_view(),
        name="school-stats-retrieve-api"
    ),
    path(
        "teacher/<int:pk>/courses/",
        TeacherCourseRetrieveAPIView.as_view(),
        name="teacher-courses-retrieve-api",
    ),
    path(
        "student/<int:pk>/report/",
        StudentReportRetrieveAPIView.as_view(),
        name="student-report-retrieve-api",
    ),
    path(
        "stats/",
        SchoolReportRetrieveAPIView.as_view(),
        name="school-report-retrieve-api"
    ),
]

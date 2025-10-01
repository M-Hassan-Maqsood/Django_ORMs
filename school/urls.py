from django.urls import path

from school.views import (
    SchoolListCreateAPIView,
    SchoolRetrieveUpdateDestroyAPIView,
    TeacherListCreateAPIView,
    TeacherRetrieveUpdateDestroyAPIView,
    StudentListCreateAPIView,
    StudentRetrieveUpdateDestroyAPIView,
    CourseListCreateAPIView,
    CourseRetrieveUpdateDestroyAPIView,
    ExamResultListCreateAPIView,
    ExamResultRetrieveUpdateDestroyAPIView,
    SchoolStatsRetrieveAPIView,
    TeacherCourseRetrieveAPIView,
    StudentReportRetrieveAPIView,
    SchoolReportRetrieveAPIView,
)


urlpatterns = [
    path("schools/", SchoolListCreateAPIView.as_view(), name="school-list-create-api"),
    path(
        "schools/<int:pk>/",
        SchoolRetrieveUpdateDestroyAPIView.as_view(),
        name="school-detail-api",
    ),
    path("teachers/", TeacherListCreateAPIView.as_view(), name="teacher-list-create-api"),
    path(
        "teachers/<int:pk>/",
        TeacherRetrieveUpdateDestroyAPIView.as_view(),
        name="teacher-detail-api",
    ),
    path("students/", StudentListCreateAPIView.as_view(), name="student-list-create-api"),
    path(
        "students/<int:pk>/",
        StudentRetrieveUpdateDestroyAPIView.as_view(),
        name="student-detail-api",
    ),
    path("courses/", CourseListCreateAPIView.as_view(), name="course-list-create-api"),
    path(
        "courses/<int:pk>/",
        CourseRetrieveUpdateDestroyAPIView.as_view(),
        name="course-detail-api",
    ),
    path("results/", ExamResultListCreateAPIView.as_view(), name="result-list-create-api"),
    path(
        "results/<int:pk>/",
        ExamResultRetrieveUpdateDestroyAPIView.as_view(),
        name="result-detail-api",
    ),
    path(
        "school/<int:pk>/stats/",
        SchoolStatsRetrieveAPIView.as_view(),
        name="school-stats-retrieve-api",
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
        name="school-report-retrieve-api",
    ),
]

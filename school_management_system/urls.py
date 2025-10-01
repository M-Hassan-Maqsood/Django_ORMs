from django.urls import path

from school_management_system.views import (
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
)


urlpatterns = [
    # Schools
    path("schools/", SchoolListCreateAPIView.as_view(), name="school-list-create"),
    path(
        "schools/<int:pk>/",
        SchoolRetrieveUpdateDestroyAPIView.as_view(),
        name="school-detail",
    ),
    # Teachers
    path("teachers/", TeacherListCreateAPIView.as_view(), name="teacher-list-create"),
    path(
        "teachers/<int:pk>/",
        TeacherRetrieveUpdateDestroyAPIView.as_view(),
        name="teacher-detail",
    ),
    # Students
    path("students/", StudentListCreateAPIView.as_view(), name="student-list-create"),
    path(
        "students/<int:pk>/",
        StudentRetrieveUpdateDestroyAPIView.as_view(),
        name="student-detail",
    ),
    # Courses
    path("courses/", CourseListCreateAPIView.as_view(), name="course-list-create"),
    path(
        "courses/<int:pk>/",
        CourseRetrieveUpdateDestroyAPIView.as_view(),
        name="course-detail",
    ),
    # Exam Results
    path("results/", ExamResultListCreateAPIView.as_view(), name="result-list-create"),
    path(
        "results/<int:pk>/",
        ExamResultRetrieveUpdateDestroyAPIView.as_view(),
        name="result-detail",
    ),
]

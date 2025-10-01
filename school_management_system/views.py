from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView

from school_management_system.models import School, Teacher, Student, Course, ExamResult
from school_management_system.serializers import (
    SchoolSerializer,
    TeacherSerializer,
    StudentSerializer,
    CourseSerializer,
    ExamResultSerializer,
)


class SchoolListCreateAPIView(ListCreateAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class SchoolRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = School.objects.all()
    serializer_class = SchoolSerializer


class TeacherListCreateAPIView(ListCreateAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class TeacherRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Teacher.objects.all()
    serializer_class = TeacherSerializer


class StudentListCreateAPIView(ListCreateAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class StudentRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Student.objects.all()
    serializer_class = StudentSerializer


class CourseListCreateAPIView(ListCreateAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class CourseRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Course.objects.all()
    serializer_class = CourseSerializer


class ExamResultListCreateAPIView(ListCreateAPIView):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer


class ExamResultRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = ExamResult.objects.all()
    serializer_class = ExamResultSerializer

from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView, RetrieveAPIView
from rest_framework.response import Response

from school.utils import generate_school_report, get_student_report, get_school_stats, get_teacher_courses
from school.models import School, Teacher, Student, Course, ExamResult
from school.serializers import (
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


class SchoolStatsRetrieveAPIView(RetrieveAPIView):
    queryset = School.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        data = get_school_stats(pk)

        return Response(data)


class TeacherCourseRetrieveAPIView(RetrieveAPIView):
    queryset = Teacher.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        data = get_teacher_courses(pk)

        return Response(data)


class StudentReportRetrieveAPIView(RetrieveAPIView):
    queryset = Student.objects.all()

    def retrieve(self, request, *args, **kwargs):
        pk = kwargs.get("pk")
        data = get_student_report(pk)

        return Response(data)


class SchoolReportRetrieveAPIView(RetrieveAPIView):
    def retrieve(self, request, *args, **kwargs):
        data = generate_school_report()

        return Response(data)

from rest_framework import serializers

from school_management_system.models import School, Teacher, Student, Course, ExamResult


class SchoolSerializer(serializers.ModelSerializer):
    class Meta:
        model = School
        fields = "__all__"


class TeacherSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField()

    class Meta:
        model = Teacher
        fields = "__all__"


class StudentSerializer(serializers.ModelSerializer):
    school = serializers.StringRelatedField()

    class Meta:
        model = Student
        fields = "__all__"


class CourseSerializer(serializers.ModelSerializer):
    teacher = serializers.StringRelatedField()
    students = serializers.StringRelatedField(many=True)

    class Meta:
        model = Course
        fields = "__all__"


class ExamResultSerializer(serializers.ModelSerializer):
    student = serializers.StringRelatedField()
    course = serializers.StringRelatedField()

    class Meta:
        model = ExamResult
        fields = "__all__"

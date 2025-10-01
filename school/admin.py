from django.contrib import admin

from school.models import School, Teacher, Student, Course, ExamResult


@admin.register(School)
class SchoolAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "city")
    search_fields = ("name", "city")


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "school")
    search_fields = ("name",)
    list_filter = ("school",)


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "school")
    search_fields = ("name",)
    list_filter = ("school",)


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ("id", "name", "teacher")
    search_fields = ("name",)
    list_filter = ("teacher", "students")


@admin.register(ExamResult)
class ExamResultAdmin(admin.ModelAdmin):
    list_display = ("id", "student", "course", "marks", "date")
    search_fields = ("student__name", "course__name")
    list_filter = ("course", "date")

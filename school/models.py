from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    class Meta:
        db_table = "school"
        verbose_name = "School"
        verbose_name_plural = "Schools"

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)

    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="teachers"
    )

    class Meta:
        db_table = "teacher"
        verbose_name = "Teacher"
        verbose_name_plural = "Teachers"

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)

    school = models.ForeignKey(
        "school.School", on_delete=models.CASCADE, related_name="students"
    )

    class Meta:
        db_table = "student"
        verbose_name = "Student"
        verbose_name_plural = "Students"

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)

    teacher = models.ForeignKey(
        "school.Teacher", on_delete=models.CASCADE, related_name="courses"
    )
    students = models.ManyToManyField("school.Student", related_name="courses")

    class Meta:
        db_table = "course"
        verbose_name = "Course"
        verbose_name_plural = "Courses"

    def __str__(self):
        return f"{self.name} ({self.teacher.name})"


class ExamResult(models.Model):
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    student = models.ForeignKey(
        "school.Student", on_delete=models.CASCADE, related_name="results"
    )
    course = models.ForeignKey("school.Course", on_delete=models.CASCADE, related_name="results")

    class Meta:
        db_table = "exam_result"
        verbose_name = "Exam Result"
        verbose_name_plural = "Exam Results"

    def __str__(self):
        return f"{self.student.name} - {self.course.name}: {self.marks}"

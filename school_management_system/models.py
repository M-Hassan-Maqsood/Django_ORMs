from django.db import models


class School(models.Model):
    name = models.CharField(max_length=100)
    city = models.CharField(max_length=100)

    def __str__(self):
        return self.name


class Teacher(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="teachers"
    )

    def __str__(self):
        return self.name


class Student(models.Model):
    name = models.CharField(max_length=100)
    school = models.ForeignKey(
        School, on_delete=models.CASCADE, related_name="students"
    )

    def __str__(self):
        return self.name


class Course(models.Model):
    name = models.CharField(max_length=100)
    teacher = models.ForeignKey(
        Teacher, on_delete=models.CASCADE, related_name="courses"
    )
    students = models.ManyToManyField(Student, related_name="courses")

    def __str__(self):
        return f"{self.name} ({self.teacher.name})"


class ExamResult(models.Model):
    student = models.ForeignKey(
        Student, on_delete=models.CASCADE, related_name="results"
    )
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name="results")
    marks = models.DecimalField(max_digits=5, decimal_places=2)
    date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.course.name}: {self.marks}"

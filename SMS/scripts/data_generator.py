import random
import datetime

from school_management_system.models import School, Teacher, Student, Course, ExamResult


def generate_school_data():
    print("Deleting old data...")
    ExamResult.objects.all().delete()
    Course.objects.all().delete()
    Student.objects.all().delete()
    Teacher.objects.all().delete()
    School.objects.all().delete()

    print("Creating schools...")
    # Create Schools
    schools = []
    for i in range(3):
        school = School.objects.create(
            name=f"School_{i+1}",
            city=random.choice(
                ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]
            ),
        )
        schools.append(school)

    print("Creating teachers...")
    teachers = []
    for i in range(6):
        teacher = Teacher.objects.create(
            name=f"Teacher_{i+1}",
            school=random.choice(schools),
        )
        teachers.append(teacher)

    print("Creating students...")
    students = []
    for i in range(20):
        student = Student.objects.create(
            name=f"Student_{i+1}",
            school=random.choice(schools),
        )
        students.append(student)

    print("Creating courses...")
    courses = []
    course_names = [
        "Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "English",
    ]
    for i, name in enumerate(course_names):
        teacher = random.choice(teachers)
        course = Course.objects.create(
            name=name,
            teacher=teacher,
        )
        # Random students enroll
        selected_students = random.sample(students, random.randint(5, 12))
        course.students.add(*selected_students)
        courses.append(course)

    print("Creating exam results...")
    for student in students:
        for course in random.sample(
            courses, random.randint(2, 4)
        ):  # each student enrolls in 2–4 courses
            ExamResult.objects.create(
                student=student,
                course=course,
                marks=random.randint(40, 100),
                date=datetime.date(2024, random.randint(1, 12), random.randint(1, 28)),
            )

    print("All school data created successfully!")

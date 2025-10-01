import random
import datetime

from school_management_system.models import School, Teacher, Student, Course, ExamResult


def generate_school_data():
    print("Deleting old data...")
    School.objects.all().delete()
    Course.objects.all().delete()
    Student.objects.all().delete()
    Teacher.objects.all().delete()
    ExamResult.objects.all().delete()

    print("Creating schools...")
    schools=create_school_data()
    print("Creating teachers...")
    teachers=create_teacher_data(schools)
    print("Creating students...")
    students=create_student_data(schools)
    print("Creating courses...")
    courses=create_course_data(teachers, students)
    print("Creating exam results...")
    create_exam_result_data(students, courses)
    print("All school data created successfully!")

def create_school_data():
    schools = []
    for i in range(3):
        school = School.objects.create(
            name=f"School_{i+1}",
            city=random.choice(
                ["Karachi", "Lahore", "Islamabad", "Peshawar", "Quetta"]
            ),
        )
        schools.append(school)

    return schools

def create_teacher_data(schools):
    teachers = []
    for i in range(6):
        teacher = Teacher.objects.create(
            name=f"Teacher_{i+1}",
            school=random.choice(schools),
        )
        teachers.append(teacher)

    return teachers

def create_student_data(schools):
    students = []
    for i in range(20):
        student = Student.objects.create(
            name=f"Student_{i+1}",
            school=random.choice(schools),
        )
        students.append(student)

    return students

def create_course_data(teachers, students):
    courses = []
    course_names = [
        "Mathematics",
        "Physics",
        "Chemistry",
        "Biology",
        "Computer Science",
        "English",
        "PST",
    ]
    for i, name in enumerate(course_names):
        teacher = random.choice(teachers)
        course = Course.objects.create(
            name=name,
            teacher=teacher,
        )
        selected_students = random.sample(students, random.randint(5, 12))
        course.students.add(*selected_students)
        courses.append(course)

    return courses

def create_exam_result_data(students, courses):
    for student in students:
        for course in random.sample(
            courses, random.randint(2, 4)
        ):
            ExamResult.objects.create(
                student=student,
                course=course,
                marks=random.randint(40, 100),
                date=datetime.date(2024, random.randint(1, 12), random.randint(1, 28)),
            )

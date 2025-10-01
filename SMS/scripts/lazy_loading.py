from django.db import connection

from school.models import School, ExamResult, Student


def demonstrate_lazy_evaluation():
    connection.queries_log.clear()
    # Create queryset
    qs = School.objects.all()
    print("\n Step 2: Created queryset")
    print("Queries executed:", len(connection.queries_log))
    print("Prepared SQL (not executed yet):", qs.query)

    list(qs)
    print("\n Step 3: After evaluation")
    print("Queries executed:", len(connection.queries_log))
    print("Executed SQL:", connection.queries_log[-1]["sql"])

    qs_chain = ExamResult.objects.filter(marks__gte=50)
    print("\n Step 4: Chained queryset created")
    print("Queries executed:", len(connection.queries_log))
    print("Prepared SQL:", qs_chain.query)

    list(qs_chain)
    print("\n Step 5: After chained queryset evaluation ")
    print("Queries executed:", len(connection.queries_log))
    print("Executed SQL:", connection.queries_log[-1]["sql"])

    qs_student = Student.objects.filter(name__startswith="Student_7")
    print("\n Step 6: Student queryset created")
    print("Queries executed:", len(connection.queries_log))
    print("Prepared SQL:", qs_student.query)

    count_students = qs_student.count()
    print("\n Step 7: After count()")
    print("Queries executed:", len(connection.queries_log))
    print("Executed SQL:", connection.queries_log[-1]["sql"])
    print("Student count:", count_students)

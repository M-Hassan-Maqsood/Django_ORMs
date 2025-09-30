from django.db import connection
from school_management_system.models import School, ExamResult, Student


def demonstrate_lazy_evaluation():
    connection.queries_log.clear()

    # Step 2: Create queryset (no SQL executed yet)
    qs = School.objects.all()
    print("\n Step 2: Created queryset")
    print("Queries executed:", len(connection.queries_log))
    print("Prepared SQL (not executed yet):", qs.query)

    # Step 3: Force evaluation with list()
    list(qs)
    print("\n Step 3: After evaluation")
    print("Queries executed:", len(connection.queries_log))
    print("Executed SQL:", connection.queries_log[-1]["sql"])

    # Step 4: Chaining filters on ExamResult
    qs_chain = ExamResult.objects.filter(marks__gte=50)  # students with >=50 marks
    print("\n Step 4: Chained queryset created")
    print("Queries executed:", len(connection.queries_log))  # Still 1
    print("Prepared SQL:", qs_chain.query)

    # Step 5: Force evaluation
    list(qs_chain)
    print("\n Step 5: After chained queryset evaluation ")
    print("Queries executed:", len(connection.queries_log))  # 2 now
    print("Executed SQL:", connection.queries_log[-1]["sql"])

    # Step 6: Another example with Student
    qs_student = Student.objects.filter(name__startswith="Student_7")
    print("\n Step 6: Student queryset created")
    print("Queries executed:", len(connection.queries_log))  # Still 2
    print("Prepared SQL:", qs_student.query)

    # Step 7: Force evaluation with count()
    count_students = qs_student.count()
    print("\n Step 7: After count()")
    print("Queries executed:", len(connection.queries_log))  # 3 now
    print("Executed SQL:", connection.queries_log[-1]["sql"])
    print("Student count:", count_students)

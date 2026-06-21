from database import create_tables
from learning import LMS

create_tables()
system = LMS()

while True:
    print("""
1. Add User
2. View Users
3. Create Course
4. View Courses
5. Enroll Student
6. Update Progress
7. Make Payment
8. Exit

""")

    choice=input("Choose: ")
    if choice=="1":
        name=input("Name: ")
        role=input("Role(Student/Teacher/Admin): ")
        system.add_user(name,role)
    elif choice=="2":
        system.view_users()
    elif choice=="3":
        name=input("Course name: ")
        price=float(input("Price: "))
        teacher=int(input("Teacher ID: "))
        system.create_course(name,price,teacher )
    elif choice=="4":
        system.view_courses()
    elif choice=="5":
        student=int(input("Student ID: "))
        course=int(input("Course ID: "))
        system.enroll(student,course)

    elif choice=="6":
        student=int(input("Student ID: "))
        course=int(input("Course ID: "))
        progress=int(input("Progress %: "))
        system.update_progress(student,course,progress)


    elif choice=="7":
        student=int(input("Student ID: "))
        course=int(input("Course ID: "))
        amount=float(input("Amount: "))
        system.make_payment(student,course,amount)
    elif choice=="8":

        break
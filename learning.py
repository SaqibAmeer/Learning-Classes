from database import connect
class LMS:
    def add_user(self,name,role):
        db = connect()
        cursor = db.cursor()
        cursor.execute("INSERT INTO users(name,role) VALUES(?,?)",(name,role) )
        db.commit()
        db.close()
        print("User created")


    def view_users(self):
        db = connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM users" )
        users = cursor.fetchall()

        for user in users:
            print(user)
        db.close()




    def create_course(self,name,price,teacher_id):
        db = connect()
        cursor = db.cursor()
        cursor.execute(
        """
        INSERT INTO courses
        (name,price,teacher_id)

        VALUES(?,?,?)

        """,
        (name,price,teacher_id))

        db.commit()
        db.close()
        print("Course created")


    def view_courses(self):
        db = connect()
        cursor = db.cursor()
        cursor.execute("SELECT * FROM courses" )
        courses = cursor.fetchall()

        for course in courses:
            print(course)

        db.close()




    def enroll(self,student_id,course_id):
        db = connect()
        cursor = db.cursor()
        cursor.execute(
        """
        INSERT INTO enrollments

        (student_id,course_id,progress)

        VALUES(?,?,?)

        """,
        (student_id,course_id,0)
        )

        db.commit()
        db.close()
        print("Student enrolled")








    def update_progress(self,student_id,course_id,progress):
        db = connect()
        cursor = db.cursor()
        cursor.execute(
        """
        UPDATE enrollments

        SET progress=?

        WHERE student_id=? AND course_id=?

        """,
        (progress,student_id,course_id))
        db.commit()
        db.close()
        print("Progress updated")







    def make_payment(self,student,course,amount):
        db = connect()
        cursor = db.cursor()
        cursor.execute(
        """
        INSERT INTO payments

        (student_id,course_id,amount,status)

        VALUES(?,?,?,?)

        """,
        (student,course,amount,"Paid") )
        db.commit()
        db.close()
        print("Payment completed")
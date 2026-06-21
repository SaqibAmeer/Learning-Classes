import sqlite3

def connect():
    return sqlite3.connect("lms.db")




def create_tables():
    db = connect()
    cursor = db.cursor()
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users(

        id INTEGER PRIMARY KEY AUTOINCREMENT,

        name TEXT,

        role TEXT

    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS courses(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT,
        price REAL,
        teacher_id INTEGER
    )
    """)


    cursor.execute("""
    CREATE TABLE IF NOT EXISTS enrollments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,

        course_id INTEGER,
        progress INTEGER

    )
    """)



    cursor.execute("""
    CREATE TABLE IF NOT EXISTS payments(
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        student_id INTEGER,
        course_id INTEGER,
        amount REAL,

        status TEXT

    )
    """)



    db.commit()
    db.close()
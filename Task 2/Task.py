import mysql.connector

def create_database(cursor):
    cursor.execute("CREATE DATABASE IF NOT EXISTS school")

def create_table(cursor):
    cursor.execute("USE school")
    cursor.execute("""
        CREATE TABLE IF NOT EXISTS students (
            student_id INT AUTO_INCREMENT PRIMARY KEY,
            first_name VARCHAR(255),
            last_name VARCHAR(255),
            age INT,
            grade FLOAT
        )
    """)

def insert_student(cursor, first_name, last_name, age, grade):
    cursor.execute("""
        INSERT INTO students (first_name, last_name, age, grade)
        VALUES (%s, %s, %s, %s)
    """, (first_name, last_name, age, grade))

def update_student_grade(cursor, first_name, new_grade):
    cursor.execute("""
        UPDATE students
        SET grade = %s
        WHERE first_name = %s
    """, (new_grade, first_name))

def delete_student(cursor, last_name):
    cursor.execute("""
        DELETE FROM students
        WHERE last_name = %s
    """, (last_name,))

def fetch_all_students(cursor):
    cursor.execute("SELECT * FROM students")
    return cursor.fetchall()

def main():
    # Connect to MySQL database
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="7488552785aA@"
    )
    cursor = conn.cursor()

    create_database(cursor)
    create_table(cursor)

    # Insert record
    insert_student(cursor, "Alice", "Smith", 18, 95.5)
    conn.commit()

    # Update the grade of the student with the first name "Alice"
    update_student_grade(cursor, "Alice", 97.0)
    conn.commit()

    # Delete the student with the last name "Smith"
    delete_student(cursor, "Smith")
    conn.commit()

    # Fetch and display all student records
    cursor.execute("USE school")
    students = fetch_all_students(cursor)
    for student in students:
        print(student)

    # Close the cursor and connection
    cursor.close()
    conn.close()

if __name__ == "__main__":
    main()

import mysql.connector

# Database Connection
conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="YOUR_PASSWORD",
    database="studentdb"
)

cursor = conn.cursor()

# Add Student
def add_student():
    name = input("Enter Name: ")
    age = int(input("Enter Age: "))
    course = input("Enter Course: ")
    marks = float(input("Enter Marks: "))

    query = "INSERT INTO students(name, age, course, marks) VALUES (%s,%s,%s,%s)"
    values = (name, age, course, marks)

    cursor.execute(query, values)
    conn.commit()

    print("Student Added Successfully!")

# View Students
def view_students():
    cursor.execute("SELECT * FROM students")
    records = cursor.fetchall()

    print("\n----- Student Records -----")

    for row in records:
        print(row)

# Search Student
def search_student():
    sid = int(input("Enter Student ID: "))

    cursor.execute("SELECT * FROM students WHERE id=%s", (sid,))
    record = cursor.fetchone()

    if record:
        print(record)
    else:
        print("Student Not Found")

# Update Student
def update_student():
    sid = int(input("Enter Student ID: "))
    marks = float(input("Enter New Marks: "))

    cursor.execute(
        "UPDATE students SET marks=%s WHERE id=%s",
        (marks, sid)
    )

    conn.commit()
    print("Record Updated Successfully!")

# Delete Student
def delete_student():
    sid = int(input("Enter Student ID: "))

    cursor.execute(
        "DELETE FROM students WHERE id=%s",
        (sid,)
    )

    conn.commit()
    print("Student Deleted Successfully!")

# Main Menu
while True:
    print("\n===== STUDENT MANAGEMENT SYSTEM =====")
    print("1. Add Student")
    print("2. View Students")
    print("3. Search Student")
    print("4. Update Student")
    print("5. Delete Student")
    print("6. Exit")

    choice = int(input("Enter Choice: "))

    if choice == 1:
        add_student()

    elif choice == 2:
        view_students()

    elif choice == 3:
        search_student()

    elif choice == 4:
        update_student()

    elif choice == 5:
        delete_student()

    elif choice == 6:
        print("Thank You!")
        break

    else:
        print("Invalid Choice")

conn.close()

import sqlite3

con = sqlite3.connect('database.db')

cursor = con.cursor()

try:
    cursor.execute("DROP TABLE IF EXISTS Student;")
    cursor.execute("DROP TABLE IF EXISTS Department;")

    # use the execute method to create the first table
    cursor.execute("""CREATE TABLE IF NOT EXISTS Department(
        id INTEGER PRIMARY KEY,
        name TEXT);""")

    # create the second table and add a reference to the first
    cursor.execute("""CREATE TABLE IF NOT EXISTS Student(
        id INTEGER PRIMARY KEY,
        full_name TEXT,
        email TEXT,
        gpa REAL,
        department INTEGER,
        FOREIGN KEY (department) REFERENCES Department(id)
        );""")

    cursor.execute("""INSERT INTO Department(name) VALUES ('Engineering')""")
    cursor.execute("""INSERT INTO Department(name) VALUES ('Mathematics')""")
    new_department  = (45, 'Physics')
    cursor.execute("INSERT INTO Department(id, name) VALUES (?, ?)", new_department)

    students_list = [
        (1, 'Alan Turing', 'alan@mail.com', 9.5, 1),
        (2, 'Katherine Johnson', 'katherine@mail.com', 10.0, 2),
        (3, 'Helen Quinn', 'helen@mail.com', 8.7, 45),
    ]

    # Use executemany() to insert multiple records at the same time
    cursor.executemany('INSERT INTO Student VALUES(?, ?, ?, ?, ?)', students_list)

    con.commit() # saves the changes

    cursor.execute("SELECT *  FROM Student;")
    one_row = cursor.fetchone()
    print(one_row)
    # (1, 'Alan Turing', 'alan@mail.com', 9.5, 1)

    cursor.execute("SELECT *  FROM Student;")
    two_rows = cursor.fetchmany(2)
    print(two_rows)
    # [(1, 'Alan Turing', 'alan@mail.com', 9.5, 1),
    #  (2, 'Katherine Johnson', 'katherine@mail.com', 10.0, 2)]

    cursor.execute("SELECT * FROM student;")
    all_rows = cursor.fetchall()
    print(all_rows)
    # [(1, 'Alan Turing', 'alan@mail.com', 9.5, 1),
    #  (2, 'Katherine Johnson', 'katherine@mail.com' 10.0, 2),
    #  (3, 'Helen Quinn', 'helen@mail.com', 8.7, 45)]

    average_gpa = (9.5 + 10 + 8.7) / 3
    cursor.execute("SELECT * FROM student WHERE gpa >= ?", (average_gpa,))
    all_rows = cursor.fetchall()

    for student in all_rows:
        print(student[1])
        # Alan Turing
        # Katherine Johnson
except Exception as e:
    print("Error: ", e)
    con.rollback() # undo the changes

cursor.close()
con.close()

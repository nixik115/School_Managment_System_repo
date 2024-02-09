import sqlite3 #import necessary modules
 #creates a cursor object in database
from Person import *
from Student import *
from Teacher import *
from Course import *
from Exam import *



def create_tables(cursor,connection): #method of creating tables in database
    try:
        cursor.execute('''
  CREATE TABLE IF NOT EXISTS "Course" (
	"course_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"course_name"	TEXT,
	"room"	INTEGER,
	"teacher_id"	INTEGER,
	FOREIGN KEY("teacher_id") REFERENCES "Teacher"("teacher_id")
);
	     ''')
        cursor.execute('''
  CREATE TABLE IF NOT EXISTS "Student" (
	"student_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"email"	TEXT,
	"phone_number"	INTEGER,
	"course_id"	INTEGER,
	FOREIGN KEY("course_id") REFERENCES "Course"("course_id")
);
    	''')
        cursor.execute('''
 CREATE TABLE IF NOT EXISTS "Teacher" (
	"teacher_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"first_name"	TEXT,
	"last_name"	TEXT,
	"email"	TEXT,
	"phone_number"	INTEGER,
	"course_id"	INTEGER,
	FOREIGN KEY("course_id") REFERENCES "Course"("course_id")
);
    	''')
        cursor.execute('''
   CREATE TABLE IF NOT EXISTS "Exam" (
	"exam_id"	INTEGER PRIMARY KEY AUTOINCREMENT,
	"date"	REAL,
	"pass_mark"	INTEGER,
	"course_id"	INTEGER,
	FOREIGN KEY("course_id") REFERENCES "Course"("course_id")
);
    	''')



    except Exception as e:
        print(f"Connection failed {e}")

    finally:
        print("Closing database")
        connection.commit()

def main_menu(): #this function allows to manage different entities
    try:
        print('what would you like to manage:\n press 1 for Students,\n 2 for teachers,\n 3 for courses,\n 4 for exams')
        choice = input('Input your choice: ') #takes user input values

        if choice == '1':
            print('\n\nYou have chosen Student Management,\n press 1 to add a new user,\n 2 to update an exsiting student,\n 3 to delete a student,\n 4 to view all students details')
            student_management_choice = input('Input your choice: ')

            if student_management_choice == '1':
                student_id = input('Input student ID: ')
                s = Student(student_id, course_id)
                s.add_new_student(cursor, connection)
                s.print_student_details()

            elif student_management_choice == '2':
                student_id = input('Student ID :')
                first_name = input('input student name: ')
                last_name = input('Input student last name: ')
                email = input("enter student email address: ")
                phone_number = input("Student phone number: ")
                enrollment_date = input("Update enrollment date: ")
                course_id = input("Update course id: ")

                s = Student(student_id, enrollment_date, course_id)
                s.update_student(cursor, connection)
                s.print_student_details()

            elif student_management_choice == '3':
                student_id = input("Type in student ID: ")
                s = Student(student_id, enrollment_date="", course_id="", person_id="")
                s.delete_student(cursor,connection)
                s.print_student_details()

            elif student_management_choice == '4':
                Student.print_all_students_details(cursor,connection)

        else:
            print('input is not valid')

        if choice == '2':
            print('\n\nYou have chosen Teacher Management,\n press 1 to add a new teacher,\n 2 to update an exsiting teacher,\n 3 to delete a teacher,\n 4 to view all teacher details')
            teacher_management_choice = input('Input your choice: ')

            if teacher_management_choice == '1':
                teacher_id = input('input teacher id: ')
                email = input("enter teacher email address: ")
                password = input("enter the password: ")

                t = Teacher(teacher_id, email, password)
                t.add_new_teacher(cursor, connection)
                t.print_teacher_details()

            elif teacher_management_choice == '2':
               teacher_id = input('Type in teacher ID need updating: ')
               first_name = input('Updated teacher name : ')
               last_name = input('Updated teacher surname: ')
               email = input("Enter updated email: ")

               t = Teacher(teacher_id, first_name, last_name, email)
               t.update_teacher(cursor, connection)
               t.print_teacher_details()

            elif teacher_management_choice == '3':
                teacher_id = input("Type in teacher ID: ?")
                t = Teacher(teacher_id, first_name = " ", last_name = "",email =" ")
                t.delete_teacher(cursor, connection)
                t.print_teacher_details()

            elif teacher_management_choice == '4':
               Teacher.print_all_teacher_details(cursor, connection)

        else:
            print('input is not valid')

        if choice == '3':
            print('\n\nYou have chosen Course Management,\n press 1 to add a new course ,\n 2 to update an exsiting course,\n 3 to delete a course,\n 4 to view all course details')
            course_management_choice = input('Input your choice: ')

            if course_management_choice == '1':
                course_id = input('Type in Course ID: ')
                course_name = input('Type in Course name: ')
                room = input('What is room nr?: ')
                teacher_id = input('Teacher ID teaching in this room?: ')

                c = Course(course_id, course_name, teacher_id, room)
                c.add_new_course(cursor, connection)
                c.print_course_details()



            elif course_management_choice == '2':
                course_id = input('Type in Course ID need updating: ')
                course_name = input('Updated course name: ')
                room = input("Enter room nr: ")

                c = Course(course_id, course_name, room)
                c.update_course(cursor, connection)
                c.print_course_details()

            elif course_management_choice == '3':
                course_id = input("Type in course ID you want to delete: ")
                c = Course(course_id)
                c.delete_course(cursor, connection)
                c.print_course_details()

            elif course_management_choice == '4':
                  Course.print_all_course_details(cursor, connection)

        else:
            print('input is not valid')

        if choice == '4':
            print('\n\nYou have chosen Exam Management,\n press 1 to add a new exam ,\n 2 to update an exsiting exam,\n 3 to delete a exam,\n 4 to view all exam details')
            exam_management_choice = input('Input your choice: ')

            if exam_management_choice == '1':
                exam_id = input('Type in Exam ID: ')
                date = input('Type in exam date: ')
                pass_mark = input('What is pass mark?: ')
                course_id = input('Course ID related to exam?: ')
                e = Exam(exam_id, date, pass_mark, course_id)
                e.add_new_exam(cursor, connection)
                e.print_exam_details()



            elif exam_management_choice == '2':
                exam_id = input('Type in Exam ID need updating: ')
                date = input('Update exam date: ')
                pass_mark = input("Update room nr: ")
                e = Exam(exam_id, date, pass_mark)
                e.update_exam(cursor, connection)
                e.print_exam_details()

            elif exam_management_choice == '3':
                exam_id = input("Type in exam ID you want to delete: ")
                e = Exam(exam_id)
                e.delete_exam(cursor, connection)
                e.print_exam_details()

            elif exam_management_choice == '4':
                Exam.print_all_exam_details(cursor, connection)




        if choice not in ("1","2","3","4"):
            print("invlaid input, please choice ")



    finally:

        connection = sqlite3.connect('/Users/nikamakovejeva/Desktop/School_Managment_System2.db')  # connect to database
        cursor = connection.cursor()
        create_tables(cursor, connection)
        connection.close()
        main_menu()
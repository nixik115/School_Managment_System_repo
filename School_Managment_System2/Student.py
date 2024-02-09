from Person import *


class Student(Person):  # creating a new class which inherits from class User
    def __init__(self,first_name, last_name, email, phone_number, student_id, course_id):
        super().__init__(first_name, last_name, email, phone_number)
        self.student_id = student_id  # instance of the class  # instance of the class
        self.course_id = course_id  # instance of the class


    def print_student_details(self):  # creating a method to print student details
        print('Student Id:', self.student_id, 'Course enrolled:', self.course_id)  # print student information

    def print_all_students_details(self, cursor, connection):  # this method is made to execute SQL query that selects all columns from Student table
        cursor.execute("SELECT * FROM Student")
        connection.commit()  # commit changes to the database
        print(cursor.fetchall())  # print all rows fetched from Student table

    def add_new_student(self, cursor, connection):  # this method allows to add new student to the Database
        self.add_person(cursor,connetion)
        cursor.execute("INSERT INTO  Student (student_id, course_id , VALUES (?, ?, ?, ?)",
                       (self.student_id, self.course_id))
        connection.commit()
        print('Student Added Successfully')


    def update_student(self, cursor, connection):
        self.update_person(cursor, connection)
        cursor.execute("UPDATE Student SET first_name = ? ,last_name = ?, email = ?, phone_number = ?"
                       "WHERE student_id = ?", (self.first_name, self.last_name, self.email, self.phone_number))

        connection.commit()
        print('Student Updated Successfully')  # print success message

    def delete_student(self, cursor, connection):  # this method allows to delete student from database
	    cursor.execute("DELETE FROM Student WHERE student_id = ?", (self.student_id,))
	    connection.commit()
	    print('Student Deleted Successfully')

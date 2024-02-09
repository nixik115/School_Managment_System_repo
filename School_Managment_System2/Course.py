
class Course:  # Class which inherits from Teacher class
    def __init__(self, course_id, course_name, room, teacher_id):
        self.course_id = course_id
        self.course_name = course_name
        self.room = room
        self.teacher_id = teacher_id

    def print_course_details(self):
        print('Course ID:', self.course_id, ', Course Name:', self.course_name, 'Teacher_ID:', self.teacher_id,
              ', Room:', self.room)

    def print_all_course_details(self, cursor, connection):
        print('Course ID:', self.course_id, ', Course Name:', self.course_name, 'Teacher_ID:', self.teacher_id,
              ', Room:', self.room)
        cursor.execute("SELECT * FROM Course")
        connection.commit()
        print(cursor.fetchall())

    def add_new_course(self, cursor, connection):
        cursor.execute("INSERT INTO  Course (course_id, course_name, teacher_id, room) VALUES (?, ?, ?, ?)",
                       (self.course_id, self.course_name, self.teacher_id, self.room))
        connection.commit()
        print('Course Added Successfully')

    def update_course(self, cursor, connection):
        cursor.execute("UPDATE Course SET course_name = ? ,teacher_id = ?, room = ? WHERE course_id = ?",
                       (self.course_id, self.course_name, self.teacher_id, self.room))
        connection.commit()
        print('Course Updated Successfully')

    def delete_course(self, cursor, connection):
        cursor.execute("DELETE FROM Course WHERE course_id = ?", (self.course_id,))
        connection.commit()
        print('Course Deleted Successfully')

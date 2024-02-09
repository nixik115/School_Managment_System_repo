
class Exam:  # new class inhereting from class Course
    def __init__(self, exam_id, date, pass_mark, course_id):
        self.exam_id = exam_id
        self.date = date
        self.pass_mark = pass_mark
        self.course_id = course_id

    def print_exam_details(self):
        print('Exam ID:', self.exam_id, ', Date:', self.date, 'Pass mark:', self.pass_mark, 'Course ID', self.course_id)

    def print_all_exam_details(self, cursor, connection):
        cursor.execute("SELECT * FROM Exam")
        connection.commit()
        print(cursor.fetchall())

    def add_new_exam(self, cursor, connection):
        cursor.execute("INSERT INTO  Exam (exam_id, date, pass_mark ,course_id) VALUES (?, ?, ?, ?)",
                       (self.exam_id, self.date, self.pass_mark))
        connection.commit()
        print('Exam Added Successfully')

    def update_exam(self, cursor, connection):
        cursor.execute("UPDATE Exam SET exam_id = ? ,date  = ?, pass_mark = ? WHERE exam_id = ?",
                       (self.exam_id, self.date, self.pass_mark))
        connection.commit()
        print('Exam Updated Successfully')

    def delete_exam(self, cursor, connection):
        cursor.execute("DELETE FROM Exam WHERE exam_id = ?", (self.exam_id,))
        connection.commit()
        print('Exam Deleted Successfully')

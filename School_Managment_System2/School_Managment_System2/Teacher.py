from Person import Person
class Teacher(Person): #Another class created which inherits from parent class User
    def __init__(self, teacher_id, person_id, qualifications, first_name, last_name, email, phone_number):
        super().__init__(person_id, first_name, last_name, email, phone_number, 'Teacher', email, password)
        self.teacher_id = teacher_id
        self.qualifications = qualifications

    def print_teacher_details(self):
        print('Teacher Id:', self.teacher_id, 'Teacher qualifications ', self.qualifications, 'Teacher Name:', self.first_name, 'Teacher last name:', self.last_name, 'Teacher email:', self.email, 'Teacher phone number:', self.phone_number)

    def print_all_teacher_details(self, cursor, connection):
        cursor.execute("SELECT * FROM Teacher")
        connection.commit()
        print(cursor.fetchall())

    def add_new_teacher(self, cursor, connection):
        cursor.execute("INSERT INTO  Teacher (teacher_id, first_name, last_name, email, phone_number) VALUES (?, ?, ?, ?, ?)",
                       (self.teacher_id, self.first_name, self.last_name, self.email, self.phone_number))
        connection.commit()
        print('Teacher Added Successfully')

    def update_teacher(self,cursor,connection):
        cursor.execute("UPDATE Teacher SET first_name = ? ,last_name = ? ,email = ?, phone_number = ? WHERE teacher_id = ?", (self.first_name, self.last_name, self.email, self.phone_number, self.teacher_id))
        connection.commit()
        print('Teacher Updated Successfully')
    def delete_teacher(self,cursor,connection):
         cursor.execute("DELETE FROM Teacher WHERE teacher_id = ?", (self.teacher_id,))
	     connection.commit()
	     print('Teacher Deleted Successfully')
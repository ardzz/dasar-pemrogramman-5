from faker import Faker
from prettytable import PrettyTable


class Student:
    def __init__(self):
        self.students = {}

    def add_student(
            self, input_type='manual',
            name=None, age=None, birthday=None,
            birthplace=None, student_id=None, status=None,
            address=None, phone=None, email=None) -> bool:
        if input_type == 'manual':
            name = input('Name: ')
            age = input('Age: ')
            birthday = input('Birthday: ')
            birthplace = input('Birthplace: ')
            student_id = input('Student ID: ')
            status = input('Status: ')
            address = input('Address: ')
            phone = input('Phone: ')
            email = input('Email: ')
        self.students[student_id] = {
            'name': name,
            'age': age,
            'birthday': birthday,
            'birthplace': birthplace,
            'student_id': student_id,
            'status': status,
            'address': address,
            'phone': phone,
            'email': email
        }

        return student_id in self.students

    def get_student(self, student_id) -> dict | None:
        if student_id in self.students:
            return self.students[student_id]
        else:
            return None

    def get_all_students(self) -> dict:
        return self.students

    def update_student(self, student_id, key, value) -> bool:
        if student_id in self.students:
            self.students[student_id][key] = value
            return True
        else:
            return False

    def delete_student(self, student_id) -> bool:
        if student_id in self.students:
            del self.students[student_id]
            return True
        else:
            return False

    def print_all_students(self):
        table = PrettyTable()
        table.field_names = [
            'Name', 'Age', 'Birthday', 'Birthplace',
            'Student ID', 'Status', 'Address', 'Phone', 'Email'
        ]
        for student_id, student in self.students.items():
            table.add_row([
                student['name'], student['age'], student['birthday'],
                student['birthplace'], student['student_id'],
                student['status'], student['address'], student['phone'],
                student['email']
            ])
        print(table)

    def generate_fake_student(self, number_of_students=1):
        fake = Faker('id_ID')
        for i in range(number_of_students):
            self.add_student(
                input_type='fake',
                name=fake.name(),
                age=fake.random_int(min=18, max=25),
                birthday=fake.date(),
                birthplace=fake.city(),
                student_id=fake.random_int(min=100000, max=999999),
                status=fake.random_element(elements=('Active', 'Inactive')),
                address=fake.address(),
                phone=fake.phone_number(),
                email=fake.email()
            )

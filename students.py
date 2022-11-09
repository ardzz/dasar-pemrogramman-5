from student import Student


def menu():
    print('1. Add student')
    print('2. Get student')
    print('3. Update student')
    print('4. Delete student')
    print('5. Get all students')
    print('6. Generate fake student')
    print('7. Exit')
    return input('Choose menu: ')


def main():
    student = Student()
    while True:
        choice = menu()
        if choice == '1':
            if student.add_student():
                print('Success add student')
            else:
                print('Failed add student')

        elif choice == '2':
            student_id = input('Student ID: ')
            student_data = student.get_student(student_id)
            print("Nama: {}".format(student_data['name']))
            print("Umur: {}".format(student_data['age']))
            print("Tanggal Lahir: {}".format(student_data['birthday']))
            print("Tempat Lahir: {}".format(student_data['birthplace']))
            print("NISN: {}".format(student_data['student_id']))
            print("Status: {}".format(student_data['status']))
            print("Alamat: {}".format(student_data['address']))
            print("No. HP: {}".format(student_data['phone']))
            print("Email: {}".format(student_data['email']))

        elif choice == '3':
            student_id = input('Student ID: ')
            key = input('Key: ')
            value = input('Value: ')
            if student.update_student(student_id, key, value):
                print('Success update student')
            else:
                print('Failed update student')

        elif choice == '4':
            student_id = input('Student ID: ')
            if student.delete_student(student_id):
                print('Success delete student')
            else:
                print('Failed delete student')

        elif choice == '5':
            # check if there is no student
            if not student.get_all_students():
                print('There is no student')
            else:
                student.print_all_students()

        elif choice == '6':
            number_of_students = input('Number of students: ')
            student.generate_fake_student(int(number_of_students))

        elif choice == '7':
            break
        else:
            print('Invalid menu')


main()

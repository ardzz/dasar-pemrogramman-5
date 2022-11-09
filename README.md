### DASAR PEMROGRAMAN JOB SHEET 5: Fungsi

<p align="center">
    <img src="https://github.com/ardzz/dasar-pemrogaman-2/raw/master/images/logo-polines.png" alt="Logo Polines" width="300" height="300">
</p>

#### Dibuat dan disusun oleh


| Variabel | Nilai               |
| -------- | ------------------- |
| Nama     | Naufal Reky Ardhana |
| NIM      | 4.33.22.0.21        |
| Kelas    | TI-1A               |

**PROGRAM STUDI TEKNIK INFORMATIKA JURUSAN TEKNIK ELEKTRO POLITEKNIK NEGERI SEMARANG - 2022**

### Laporan Praktikum

#### Alat dan Bahan

- Laptop
- PyCharm IDE
- Python 3.10

#### Langkah Kerja

1. Buatlah sebuah fungsi yang dapat memberikan salam berdasarkan waktu saat ini

```python
import time



def get_current_time():
    current_time = int(time.strftime("%H"))
    if current_time < 12:
        return "Pagi"
    elif current_time < 15:
        return "Siang"
    elif current_time < 18:
        return "Sore"
    else:
        return "Malam"
  
def greet():
    print(f"Halo Reky, Selamat {get_current_time()}")


greet()
```

Output dari kode di atas adalah sebagai berikut:

<img src="screenshots/Screen Shot 2022-11-08 at 19.32.50.png"/>

2. Buatlah sebuah program yang dapat menampung data mahasiswa, yang NPM, Nama, kelas, jurusan dan angkatan

```python
from prettytable import PrettyTable

mahasiswa = []


def input_mahasiswa(data: dict):
    attributes = [
        "name", "npm", "kelas",
        "jurusan", "program_pendidikan", "angkatan"
    ]
    for attribute in attributes:
        if attribute not in data:
            raise Exception("Data must have all attributes")

    return mahasiswa.append(data)


def get_mahasiswa(npm: str) -> dict | None:
    for data in mahasiswa:
        if data["npm"] == npm:
            return data
    return None


def get_all_mahasiswa() -> list:
    return mahasiswa


def update_mahasiswa(npm: str, key: str, value: str) -> bool:
    for data in mahasiswa:
        if data["npm"] == npm:
            data[key] = value
            return True
    return False


def delete_mahasiswa(npm: str) -> bool:
    for data in mahasiswa:
        if data["npm"] == npm:
            mahasiswa.remove(data)
            return True
    return False


def print_all_mahasiswa():
    table = PrettyTable()
    table.field_names = [
        "Nama", "NPM", "Kelas",
        "Jurusan", "Program Pendidikan", "Angkatan"
    ]

    for data in mahasiswa:
        table.add_row([
            data["name"], data["npm"], data["kelas"],
            data["jurusan"], data["program_pendidikan"], data["angkatan"]
        ])

    print(table)


if __name__ == "__main__":
    while True:
        print("Mahasiswa")
        print("1. Input Mahasiswa")
        print("2. Get Mahasiswa")
        print("3. Update Mahasiswa")
        print("4. Delete Mahasiswa")
        print("5. Print All Mahasiswa")
        print("6. Exit")
        choice = input("Choose menu: ")

        if choice == "1":
            data = {
                "name": input("Nama: "),
                "npm": input("NPM: "),
                "kelas": input("Kelas: "),
                "jurusan": input("Jurusan: "),
                "program_pendidikan": input("Program Pendidikan: "),
                "angkatan": input("Angkatan: ")
            }
            input_mahasiswa(data)
            print("Success input mahasiswa")

        elif choice == "2":
            npm = input("NPM: ")
            data = get_mahasiswa(npm)
            print("Nama: {}".format(data["name"]))
            print("NPM: {}".format(data["npm"]))
            print("Kelas: {}".format(data["kelas"]))
            print("Jurusan: {}".format(data["jurusan"]))
            print("Program Pendidikan: {}".format(data["program_pendidikan"]))
            print("Angkatan: {}".format(data["angkatan"]))

        elif choice == "3":
            npm = input("NPM: ")
            key = input("Key: ")
            value = input("Value: ")
            if update_mahasiswa(npm, key, value):
                print("Success update mahasiswa")
            else:
                print("Failed update mahasiswa")

        elif choice == "4":
            npm = input("NPM: ")
            if delete_mahasiswa(npm):
                print("Success delete mahasiswa")
            else:
                print("Failed delete mahasiswa")

        elif choice == "5":
            print_all_mahasiswa()

        elif choice == "6":
            exit()
```

Output dari kode di atas adalah sebagai berikut:

<img src="screenshots/Screen Shot 2022-11-08 at 20.16.55.png"/>

3. Buatlah sebuah program python yang menggunakan metode rekursif

```python
def recursive(n):
    if n > 0:
        print(n)
        recursive(n-1)
    else:
        print(n)


number = int(input("Enter a number: "))
recursive(number)
```

Output dari kode di atas adalah sebagai berikut:

<img src="screenshots/Screen Shot 2022-11-08 at 20.19.58.png"/>

4. Sebuah sekolah ingin membuat sistem pendataan siswa, mahasiswa prodi Teknologi Rekayasa Komputer diminta membuatkan sistem tersebut untuk pendataan siswa menggunakan bahasa pemrograman python.

file `lib_students.py`

```python
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
```

file `student_management.py`

```python
from lib_students import Student

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
```

Output program di atas:

<img src="screenshots/Screen Shot 2022-11-08 at 20.33.07.png"/>

#### Kesimpulan

Dengan menggunakan fungsi, pekerjaan lebi mudah karena kita tidak perlu menulis ulang kode yang sama berkali-kali. Dengan menggunakan fungsi, kita bisa memanggil kode yang sudah kita tulis sebelumnya. Dengan menggunakan fungsi, kita bisa membuat kode kita lebih modular dan lebih mudah untuk dibaca.

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

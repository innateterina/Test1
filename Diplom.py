import datetime
import csv


class Person:

    def __init__(self, last_name, first_name, patronymic, date_of_birth, date_of_death, gender):
        self.first_name = first_name
        self.last_name = last_name
        self.patronymic = patronymic
        self.gender = gender
        self.date_of_birth = datetime.date(
            *reversed([int(item) for item in date_of_birth.split('-')]))
        self.date_of_death = date_of_death

    def alive(self, date_of_death):
        if len(date_of_death) == 0:
            print("Возраст:", (datetime.date.today() - self.date_of_birth).days // 365)
        else:
            self.date_of_death = datetime.date(
                *reversed([int(item) for item in date_of_death.split('-')]))
            print(f"Дата смерти: {self.date_of_death.strftime('%d-%m-%Y')} Человек прожил(лет):",
                  (self.date_of_death - self.date_of_birth).days // 365)

    def describe_human(self):
        if self.gender.find("ж"):
            print(f" {self.last_name} {self.first_name} {self.patronymic} "
                  f"родился {self.date_of_birth.strftime('%d-%m-%Y')}")
        else:
            print(f" {self.last_name} {self.first_name} {self.patronymic} "
                  f"родилась {self.date_of_birth.strftime('%d-%m-%Y')}")


def find_name(a, j):
    b = []
    for item in a:
        if j in ' '.join(item):
            b.append(item)
    return b


while True:
    answer = input("Выберите цифру:  1 - загрузить данные из ранее сохраненного файла,\n"
                   "2 - ввести данные и сохранить в новый файл,\n"
                   "3 - ввести данные нового человека и сохранить в ранее сохраненный файл,\n"
                   "4 - ввести данные нового человека и дозаписать в новый файл,\n"
                   "5 - поиск человека по имени,\n"
                   "6 - выход\n"
                   "Ваш ответ: ")
    if answer == "1":
        with open("diplom1.csv", mode="r", encoding="utf-8") as r_file:
            file_reader = csv.reader(r_file)
            count = 0
            data = []
            for item in file_reader:
                if count == 0:
                    name_of_data = item
                else:
                    data.append(item)
                count += 1
        print(name_of_data)
        print(data)
        print("-"*100)
    elif answer == "2":
        a = input("Введите фамилию: ")
        b = input("Введите имя: ")
        c = input("Введите отчество: ")
        d = input("Введите дату рождения в формате <д-м-год(0000)>: ")
        e = input("Введите дату смерти <д-м-год(0000)>, если человек жив - нажмите пробел: ")
        f = input("Введите пол человека(м/ж): ")
        name_of_fields = ["фамилия", "имя", "отчество", "дата рождения", "дата смерти", "пол"]
        person = [a, b, c, d, e, f]
        answer_1 = input("Желаете занести еще одного человека в базу данных? (Д/Y)")
        if answer_1.upper() in ('Y', 'Д', 'y', 'д'):
            a_1 = input("Введите фамилию: ")
            b_1 = input("Введите имя: ")
            c_1 = input("Введите отчество: ")
            d_1 = input("Введите дату рождения в формате <д/м/год(0000)>: ")
            e_1 = input("Введите дату смерти <д-м-год(0000)>, если человек жив - нажмите пробел: ")
            f_1 = input("Введите пол человека(м/ж): ")
            person_1 = [a_1, b_1, c_1, d_1, e_1, f_1]
            answer_1 = input("Желаете занести еще одного человека в базу данных? (Д/Y)")
            if answer_1.upper() in ('Y', 'Д', 'y', 'д'):
                a_2 = input("Введите фамилию: ")
                b_2 = input("Введите имя: ")
                c_2 = input("Введите отчество: ")
                d_2 = input("Введите дату рождения в формате <д/м/год(0000)>: ")
                e_2 = input("Введите дату смерти <д-м-год(0000)>, если человек жив - нажмите пробел: ")
                f_2 = input("Введите пол человека(м/ж): ")
                person_2 = [a_2, b_2, c_2, d_2, e_2, f_2]
                with open("diplom.csv", mode="w", encoding="utf-8") as w_file:
                    file_writer = csv.writer(w_file)
                    file_writer.writerow(name_of_fields)
                    file_writer.writerow(person)
                    file_writer.writerow(person_1)
                    file_writer.writerow(person_2)
            else:
                with open("diplom.csv", mode="w", encoding="utf-8") as w_file:
                    file_writer = csv.writer(w_file)
                    file_writer.writerow(name_of_fields)
                    file_writer.writerow(person)
                    file_writer.writerow(person_1)
        else:
            with open("diplom.csv", mode="w", encoding="utf-8") as w_file:
                file_writer = csv.writer(w_file)
                file_writer.writerow(name_of_fields)
                file_writer.writerow(person)
    elif answer == "3":
        a = input("Введите фамилию: ")
        b = input("Введите имя: ")
        c = input("Введите отчество: ")
        d = input("Введите дату рождения в формате <д/м/год(0000)>: ")
        e = input("Введите дату смерти <д-м-год(0000)>, если человек жив - нажмите пробел: ")
        f = input("Введите пол человека(м/ж): ")
        person = [a, b, c, d, e, f]
        with open("diplom1.csv", mode="a", encoding="utf-8") as file:
            file_writer = csv.writer(file)
            file_writer.writerow(person)
    elif answer == "4":
        a = input("Введите фамилию: ")
        b = input("Введите имя: ")
        c = input("Введите отчество: ")
        d = input("Введите дату рождения в формате <д/м/год(0000)>: ")
        e = input("Введите дату смерти <д-м-год(0000)>, если человек жив - нажмите пробел: ")
        f = input("Введите пол человека(м/ж): ")
        person = [a, b, c, d, e, f]
        with open("diplom.csv", mode="a", encoding="utf-8") as file:
            file_writer = csv.writer(file)
            file_writer.writerow(person)
    elif answer == "5":
        answer_2 = input("Желаете искать человека в ранее сохраненном файле? (Д/Y)")
        if answer_2.upper() in ('Y', 'Д', 'y', 'д'):
            with open("diplom1.csv", mode="r", encoding="utf-8") as r_file:
                file_reader = csv.reader(r_file)
                count = 0
                data = []
                for item in file_reader:
                    if count == 0:
                        name_of_data = item
                    else:
                        data.append(item)
                    count += 1
            j = input("Введите имя или фамилию человека: ")
            m = find_name(data, j)
            print(m)
            for item in m:
                n = Person(item[0], item[1], item[2], item[3], item[4], item[5])
                n.describe_human()
                n.alive(item[4])
            print("-" * 100)
        else:
            with open("diplom.csv", mode="r", encoding="utf-8") as r_file:
                file_reader = csv.reader(r_file)
                count = 0
                data = []
                for item in file_reader:
                    if count == 0:
                        name_of_data = item
                    else:
                        data.append(item)
                    count += 1
            j = input("Введите имя или фамилию человека: ")
            m = find_name(data, j)
            print(m)
            for item in m:
                n = Person(item[0], item[1], item[2], item[3], item[4], item[5])
                n.describe_human()
                n.alive(item[4])
            print("-"*100)
    else:
        break

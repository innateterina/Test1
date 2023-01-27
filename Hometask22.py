#Создать 2 класса truck и car, которые являются наследниками класса auto из предыдущего домашнего задания.
#Класс truck имеет дополнительный обязательный атрибут max_load.
#Переопределённый метод move, перед появлением надписи «move» выводит надпись «attention»,
# его реализацию сделать при помощи оператора super.
#А так же дополнительный метод load. При его вызове происходит пауза 1 сек.,
# затем выдаётся сообщение «load» и снова пауза 1 сек.
#Класс car имеет дополнительный обязательный атрибут max_speed и при вызове
#метода move, после появления надписи «move» должна появиться надпись
#«max speed is <max_speed>». Вместо <max_speed> должно выводится значение обязательного атрибума max_speed.
#Создать по 2 объекта для каждого из классов truck и car, проверить все их методы и атрибуты.
import time

class Auto(object):

    def __init__(self, brand, age, mark, color='black', weight=5.5):
        self.brand = brand
        self.age = age
        self.mark = mark
        self.color = color
        self.weigh = weight

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


class Truck(Auto):

    def __init__(self, brand, age, mark, max_load, color='black', weight=5.5):
        super().__init__(brand, age, mark, color, weight)
        self.max_load = max_load

    def move(self):
        print("Attention")
        super().move()

    def load(self):
        time.sleep(1)
        print("Load")
        time.sleep(1)


class Car(Auto):

    def __init__(self, brand, age, mark, max_speed, color='black', weight=5.5):
        super().__init__(brand, age, mark, color, weight)
        self.max_speed = max_speed

    def move(self):
        super().move()
        print("max speed is", self.max_speed)


truck_1 = Truck('Ram', 2017, 1500, 2300)
truck_2 = Truck('Ford', 2017, 'F-250', 4260)
car_1 = Car('Ford', 2016, 'Fiesta', '112 mph')
car_2 = Car('Ford', 2015, 'Fusion', '122mph')

print(truck_1.brand)
print(truck_1.age)
print(truck_1.mark)
print(truck_1.max_load)
print(truck_1.color)
print(truck_1.weigh)
truck_1.move()
truck_1.birthday()
print(truck_1.age)
truck_1.stop()
truck_1.load()

print('-' * 50)

print(truck_2.brand)
print(truck_2.age)
print(truck_2.mark)
print(truck_2.max_load)
print(truck_2.color)
print(truck_2.weigh)
truck_2.move()
truck_2.birthday()
print(truck_2.age)
truck_2.stop()
truck_2.load()

print('-' * 50)

print(car_1.brand)
print(car_1.age)
print(car_1.mark)
print(car_1.max_speed)
print(car_1.color)
print(car_1.weigh)
car_1.move()
car_1.birthday()
print(car_1.age)
car_1.stop()

print('-' * 50)

print(car_2.brand)
print(car_2.age)
print(car_2.mark)
print(car_2.max_speed)
print(car_2.color)
print(car_2.weigh)
car_2.move()
car_2.birthday()
print(car_2.age)
car_2.stop()



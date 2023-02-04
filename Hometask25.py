#Создайте свой произвольный класс и
# в нём помимо обычных методов и атрибутов создайте несколько статических методов и методов класса.
#Продемонстрируйте их работу.

class MyNewClass(object):
    AGE = 6
    NAME = 'Ben'
    COLOR_OF_HAIR = 'black'

    def __init__(self, name='Bob', age=1, hair='white'):
        self.age = age
        self.name = name
        self.hair = hair

    @staticmethod
    def my_first():
        print("Good morning")

    @staticmethod
    def my_second():
        print("Good afternoon")

    @staticmethod
    def my_third():
        print("Good evening")

    def new_age(self):
        self.age += 1

    def for_hair(self):
        print("long " + self.hair)

    @classmethod
    def class_age(cls):
        print("My class age:", cls.AGE)

    @classmethod
    def class_name(cls):
        print("My class name:", cls.NAME)

    @classmethod
    def class_color(cls):
        print("My class hair: short", cls.COLOR_OF_HAIR)

a = MyNewClass()
print(a.name)
print(a.age)
a.new_age()
print(a.age)
a.class_age()
a.class_name()
a.my_first()
a.for_hair()
a.class_color()





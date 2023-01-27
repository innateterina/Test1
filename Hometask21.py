#Создать родительский класс auto, у которого есть атрибуты:
#brand, age, cоlor, mark и weight.
#А так же методы: move, birthday и stop.
#Методы move и stop выводят сообщение на экран «move» и «stop»,а birthday увеличивает атрибут age на 1.
#Атрибуты brand, age и mark являются обязательными при объявлении объекта.

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


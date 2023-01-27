#Создать родительский класс auto, у которого есть атрибуты:
#brand, age, cоlor, mark и weight.
#А так же методы: move, birthday и stop.
#Методы move и stop выводят сообщение на экран «move» и «stop»,а birthday увеличивает атрибут age на 1.
#Атрибуты brand, age и mark являются обязательными при объявлении объекта.

class Auto(object):
    brand = 'Ford'
    age = 5
    mark = 'Focus'
    color = 'black'
    weight = 5.5

    def __int__(self, brand='Ford', age=5, mark='Focus'):
        self.brand = brand
        self.age = age
        self.mark = mark

    def move(self):
        print("move")

    def stop(self):
        print("stop")

    def birthday(self):
        self.age += 1


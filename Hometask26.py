#Создать программу-калькулятор в виде класса и несколько методов,
# как минимум сложение, вычитание, деление, умножение, возведение в степень и извлечение квадратного корня.
#Обернуть каждый метод в блок try/except и сделать обработку нескольких исключений, как минимум деление на 0.
#Создать своё исключение, к примеру возведение в отрицательную степень.
import math


class NewException(Exception):
    def __init__(self, message='Возведение в отрицательную степень недопустимо'):
        super().__init__(message)


class Calculator(object):
    def __init__(self, a=0, b=0):
        self.a = a
        self.b = b

    def addition(self, a, b):
        try:
            return a + b
        except TypeError:
            print('Wrong type instead of "int" or "float')

    def substraction(self, a, b):
        try:
            return a - b
        except TypeError:
            print('Wrong type instead of "int"')

    def division(self, a, b):
        try:
            return a / b
        except ZeroDivisionError:
            print('You can not divide by zero')
        except TypeError:
            print('Wrong type instead of "int" or "float"')

    def multiplication(self, a, b):
        try:
            return a * b
        except TypeError:
            print('Wrong type instead of "int" or "float"')
        except Exception:
            print(Exception)

    def exponentiation(self, a, b):
        try:
            if b < 0:
                raise NewException
            print(a ** b)
        except TypeError:
            print('Wrong type instead of "int" or "float"')
        except NewException as err:
            print(err)


    def root_extraction(self, a):
        try:
            print(math.sqrt(a))
        except ValueError:
            print('Нельзя извлечь квадратный корень из отрицательного числа')
        except TypeError:
            print('Wrong type instead of "int" or "float"')


s = Calculator()
print(s.addition(5, 8))
print(s.substraction(9, 7))
print(s.division(9, 7))
print(s.multiplication(2, 3))
s.exponentiation(2, -4)
s.root_extraction(-4)

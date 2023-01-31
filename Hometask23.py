#Для рассмотренного на уроке класса Circle реализовать метод производящий вычитание двух окружностей,
# вычитание радиусов произвести по модулю. Если вычитаются две окружности с одинаковым значением радиуса,
# то результатом вычитания будет точка класса Point.

import math


class Point():

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        return Point(x, y)

    def __str__(self):
        return f'({self.x}, {self.y})'

    def distance_from_origin(self):
        return math.hypot(self.x, self.y)


class Circle(Point):

    def __init__(self, radius, x=0, y=0):
        super().__init__(x, y)
        self.radius = radius

    def __eq__(self, other):
        return self.radius == other.radius

    def __str__(self):
        return f'(radius={self.radius}, ' + super().__str__()[1:]

    def __add__(self, other):
        x = self.x + other.x
        y = self.y + other.y
        radius = self.radius + other.radius
        return Circle(radius, x, y)

    def __sub__(self, other):
        x = self.x - other.x
        y = self.y - other.y
        radius = abs(self.radius - other.radius)
        return Point(x, y) if self.radius == other.radius else Circle(radius, x, y)

    def edge_distance_from_origin(self):
        return abs(self.distance_from_origin() - self.radius)

    def circumference(self):
        return 2 * math.pi * self.radius

    def area(self):
        return math.pi * (self.radius**2)

    def sub_of_cirsum_of_circle(self, other):
        return abs(self.circumference() - other.circumference())



a = Circle(6, 9, 0)
print(a.circumference())
b = Circle(6, 6, 0)
print(b.circumference())
c = abs(a.circumference() - b.circumference())
print(c)
d = abs(a.area() - b.area())
print(d)

a_1 = Circle(3, 9, 0)
print(a_1.circumference())
b_1 = Circle(9, 6, 0)
print(b_1.circumference())
c_1 = abs(a_1.circumference() - b_1.circumference())
print(c_1)
d_1 = abs(a_1.area() - b_1.area())
print(d_1)

a_2 = Circle(6, 9, 0)
b_2 = Circle(3, 6, 0)
print(a_2.sub_of_cirsum_of_circle(b_2))
print(a_2.__sub__(b_2))


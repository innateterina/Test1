class String(str):
    def __add__(self, other):
        return f'{str(self)}{str(other)}'

    def __sub__(self, other):
        return str(self).replace(str(other), '', 1)





a = String('NoneType')
b = None
print(a - b)
print(type(a - b))

a_1 = String('New')
b_1 = True
print(a_1 + b_1)
print(type(a_1 + b_1))
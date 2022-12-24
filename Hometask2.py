a = (5,)
a_1 = (5,)
a_2 = (5,)

print(a == a_1 == a_2)
print(a is a_1 is a_2)
a = set(a)
a_1 = set(a_1)
a_2 = set(a_2)

print(a == a_1 == a_2)
print(a is a_1 is a_2)


b = {1, 5, 2}
b_1 = {1, 2, 5}
print(b == b_1)
print(b is b_1)

b = bool(b)
b_1 = bool(b_1)
print(b == b_1)
print(b is b_1)

#Создать генератор геометрической прогрессии

def geometric_progression(a, b):
    current = 1
    for item in range(b):
        current *= a
        yield current


for x in geometric_progression(5, 10):
    print(x)


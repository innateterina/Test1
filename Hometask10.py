#Дан список состоящий из данных разного типа.
#Вернуть новый список, где при помощи функции map(),
# каждый элемент типа int первоначального списка приведён к типу str,
# элементы всех остальных типов передаются в новый список без изменения их типа.
#В качестве входной функции в map() использовать lambda-функцию.

value = [1, 2, '3', 'forth', 'end', 99, True, None]

value_2 = list(map(lambda a: str(a) if isinstance(a, int) else a, value))

print(value_2)


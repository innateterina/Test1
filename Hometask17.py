#Дана строка в байтовом виде: b'r\xc3\xa9sum\xc3\xa9'.
#Декодировать её в строковый вид в кодировке по умолчанию.
#Затем результат преобразовать снова в байтовый, только уже в кодировке ‘Latin1’.
#И на конец результат снова декодировать в строку.
#(результаты всех преобразований выводить на экран).

bytes = b'r\xc3\xa9sum\xc3\xa9'
d = bytes.decode()
print(d)
bytes_2 = d.encode("Latin1")
print(bytes_2)
print(bytes_2.decode("Latin1"))
#print(bytes_2.decode("utf-8", errors='ignore'))
#print(bytes_2.decode("utf-16"))
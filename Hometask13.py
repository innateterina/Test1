#Сделать программу в виде функции в которой нужно будет угадывать число.
def number():
    for i in range(1, 30 + 1):
        a = int(input('Угадайте число от 1 до 30: '))
        while a != i:
            if a < i:
                    i += 2
                    print('Ваше число меньше, чем загадал компьютер')
            elif a > i:
                    print('Ваше число больше, чем загадал компьютер')
            a = int(input('Повторите попытку '))
        print('Вы угадали')
    return

number()
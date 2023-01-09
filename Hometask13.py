def func_2():
    answer = input('Ваше нечетное число больше 2? (Д/H): ')
    if answer.upper() in ('Д', 'д'):
        answer_1 = input('Ваше число больше 4? (Д/H): ')

    elif answer.upper() in ('Н', 'н'):
        print('Вы загадали число 1')

    if answer_1.upper() in ('Д', 'д'):
        answer_2 = input('Ваше число больше 6? (Д/H): ')

    elif answer_1.upper() in ('Н', 'н'):
        print('Вы загадали число 3')

    if answer_2.upper() in ('Д', 'д'):
        answer_3 = input('Ваше число больше 8? (Д/H): ')

    elif answer_2.upper() in ('Н', 'н'):
        print('Вы загадали число 5')

    if answer_3.upper() in ('Д', 'д'):
        print('Вы загадали число 9')
    else:
        print('Вы загадали число 7')

    return

def func_1():
    print(input('Загадайте число от 1 до 9 и нажмите Enter:'))
    answer = input('Ваше число четное? (Д/H): ')
    if answer.upper() in ('Д', 'д'):
        answer_1 = input('Ваше число больше 3? (Д/H): ')
    elif answer.upper() in ('н', 'Н'):
        print(func_2())
    if answer_1.upper() in ('Д', 'д'):
        answer_2 = input('Ваше число больше 5? (Д/H): ')
    elif answer_1.upper() in ('Н', 'н'):
        print('Вы загадали число 2')
    if answer_2.upper() in ('Д', 'д'):
        answer_3 = input('Ваше число больше 7? (Д/H): ')
    elif answer_2.upper() in ('Н', 'н'):
        print('Вы загадали число 4')
    if answer_3.upper() in ('Д', 'д'):
        print('Вы загадали число 8'
    elif answer_3.upper() in ('Н', 'н'):
        print('Вы загадали число 6')

    return



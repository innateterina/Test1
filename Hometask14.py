#Написать программу которая состоит из вечного цикла ожидающего ввод числа или одно из значений:
# "выход", "exit", "quit", "e" или "q" в любом регистре.
# При вводе одного из этих значений происходит выход из вечного цикла.
# При любом другом вводе вызывается отдельная функция которая умеет распознавать введённые числа.
# Сама функция ничего не распечатывает, она возвращает строку, типа:
# "Вы ввели отрицательное дробное число: -6.7" или "Вы ввели не корректное число: Erdf"
#Затем в цикле выводится это сообщение и цикл начинается заново ожидая следующего ввода.
#Функция на вход принимает строку из ввода из вечного цикла.
# #Анализирует её исключительно методом .isdigit() и другими методами строк,
# без доп.библиотек и переводит строку в число, если это возможно.
#Функция умеет распознавать отрицательные числа и десятичные дроби,
# а так же распознаёт десятичные дроби как с точкой, так и с запятой.
#Функция возвращает строку в которой описывается какое число введено - отрицательное или положительно,
# целое или дробное и выводит его или же сообщает, что введено не корректное число.
#*Дополнительно: правильно распознаётся десятичная дробь без первого значащего нуля

def func_1(number):
    if number.isdigit():
        if number.__contains__('0') and len(number) == 1:
            print('вы  ввели ноль')
        elif int(number) > 0:
            print('вы ввели целое положительное число:', number)
    elif number.isdigit() != True:
        if number.replace('-', '', 1):
           if number.isdigit():
                print('вы ввели целое отрицательное число:', number)
        elif number.replace('.', '', 1):
            if number.matches('0+') and number.isdigit():
                if True:
                    print(('вы  ввели ноль'))
            elif number.isdigit():
                    print('вы ввели отрицательное дробное число:', number)
        elif len(number.replace('-', '', 1)) == len(number) and number.replace('.', '', 1):
                if number.isdigit():
                    print('вы ввели положительное дробное число:', number)
                else:
                    print('вы ввели некоректное число')
        else:
            print('вы ввели некоректное число')
    else:
        print('вы ввели некоректное число')

        return


while True:
        number = input('введите число: ')
        number = number.replace(',', '.')
        if number.replace('-', '', 1) and number[0] == 0 and number[1] == '.':
            number.replace('0', '', 1)  #это условие для игнорирования первого значащего нуля,там ли оно где нужно
        elif number != number.isalpha():
            func_1(number)
        else:
            print('Вы ввели некорректное число')

        answer = input('Для выхода из цикла введите:выход/exit/quit/e/q: ')
        if answer.upper() in ('exit', 'quit', 'e', 'q', 'выход'):
            break
---------------------------------------
def func_1(number):
    if number.isdigit():
        if number.__contains__('0') and len(number) == 1:
            print('вы  ввели ноль')
        elif int(number) > 0:
            print('вы ввели целое положительное число:', number)
    elif number.isdigit() == False:
        if number.replace('-', '', 1) and number.isdigit():
            print('вы ввели целое отрицательное число:', number)
        elif number.replace('.', '', 1) and number.isdigit():
                print('вы ввели положительное дробное число:', number)
        elif number.replace('.', '', 1) and number.replace('-', '', 1):
            if number.isdigit():
                print('вы ввели положительное дробное число:', number)
            else:
                print('вы ввели некоректное число')
        else:
            print('вы ввели некоректное число')
    else:
        print('вы ввели некоректное число')
        return

while True:
        number = input('введите число: ')
        number = number.replace(',', '.')
        if number[0] == 0 and number[1] == '.':
            number.replace('0', '', 1)
        if number != number.isalpha():
            func_1(number)
        else:
            print('Вы ввели некорректное число')

        answer = input('Для выхода из цикла введите:выход/exit/quit/e/q: ')
        if answer.upper() in ('exit', 'quit', 'e', 'q', 'выход'):
            break

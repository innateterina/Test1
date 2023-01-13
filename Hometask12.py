#Написать декоратор к 2-м любым функциям, который бы считал и выводил время их выполнения.
#Подсказка:
#from datetime import datetime
#time = datetime.now()



def decorator_duration(my_function):
    def wrapper():
        from datetime import datetime
        time_1 = datetime.now()
        print('time_1:', time_1)
        my_function()
        time_2 = datetime.now()
        print('time_2:', time_2)
        print('function_time_fulfillment:', time_2 - time_1)

    return wrapper


@decorator_duration
def addition():
    add = 5 + 8
    print('add:', add)

addition()

print('--'*50)

@decorator_duration
def multiplication():
    multiplic = 5 * 8
    print('multiplic:', multiplic)

multiplication()
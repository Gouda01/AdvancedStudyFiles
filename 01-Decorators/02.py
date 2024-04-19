def mydecorator_function(func):
    def wrapper():
        resault = func()
        return resault.upper()

    return wrapper


@mydecorator_function
def my_upper():
    return('hello world ......')


print(my_upper())
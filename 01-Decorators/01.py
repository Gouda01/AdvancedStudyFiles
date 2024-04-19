def mydecorator_function(func):
    def wrapper_function():
        print('Start .....')
        func()
        print('End ......')

    return wrapper_function


@mydecorator_function
def hello():
    print('Hello world ....')



hello()
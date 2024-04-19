import time

def calculate_excution_time(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        func(*args, **kwargs)
        end_time = time.time()

        print(f"Execution time for {func.__name__} = {end_time - start_time}")

    return wrapper


@calculate_excution_time
def myfunc(x):
    for _ in range(x) :
        pass


myfunc(100000000)
    
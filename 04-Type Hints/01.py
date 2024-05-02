# We can define if integer or string

x:int = 10


def mysum(x:int, y:int) -> int:             # Return with int
    print(x+y)


def mysum(x:int, y:int) -> list[str]:       # Return with List
    print(x+y)

def mysum(x:int, y:int) -> None:            # Return with None
    print(x+y)
# We can define if integer or string

x:int = 10


def mysum(x:int, y:int) -> int:
    print(x+y)


def mysum(x:int, y:int) -> list[str]:
    print(x+y)
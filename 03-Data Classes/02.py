# With Data Classes :

from dataclasses import dataclass


@dataclass
class Person:
    name:str
    age:int


p1 = Person('Mohamed',20)

print(p1.name)
print(p1.age)
print(p1)
    
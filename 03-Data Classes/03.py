# With Data Classes :
# Make compare :

from dataclasses import dataclass


@dataclass
class Person:
    name:str
    age:int


p1 = Person('Mohamed',20)
p2 = Person('Ali',22)
p3 = Person('Mohamed',20)

print(p1 == p2)
print(p1 == p3)

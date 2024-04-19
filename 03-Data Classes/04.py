# With Data Classes :
# Make compare with orders  as  > and < : 

from dataclasses import dataclass


@dataclass(order=True)
class Person:
    name:str
    age:int


p1 = Person('Mohamed',20)
p2 = Person('Ali',22)
p3 = Person('Mohamed',20)

print(p1 > p2)
print(p1 > p3)
print(p1 >= p3)

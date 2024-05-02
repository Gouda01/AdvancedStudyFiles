class Calc :
    def sum(self, x:int, y:int) -> int :
        return x + y
    
    def mul(self, x:int, y:int) -> int :
        return x * y
    

c = Calc()
print(c.sum(3,4))
print(c.mul(4,5))
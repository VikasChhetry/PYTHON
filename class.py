class Myclass:
    def __init__(self,a,b):
        self.a = a
        self.b = b
    def __str__(self):
        return f"{self.a} and {self.b}"
M=Myclass(3,4)
print(M)            


####NAME SPACE

x=200
def outer():
    x=300
    def inner(): 
        print(x)
    inner()    
outer()    
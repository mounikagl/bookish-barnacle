class Descriptors:
    def __init__(self, x=" "): 
        self.x = x
    
    def __get__(self, obj, objtype):
        return "{} for {} ".format(self.x, self.x)

    def __set__(self, obj, x):
        if isinstance(x, str):
            self.x = x
        else:
            raise TypeError("x should be string")

class A(object):
    x = Descriptors()

y = A()
y.x = 'John'
print(y.x)

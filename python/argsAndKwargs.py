# def myfunc(a , b):
#     return a+b

# result = myfunc(20,40)
# print(result)

# def myfunc(a,b,c):
#     return (a+b+c)*0.05

# result = myfunc(40,23,34)
# print(round(result))
import math

def myfunc(*args):
    return sum((args))*0.05

result = myfunc(40,23,34)
print(round(result))
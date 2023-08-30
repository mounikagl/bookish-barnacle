def x(a):
    return a*2

# print(x(2))
y = [x(a) for a in range(10) if a%2==0]
print(y)
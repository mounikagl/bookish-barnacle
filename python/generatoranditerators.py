def gencubes(n):
    for num in range(n):
        yield num**2
for x in gencubes(10):
    print(x)
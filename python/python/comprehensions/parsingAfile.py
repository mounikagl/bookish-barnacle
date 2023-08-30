op = open("sample.txt", 'r')

x = [a for a in op if 'parsing' in a]
print(x)

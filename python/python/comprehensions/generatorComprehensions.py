input = [1,2,3,2,4,5,6,6,6,7,8]

output = (var for var in input if var%2==0)
# print(output)
print("Values of generator comprehenions are:", end='')
for var in output:
    print(var, end='')
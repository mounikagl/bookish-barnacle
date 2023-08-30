input = [1,2,2,3,4,4,5,6,6,6,7,7,8]

# output = set()

# for var in input:
#     if var%2 == 0:
#         output.add(var)
# print(output)

output = {var for var in input if var%2==0}
print(output)
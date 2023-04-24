# myset = set()
# # print(myset)
# myset.add(1)
# print(myset)
# myset.add(2)
# print(myset)

set1 = {1,2,3,4}
set2 = {6,3,5,2}

# my_set = set1.union(set2)
# print(my_set)

# my_set = set1.intersection(set2)
# print(my_set)

my_set = set1.difference(set2)
print(my_set)

my_set = set2.difference(set1)
print(my_set)
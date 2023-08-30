#squares of numbers
num = [1, 2, 3, 4, 5]

#  using list comprehension

squares = [n**2 for n in num] 
            # if n%2 == 0]

# sqaures = []

# for n in num:
#     sqaures.append(n**2)

print(squares)

# finding common num from two lists using list comprehensions
list1 = [1,2,3,4,5,6]
list2 = [1,3,4,5,7]

intersection = []

for x in list1:
    for y in list2:
        if x==y:
            intersection.append(x)

print(intersection)

# using list comprehension

list1 = [1,2,3,4,5,6]
list2 = [1,3,4,5,7]
 
# finding common num from two lists using list comprehensions
intersection = [x for x in list1 for y in list2 if x==y]

# return numbers from the list which are not equal as tuple
intersection = [(x,y) for x in list1 for y in list2 if x!=y]

print(intersection)

# iterate over a string using list comprehension
list = ["Hello World", "Python", "Java", "C", "HTML", "CSS"]

x = [str.upper() for str in list]

print(x)

# produce a list of a list using list comprehension
list = [1,2,3,4,5]

x = [[a**2, a**3] for a in list]

print(x)


# class Trees():
#     def __init__(self,name):
#         self.name = name

# tree_name = Trees(name = 'Coconut')
# print(tree_name.name)
# print(type(tree_name))

# class Trees():
#     def __init__(self,name,fruits):
#         self.name = name
#         self.fruits = fruits

# tree_name = Trees(name = 'Coconut\n', fruits = True)
# print(tree_name.name, tree_name.fruits)
# print(type(tree_name))

# class Trees():
#     def __init__(self,name):
#         self.name = name

#     def height(self):
#         self.height = height

# tree_name = Trees(name = 'Coconut')
# print(tree_name.name)
# print(type(tree_name))

# import math

class circle():
     pi = 3.14

     def __init__(self, radius=1):
        self.radius = radius
        self.area = radius*radius*circle.pi

     def setRadius(self, new_radius):
        self.radius = new_radius
        self.area = new_radius*new_radius*circle.pi

     def getCircumference(self):
        return self.radius*self.pi*2
    
c = circle()

print("Radhius: ", c.radius)
print("Area : ", c.area)
print("Circumference: ", c.getCircumference())

c.setRadius(2)

print("Radhius: ", c.radius)
print("Area : ", c.area)
print("Circumference: ", c.getCircumference())

# class Dog:
#     def __init__(self,name):
#         self.name = name

#     def Sound(self):
#         return self.name + " souns like Wooof"

# class Cat:
#     def __init__(self,name):
#         self.name = name

#     def Sound(self):
#         return self.name + " sounds like Meow"

# animal1 = Dog("Huskie")
# animal2 = Cat("Teddy")

# print(animal1.Sound())
# print(animal2.Sound())

# for pet in [animal1, animal2]:
#     print(pet.Sound())




# class Animal:
#       def __init__(self, name):    # Constructor of the class
#         self.name = name

#       def speak(self):              # Abstract method, defined by convention only
#         raise NotImplementedError("Subclass must implement abstract method")


# class Dog(Animal):
    
#     def speak(self):
#         return self.name+' says Woof!'
    
# class Cat(Animal):

#     def speak(self):
#         return self.name+' says Meow!'
    
# fido = Dog('Fido')
# isis = Cat('Isis')

# print(fido.speak())
# print(isis.speak())

# ******SPECIAL FUNCTIONS******
class Book:
    def __init__(self, title, author, pages):
        print("A book is created")
        self.title = title
        self.author = author
        self.pages = pages

    def __str__(self):
        return "Title: %s, author: %s, pages: %s" %(self.title, self.author, self.pages)

    def __len__(self):
        return self.pages

    def __del__(self):
        print("A book is destroyed")

book = Book("Python Rocks!", "Jose Portilla", 159)

print(book)
print(len(book))
del book
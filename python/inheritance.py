# class Flowers():

#     def __init__(self):
#         print("Welcome to Flowers shop")

#     def WhichFlower(self):
#         print("Rose")

#     def Smell(self):
#         print("Smells Good")

# class Rose(Flowers):

#     def __init__(self):
#         Flowers.__init__(self)
#         print("Flowers are there")

#     def RoseColor(self):
#         print("Roses are Red")

# r = Rose()

# r.WhichFlower()
# r.Smell()
# r.RoseColor()

class Flowers:

    def __init__(self):
        print("*****Welcome to Flower shop*****")
        name = input("What Flowers are there? ")
        self.flower = None
        self.smell = None

    def WhichFlower(self):
        self.flower = input("Which Flowers are there? ")

    def Smell(self):
        smell = input("How does the flower smell? ")


class Rose(Flowers):

    def __init__(self):
        super().__init__()
        print("Many roses available")
        self.color = None

    def RoseColor(self):
        self.color = input("What color are the Roses? ")

r = Rose()

r.WhichFlower()
r.Smell()
r.RoseColor()


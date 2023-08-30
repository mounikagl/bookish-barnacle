# import random
# import time

# class Lazy:
#     def __init__(self, function):
#         self.function = function
#         self.name = function.__name__
#         def __get__(self, obj, type=None) -> object:
#             obj.__dict__[self.name] = self.function(obj)
#             return obj.__dict__[self.name]

#         def __set__(self, obj, value):
#             pass

# class Waiting:
#     @Lazy
#     def wait(self):
#             time.sleep(4)
#             return 42

# x = Waiting()
# print(x.wait)
# print(x.wait)
# print(x.wait)
# print(x.wait)
# print(x.wait)
# print(x.wait)

class EvenNumber:
    def __set_name__(self, owmer, name):
        self.name = name

    def __get__(self, obj, type=None)->object:
        return obj.__dict__.get(self.name) or 0

    def __set__(self, obj, value)->None:
        obj.__dict__(self.name) == (value if value %2 ==0 else 0)

class Values:
    def __init__(self):
        self.value1 = 0
        self.value2 = 0
        self.value3 = 0
        self.value4 = 0
        self.value5 = 0

    @property 
    def value1(self):
        return self._value1

    @value1.setter
    def value1(self, value):
        self._value1 = value if value%2 == 0 else 0

    @property
    def value2(self):
        return self._value2

    @value2.setter
    def value2(self, value):
        self._value2 = value if value%2 == 0 else 0

    @property
    def value3(self):
        return self._value3

    @value3.setter
    def value3(self, value):
        self._value3 = value if value%2 == 0 else 0

    @property
    def value4(self):
        return self._value4

    @value4.setter
    def value4(self, value):
        self._value4 = value if value%2 == 0 else 0

    @property
    def value5(self):
        return self._value5

    @value5.setter
    def value5(self, value):
        self._value5 = value if value%2 == 0 else 0

my_values = Values()

my_values.value1 = 1
my_values.value2 = 4
print(my_values.value1)
print(my_values.value2)
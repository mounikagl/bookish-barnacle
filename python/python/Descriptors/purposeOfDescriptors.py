# class Person:
#     def __init__(self, name, age, bmi):
#         self.name = name
#         self.age = age
#         self.bmi = bmi

#         if isinstance(self.name, str):
#             print(self.name)
#         else:
#             raise ValueError("Name can never be INTEGER value")
#         if self.bmi < 0:
#             raise ValueError("BMI can never be less than ZERO")


#     def __str__(self):
#         return "{0} age is {1} with BMI of {2}" .format(self.name, self.age, self.bmi)

# person1 = Person('JOHN', '25', 19)
# print(person1)
# # person2 = Person(12, '32', -12)
# # print(person2)
# person1.name = 12 #error is not raising here to solve we use descriptors
# print(person1)


class DescriptorsBmi:
    def __init__(self):
        self.__bmi =0
    def __get__(self, instance, owner):
        return self.__bmi
    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else:
            raise TypeError("BMI can only be interger value")
        if value <= 0:
            raise ValueError("BMI should be always greater than zero")

        self.__bmi = value
    def __delete__(self, instance):
        del self.__bmi

class DescriptorsName:
    def __init__(self):
        self.__name =0
    def __get__(self, instance, owner):
        return self.__name
    def __set__(self, instance, value):
        if isinstance(value, str):
            print(value)
        else:
            raise TypeError("Name cannot be interger value")

        self.__name = value
    def __delete__(self, instance):
        del self.__name


class DescriptorsAge:
    def __init__(self):
        self.__age =0
    def __get__(self, instance, owner):
        return self.__age
    def __set__(self, instance, value):
        if isinstance(value, int):
            print(value)
        else:
            raise TypeError("age can only be interger value")
        if value < 0:
            raise ValueError("age cannot be a negative value")

        self.__age = value
    def __delete__(self, instance):
        del self.__age


class Person:

    bmi = DescriptorsBmi()
    name = DescriptorsName()
    age = DescriptorsAge()
    def __init__(self, name, age, bmi):
        self.name = name
        self.age = age
        self.bmi = bmi

    def __str__(self):
        return "{0} age is {1} and BMi is {2}".format (self.name, self.age, self.bmi)

person1 = Person("JOHN", 25, 26)
print(person1)
person1.age = -1
print(person1)
# def hello():
#     print("Inside hello function")


#     def greet():
#         return "\t Executed Greet function"
#     def print_text():
#         return "\t Executed print_text function"

#     print(greet())
#     print(print_text())
#     print("Outside the hello function")
# hello()



# def hello(name = "KRISHNA"):
#     print("Inside hello function")

#     def greet():
#         return "\t Executed Greet function"

#     def print_text():
#         return "\t Executed print_text function"

#     if name == "KRISHNA":
#         return greet()
#     else:
#         return print_text()
      
#     print("Outside the hello function")
# x = hello()
# print(x)


# def hello():
#     print("Hello world")

# def greet(func):
#     print("Good to learn python")
#     print(func())

# greet(hello)


def new_decorator(func):

    def first():
        print("Before func")

        func()

        print("after func")
    return first

# def generate_new_decorator():
#     print("Hello World")

# generate_new_decorator = new_decorator(generate_new_decorator)

# generate_new_decorator()

@new_decorator
def generate_new_decorator():
    print("Hello World")

generate_new_decorator()



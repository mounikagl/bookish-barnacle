# x = "hello this is global var"

# def local():
#     # x = 10

#     print(f'x value is {x}')

# local()

x = "Krishna"

def local():
    # x = "Kanna"

    def greet():
        # x = "Radha"
        print(f'Hello {x}')
    greet()

local()
# try:
#     add = 5+'5'
# except:
#     print("You aren't entered correct values")

# else:
#     print(add)


# try:
#     f = open("TEXTFILE", 'w') # 'w' is for writting
#     f.write("HELLO PYTHON")

# except IOError:
#     print("Error found: Unable to find file or read data")

# else:
#     print("Content written successfully")
#     f.close()


# try:
#     f = open("TEXTFILE", 'r') # 'r' is for reading
#     f.write("HELLO PYTHON")

# except IOError:
#     print("Error found: Unable to find file or read data")

# else:
#     print("Content written successfully")
#     f.close()

def askint():
    try:
        val = int(input("Please enter an integer: "))
    except:
        print("Looks like you did not enter an integer!")

    finally:
        print("Finally, I executed!")
    print(val)

askint()
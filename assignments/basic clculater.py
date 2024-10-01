def add():
    print("add two numbers")
    x = input ("what would is the first number you want to add?\n> ")
    x = int(x)                                                              #turns x into int
    y = input ("what would is the second number you want to add?\n> ")
    y = int(y)                                                              #turns y into int
    print(str(x) + " + " + str(y) + " = " + str(x + y)) 
add()
def subtract():     
    print("subtract two numbers")
    x = input ("what would is the first number you want to subtract?\n> ")
    x = int(x)                                                              #turns x into int
    y = input ("what would is the second number you want to subtract?\n> ")
    y = int(y)                                                              #turns y into int
    print(str(x) + " - " + str(y) + " = " + str(x - y)) 
subtract()
def multiply():
    print("multiply two numbers")
    x = input ("what would is the first number you want to multiply?\n> ")
    x = int(x)                                                              #turns x into int
    y = input ("what would is the second number you want to multiply?\n> ")
    y = int(y)                                                              #turns y into int
    print(str(x) + " * " + str(y) + " = " + str(x * y)) 
multiply()
def divide():
    print("divide two numbers")
    x = input ("what would is the first number you want to divide?\n> ")
    x = int(x)                                                              #turns x into int
    y = input ("what would is the second number you want to divide?\n> ")
    y = int(y)                                                              #turns y into int
    print(str(x) + " / " + str(y) + " = " + str(x / y)) 
divide()
def exponent():
    print("find an exponent")
    x = input ("what would you like the base to be? \n> ")
    x = int(x)                                                              #turns x into int
    y = input ("what power do you want it to?\n> ")
    y = int(y)                                                              #turns y into int
    print(str(x) + " ^ " + str(y) + " = " + str(x ** y)) 
exponent()
def modulus():
    print("modulus of two numbers")
    x = input ("what would is the first number you want to modulue?\n> ")
    x = int(x)                                                              #turns x into int
    y = input ("what would is the second number you want to divmodule?\n> ")
    y = int(y)                                                              #turns y into int
    print(str(x) + " % " + str(y) + " = " + str(x % y)) 
modulus()
def floor_divide():
    print("floor divide two numbers")
    x = input ("what would is the first number you want to floor divide?\n> ")
    x = int(x)                                                              #turns x into int
    y = input ("what would is the second number you want to floor divide?\n> ")
    y = int(y)                                                              #turns y into int
    print(str(x) + " // " + str(y) + " = " + str(x // y)) 
floor_divide()


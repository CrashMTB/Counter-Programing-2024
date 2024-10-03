#1 (15 points)
#Create a program that uses three input statements to ask the user for three random words, print the concatenation of those three words

#2 (7 points)
#Create a function called add_three that takes three parameters. Outside the function, use three input statements that ask for one integer each. Run add_three using those integers. add_three should print the sum of those integers.

#3 (3 points)
#Create a function called data_three that takes zero parameters. Inside of the function create three input statements that ask for a word, an integer, and a float. Add the integer and the float and then concatenate that sum with the word, then print.


#HOW TO TURN IN!
#Create a folder in your github repo called Tests. Save your file as unit2test.py in that folder and push your changes.


#1
potato = input("give me any random word? \n> ")
you_are_great = input("give me a second random word? \n> ")                                                     #lines 16-19 are the first problem
hello = input("give me a third random word? \n> ")
print("your three random words were " + potato + " " + you_are_great + ", and " + hello + ".")



#2
def add_three(x, y, z):
    print (x + y + z)
    return(x + y + z)

x = input("whats the first number you want to add? \n> ")
x = int(x)
y = input("whats the second number you want to add?\n> ")                               #lines 24-34 are used for the second problem
y = int(y)
z = input("whats the third number you want to add?\n> ")
z = int(z)
add_three(x, y, z)


#3
def data_three():
    word = input("give me any word?\n> ")
    number = int(input("give me any number?\n> "))
    dec = float(input("give me anny float? \n> "))                                      #lines 37-43 are the third problem
    print (str(number + dec) + " " + word)
data_three()
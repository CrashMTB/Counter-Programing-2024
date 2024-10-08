# If statments evaluate boolean expressions
# Make decsions about which code to run next

#take a tempature
#print "<emprature is hot if the tem is >= 80
#other wise, pritn "<temp>is not hot
temperature = int(input("what is the tempature \n> "))
if temperature >= 80:
    print(str(temperature) +  " is hot!") #if false it skips the indented lines but if true it goes inside
else: # if take no condition than run this
    #otherwise....
    print(str(temperature) +  " is cold.")


#complete activit complete [rogram thar asked for program print acsess granted if correct
#pass wor 68.
    
password = input("what is the pass word?\n> ")
if password == "skibidi68":
    print("ACCESS GRANTED")
else:
    print("ACCESS DENIED")


#activity two electric boogaloo
    #creat a five question quiz that prints your score

def quiz():
    x = 0
    quest1 = input("is mister osowski gay?\n> ")
    if quest1 == "no":
        x = x + 1
    quest2 = input("does mister osowski have a boy friend?\n> ")
    if quest2 == "no":
        x = x + 1
    quest3 = input("osowski has beatiful children true or false?\n> ")
    if quest3 == "yes":
       x = x + 1
    quest4 = input("is osowski a good teacher?\n> ")
    if quest4 == "yes":
        x = x + 1
    quest5 = input("did osowski ask us to go to downloadfreeram.com? \n> ")
    if quest5 == "yes":
        x = x + 1
    x = str(x)
    print (x + "/5")
quiz()

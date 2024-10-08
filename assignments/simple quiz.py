def quiz():
    x = 0
    quest1 = input("is mister osowski gay?\n> ")
    if quest1 == "no":
        x = x + 1
    quest2 = input("does mister osowski have a boy friend?\n> ")
    if quest2 == "no":
        x = x + 1
    quest3 = input("osowski has beatiful children, true or false?\n> ")
    if quest3 == "true":
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
#i fixed the questions
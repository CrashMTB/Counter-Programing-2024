quest1 = input("is mister osowski gay?\n> ")
quest2 = input("does mister osowski have a boy friend?\n> ")
quest3 = input("osowski has beatiful children?\n> ")
quest4 = input("is osowski a good teacher?\n> ")
quest5 = input("did osowski ask us to go to downloadfreeram.com? \n> ")
#i fixed the questions
def tally_score():
    x = 0
    if quest1.lower() == "no":
        x = x + 1
    if quest2.lower() == "no":
        x = x + 1
    if quest3.lower() == "yes":
        x = x + 1
    if quest4.lower() == "yes":
        x = x + 1
    if quest5.lower() == "yes":
       x = x + 1
    x = str(x)
    print (x + "/5")
tally_score()
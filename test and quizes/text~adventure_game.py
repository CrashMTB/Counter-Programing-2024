def start(): #this is how i start the program and reset it after an ending
    print("Just 5 seconds ago you were crossing the road when a truck ran you over, as your ability to feel pain and discomfort disapates,and your eyes start to close you here a voice") #start of an advadture
def restart():                         # use this function at the end of a path to see if the user would like to play again
    restart = input("Would you like to restart?\n> ").lower
    if restart == "yes":
        start()
    elif restart == "no":
        print("Good bye")
    else:
        print("Not valid")
        restart()
def second_chance():              #first function
    do_you_live = input("Hello there child. You can have a second chance at life but you will have to help me with a problem. Will you take your second chance? (yes/no) \n> ").lower
    if do_you_live == "yes":
        print("Good i will give you a second chance")
        you_do()
    elif do_you_live == "no":
        you_dont()
    else:
        print("That isnt valid, try again")
        second_chance()
def you_dont():      # 2nd section path 1
    life_death = input("you dont?! why not like are you sure?\n> ").lower
    if life_death == "yes":                        #first ending 
        print("i will not force you to do this but it is a shame")
        print("As you here muffled ambulance noises in the distance. As every fades out your life flashes befor your eyes and you think to your self maybe I should have taken the offer ")
        restart()
    elif life_death == "no":
        print("Thank you child, I promise you, you wont regret it")
        you_do()
    else:
        print("Invalid try again")
        you_dont()
def you_do():               # 2nd section path 2 
    print("Suddenly as your senses come back you start to feel something around you like your rapped in something, you open your eyes to realize your in the arms of a young woman whos looking down at you.")
    print("A man enters a room and says, so thats our baby son. In a moment of relization you dont know what to do")
    baby = input("You are shocked and cant think of what to do so do you 1. do nothing, or 2. cry?\n> ")
    if baby == "1": 
        print("Your new mother starts to rock you back and forth trying to sooth you.")
        sooth()
    elif baby == "2":
        print("As you stare off into nothingness you new father leans down and says i'm sure you will be a fine heir.")
        heir()
    else:
        print("Invalid, try again")
        you_do()
def sooth():                #3rd section path 1
    print("As you are soothed you feel much better")
    to_mother = input("you feel a lot better so will you 1. stop crying, 2, say thankyou, or 3.continue to cry")
    if to_mother == "1":
        print("Thats it dear. ive got you its ok")
        mom_timeskip()
    elif to_mother == 2:
        print("you imedeatly relize your mistake as you are thrown into the forest to die as the thought you were possesed by a demon.")
        print("it seams this place is primitive in there thinking, probably midev")
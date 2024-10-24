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
def second_chance():                                                                                                                     #first section
    do_you_live = input("Hello there child. You can have a second chance at life. Will you take your second chance? (yes/no) \n> ").lower
    if do_you_live == "yes":
        print("Good i will give you a second chance")
        you_do()
    elif do_you_live == "no":
        you_dont()
    else:
        print("That isnt valid, try again")
        second_chance()
def you_dont():                                                          # 2nd section path 1
    life_death = input("you dont?! why not like are you sure?\n> ").lower
    if life_death == "yes":                        #first ending 
        print("i will not force you to do this but it is a shame")
        print("As you here muffled ambulance noises in the distance. As every fades out your life flashes befor your eyes and you think to your self maybe I should have taken the offer ")
        print("really you died already? ending")
        restart()
    elif life_death == "no":
        print("Thank you child, I promise you, you wont regret it")
        you_do()
    else:
        print("Invalid try again")
        you_dont()
def you_do():                                                                                                                                                                                                 # 2nd section path 2 
    print("Suddenly as your senses come back you start to feel something around you like your rapped in something, you open your eyes to realize your in the arms of a young woman whos looking down at you.")
    print("A man enters a room and says, so thats our baby son. In a moment of relization you dont know what to do")
    baby = input("You are shocked and cant think of what to do so do you 1. do nothing, or 2. cry?\n> ")
    if baby == "1": 
        print("Your new mother starts to rock you back and forth trying to sooth you.")
        sooth()
    elif baby == "2":
        print("As you stare off into nothingness you new father leans down and says i'm sure you will be a fine heir.")
        heir_time_skip()
    else:
        print("Invalid, try again")
        you_do()
def sooth():                                        #3rd section path 1
    print("As you are soothed you feel much better")
    to_mother = input("you feel a lot better so will you 1. stop crying, 2, say thank you, or 3.continue to cry")
    if to_mother == "1":
        print("Thats it dear. ive got you its ok")
        mom_timeskip()
    elif to_mother == "2":                                                                                                              #ending 2
        print("you imedeatly relize your mistake as you are thrown into the forest to die as the thought you were possesed by a demon.")
        print("it seams this place is primitive in there thinking, probably midieval,")
        print("Demon? ending")
        restart()
    elif to_mother == "3":
        print("Thats it dear. ive got you its ok")
        mom_timeskip()
    else:
        print("invalid please try again")
        sooth()
def heir_time_skip():                                                                                                                                          #3rd section path 2
    print("16 years has passed yove learned some things about this new world you live in, the important stuff being the world you are in is called Maregorum.")
    print("The second thing thats important to know is that you are the son to the king of the kingdom of rampart.")
    print("Your father has been preparing you to eventually take over his crown so hes putting you in charge of a small poor region of the land to prepare.")
    your_town=input("How would you like to devolpe the land?\n 1. Agriculture,\n 2. Military\n 3. Economically \n> ").lower
    if your_town == "1" or "agriculture":                                             #ending 3
        print("Over the next few years the town has became a staple in the kingdom.")
        print("Because of your succses your father has declaired you king.")
        print("I Am The King! ending")
        restart()
    elif your_town == "2" or "military":
        print("Your ability to make this a military town is invane because of the famined people and lack of buget but you still persist with an inflated ego.")
        military()
    elif your_town == "3" or "economically":
        print("Thats all well and good but what is gonna be your method of doing that.")
        econ()
    else:
        print("invalid please try again")
        heir_time_skip()
def mom_timeskip():                                                                                                                                            #section 4 path 1
    print("16 years has passed yove learned some things about this new world you live in, the important stuff being the world you are in is called Maregorum.")
    print("The second thing thats important to know is that you are the son to the king of the kingdom of rampart.")
    print("Your father has been preparing you to eventually take over his crown so hes putting you in charge of a small poor region of the land to prepare.")
    print("But you refused you decided to go and help thos who need it. ")
    helping= input("Would you like to do that by 1. opening a free clinic or 2. starting a charity?\n> ")
    if helping== "1":
        print("You opened a free clinic to help soldiers people and adventures people of all races and speicies. How ever this gets alot of attention from the healers guild.")
        print("The Healers guild is a corupt organazation who's greed leaves many as in debt or even enslaved.")
        guild()
    elif helping == "2":                                                       # ENDING 4
        print("This last for years you become known as the saint of rampart.")
        print("However sadly your life doesnt develope much and for the rest of your life you were nothing but a saint to everyone.")
        print("The Saint. ending")
        restart()
    else:
        print("invalid response, try again ")
        mom_timeskip()
def military(): #section 4 path 2
    treason_war = input("Filled with greed and ego you know you must do something big to spread your name across Maregorum. Will you 1.go to war with neighboring nations or 2. throw over you father.")
    if treason_war == "2":
        print("you and your smalled army try to take over the crown from your father however it was far from sufficent. Your army got wiped out and your father threw you in a dungeon.")
        dungeon()
    elif treason_war == "1":
        print("you atempt a raid on the strongest kingdom, how ever your soldiers are famined and your training was sparce and inneficient leading to the defeat of your soldiers")
        print("Death of a Tyrant. ending")               #ending 5
        restart()
    else:
        print("invalid response, try again ")
        military()
def econ():                     #section 4 path 3
    econ = input("you have a few options would you like to go for\n1. the arts\n2. mining")
    if econ == "1":                                                 #ending  6
        print("it took a while but the arts are now booming your known as the town of fredom and expresion the oposite of your opressive neighbors and man people across Maregorum are coming to live in your town")
        print("The town of Freedom. ending")
        restart()
    elif econ == "2":
        mine()
    else:
        print("invalid response, try again ")
        econ()
def mine():                      #section 5 path 1
        mine = input("you notice there are caverns and ravine which would you like to focus your mining in").lower
        if mine == "cavern" or "caverns":
            cave()
        elif mine == "ravine":
            ravine()
        else: print("invalid response, try again ")
def guild():                     #section 5 path 2
    healers_guild  = input("You know this is a problem. would you like to deal with it by \nA. Either running them out of buisnes.  \nB. Have your father mandate a new law capping prices on clinics.").lower
    if healers_guild == "a":
        print("Try as you might your a small clinic with not much creditability in the public view, you seem to be un able to do anything to these unhanded buisnesses. ")
        print("Useless. ending")
    elif healers_guild == "b":
        print("your father agreed. after that the prcies dropped and people debts and sentences to servantude  were gretly diminished ")s
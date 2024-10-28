def start():                     #this is how i start the program and reset it after an ending
    print("Just 5 seconds ago you were crossing the road when a truck ran you over, as your ability to feel pain and discomfort disapates,and your eyes start to close you here a voice") #start of an advadture
    second_chance()
def restart():                   # use this function at the end of a path to see if the user would like to play again
    restar = input("Would you like to restart?\n1. yes\n2. no\n> ").lower
    if restar == "1":
        start()
    elif restar== "2":
        print("Good bye")
    else:
        print("Not valid")
        restart()
def second_chance():             #section 1
    do_you_live = input("Hello there child. You can have a second chance at life. Will you take your second chance? \n1. yes\n2. no \n>")
    if do_you_live == "1":
        print("Good i will give you a second chance")
        you_do()
    elif do_you_live == "2":
        you_dont()
    else:
        print("That isnt valid, try again")
        second_chance()
def you_dont():                  #section 1 path 1             ending 1
    life_death = input("you dont?! why not like are you sure?\n1. yes\n2.no\n>  ").lower
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
def you_do():                    #section 2 path 2 
    print("Suddenly as your senses come back you start to feel something around you like your wrapped in something, you open your eyes to realize your in the arms of a young woman whos looking down at you.")
    print("A man enters a room and says, so thats our baby son. In a moment of relization you dont know what to do")
    baby = input("You are shocked and cant think of what to do so do you. \n1. Do nothing. \n2. Cry.\n> ")
    if baby == "2": 
        print("Your new mother starts to rock you back and forth trying to sooth you.")
        sooth()
    elif baby == "1":
        print("As you stare off into nothingness you new father leans down and says i'm sure you will be a fine heir.")
        heir_time_skip()
    else:
        print("Invalid, try again")
        you_do()
def sooth():                     #section 3 path 1             ending 2
    print("As you are soothed you feel much better")
    to_mother = input("you feel a lot better so will you.\n1. Stop crying. \n2. Say thank you.  \n3.Continue to cry\n>")
    if to_mother == "1":
        print("Thats it dear. ive got you its ok")
        mom_timeskip()
    elif to_mother == "2":                                                                                                              #ending 2
        print("you immeadetyl relize your mistake as you are thrown into the forest to die as the thought you were possesed by a demon.")
        print("it seams this place is primitive in there thinking, probably medieval,")
        print("Demon? ending")
        restart()
    elif to_mother == "3":
        print("Thats it dear. ive got you its ok")
        mom_timeskip()
    else:
        print("invalid please try again")
        sooth()
def heir_time_skip():            #section 3 path 2             ending 3
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
def mom_timeskip():              #section 4 path 1             ending 4
    print("16 years has passed yove learned some things about this new world you live in, the important stuff being the world you are in is called Maregorum.")
    print("The second thing thats important to know is that you are the son to the king of the kingdom of rampart.")
    print("Your father has been preparing you to eventually take over his crown so hes putting you in charge of a small poor region of the land to prepare.")
    print("But you refused you decided to go and help thos who need it. ")
    helping= input("Would you like to do that by \n1. Opening a free clinic \n2. Starting a charity.\n> ")
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
def military():                  #section 4 path 2             ending 5
    treason_war = input("Filled with greed and ego you know you must do something big to spread your name across Maregorum so will you \n1.Go to war with neighboring nations.  \n2. Throw over you father.\n> ")
    if treason_war == "2":
        print("You and your smalled army try to take over the crown from your father however it was far from sufficent. Your army got wiped out and your father threw you in a dungeon.")
        dungeon()
    elif treason_war == "1":
        print("You atempt a raid on the strongest kingdom, how ever your soldiers are famined and your training was sparce and inneficient leading to the defeat of your soldiers")
        print("Death of a Tyrant. ending")               #ending 5
        restart()
    else:
        print("invalid response, try again ")
        military()
def econ():                      #section 4 path 3             ending 6
    econ = input("You have a few options would you like to go for\n1. The arts\n2. Mining\n> ")
    if econ == "1":                                                 #ending  6
        print("It took a while but the arts are now booming your known as the town of fredom and expresion the oposite of your opressive neighbors and man people across Maregorum are coming to live in your town.")
        print("The town of Freedom. ending")
        restart()
    elif econ == "2":
        mine()
    else:
        print("invalid response, try again ")
        econ()
def mine():                      #section 5 path 1
        mine = input("You notice there are caverns and ravine which would you like to focus your mining in the\n1. Caverns. \n2. Ravine.\n> ").lower
        if mine == "1":
            cave()
        elif mine == "2":
            ravine()
        else:
            print("invalid response, try again ")
            mine()
def guild():                     #section 5 path 2             ending 7
    healers_guild  = input("You know this is a problem. would you like to deal with it by \n1. Either running them out of buisnes.  \n2. Have your father mandate a new law capping prices on clinics.\n> ").lower
    if healers_guild == "1":
        print("Try as you might your a small clinic with not much creditability in the public view, you seem to be un able to do anything to these unhanded buisnesses. ")
        print("Useless. ending")                               #ending 7
        restart()
    elif healers_guild == "2":
        print("Your father agreed. after that the prcies dropped and people debts and sentences to servantude  were gretly diminished.")
        print("The people hailed you as a hero, now that youve accomplished that the members of the healers guild has it out for you.")
        revenge()
    else:
        print("invalid response, try again ")
        guild()
def dungeon():                   #section 5 path 3
    trapped = input("Now that your in the dungeon you have 3 options\n1. Give up, and accept your fate\n2. Plead with your father to let you go\n3. Break out \n> ")
    if trapped == "1":
        accept()
    elif trapped == "2":
        plead()
    elif trapped == "3":
        break_out()
    else:
        print("invalid response, try again ")
        guild()
def cave():                      #section 6 path 1
    print("You send the people of your town into the caves much to your delight its rich in adamantite, and mythril wich is actualy quite easy to get.")
    print("Because of the rarity of this metal you can sell it for a lot whith the economical boom this created you can now choose to paths.")
    selling = input ("Would you like to\n1. Sell to the kingdom of Rampart only\n2. Sell to the whole of Maregorum\n> ")
    if selling== "1":
        kingdom_expansion()
    elif selling== "2":
        buisness_man()
    else:
        print("invalid response, try again ")
        cave()
def ravine():                    #section 6 path 2
    print("You send people to the ravine its very dangerous there many people died just exploring it but there was a silver lining, unobtainium, and mana cyrstals.")
    print("Unobtainium is the most valuable resource in Maregorum. It can be used in magic riturals of the highest degree and outputs the purest form of mana known as either.")
    print("Mana crystals are used in everything from wizard wands to lights.")
    mage = input("your left with an important choice either  \n1.Switch your towns focus to mage training.\n2.Sell the mined ore.\n> ").lower
    if mage == "1":
        magic()
    elif mage == "2":
        riches()
    else:
        print("invalid response, try again ")
        mine()
def revenge():                   #section 6 path 3             ending 8 & 9
    print("With the healers guild now after you you have three choise.")
    print("1. Fightback\n2. Run and hide\n3. ignore\n>")
    guild_preasure = input("> ")
    if guild_preasure == "1":
        print("They send assasins after you and sadly you parished do to a knife to your throat.")
        print("Assasinated! ending")         #ending 8
        restart()
    elif guild_preasure == "2":
        print("After running and hiding for days strait but you know you may never return.")
        print("The Lost Traveler. ending")  #ending 9
    elif guild_preasure == "3":
        print("Ignoring there threats only makes them angier so you decide to shut them up once and for all.")
        guild_destruction()
    else:
        print("invalid response, try again ")
        revenge()
def accept():                    #section 6 path 4             ending 10
    print("You decided that it wasnt worth the fight to get out and you never did get out you ended up dying of old age in there.")
    print("Dungeon. ending")      #ending 10
    restart()
def plead():                     #section 6 path 5             ending 11
    print("As you plead with your father to forgive you know relise that he wont listen and instead of letting you rot he decide's to execute you.")
    print("The Unforgiven. ending")
    restart()
def break_out():                 #section 6 path 6
    print("Driven with ego and ambition you know you cant just sit and wait so as you notice the metal bars for your windows you realize that there rusty.")
    how = input("How are you going to escape?\n1. Wait for your lunches and use the oranges to further corode it. \n2. Bash into the bars as hard as you can.\n> ")
    if how == "1":
        orange()
    elif how == "2":
        bash()
    else:
        print("invalid response, try again ")
        break_out()
def kingdom_expansion():         #section 7 path 1             ending 12
    print("As you sell the ore to the rest of Rampart, your town gets richer and richer and the kingdom uses the ore to make weapons, armor, and even boats.")
    print("Over time your town is the reason why Rampart became the strongest kingdom in Maregroum.")
    print("The Miner. ending")
    restart()
def buisness_man():              #section 7 path 2             ending 13
    print("You begin to sell to the whole of Maregorum, You quickly become the richest man in the world and a majot part of the function of all kingdoms in Margorum")
    print("buisness man ending")
    restart()
def magic():                     #section 7 path 3             ending 14
    print("Altho this magic stuff is new to you, you have faith it will work. You use the remaining budget to build the school and higher high class mages.")
    print ("because of the major amounts of mana in the air, your schools were very efective causing the military might of Rampart to sky rocket and at the.\nSame time it brough many scholars to the area causing many technological advancments to Rampart as well")
    print("The Man of Knowledge. ending")
    restart()
def riches():                    #section 7 path 4             ending 15
    print("Even though you were able to mine it and get a buyer you made a massive mistake. You didnt get an escort for the goods, so a group of bandits stole all the ore.")
    print("Not The Bandits. ending")
    restart()
def guild_destruction():         #section 7 path 5
    print("You know that you need to use violence so what would you like to do.")
    destroy = input("1. Would you like to blow up there buildings?\n2. Would you like to hire assasins to kill the guild members?\n> ")
    if destroy == "1":
        terrorist()
    elif destroy == "2":
        assasins()
    else:
        print("invalid response, try again ")
        guild_destruction()
def orange():                    #section 8 path 1             ending 16
    print("To your surprise it actually works.")
    print("After a few month it wore down enough to allow you to easilt break the bars and escape")
    print("Convict. ending")
    restart()
def bash():                      #section 8 path 2             ending 17
    print("You bash against the bars again and again but they arent coroded enough to break. This makes alot of noise and alerts the guards.")
    print("When they see you tring to escapeso they cain you up unable to move.")
    print("The Bound. ending")
    restart()
def terrorist():                 #section 8 path 3             ending 18
    print("You know there will be lots of casualties bu you feel you have to so after a long year of placing secret bombs at the guild locations you detonate all of the bombs.")
    print("It was succsesfull however, you were classified as a terrorits.")
    print("The Terrorist! ending")
    restart()
def assasins():                  #section 8 path 4             ending 19
    print("The assasins you hire were secretly alredy working for the guild and they cut open your guts.")
    print("The Betrayal. ending")
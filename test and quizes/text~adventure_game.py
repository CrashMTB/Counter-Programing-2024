print("just 5 seconds ago you were crossing the road when a truck ran you over, as your ability to feel pain and discomfort disapates,and your eyes start to close you here a voice") #start of an advadture
def second_chance():              #first function
    do_you_live = input("hello there child. you can have a second chance at life but you will have to help me with a problem. will you take your second chance? (yes/no) \n> ").lower
    if do_you_live == "yes":
        print("Good i will give you a second chance")
    elif do_you_live == "no":
        you_dont()
    else:
        print("that isnt valid, try again")
        second_chance()

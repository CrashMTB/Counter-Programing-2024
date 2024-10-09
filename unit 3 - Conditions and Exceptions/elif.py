x = 5

if x > 0: #  > < == <= >= !=
    print("x is postive")

elif x == 0: # elif statements is always paried to an if
    print("x is 0")

else:       # awlays connected to if
            # else statments never takes a condition
    print("x is a negative number")


collor = input("what collor is the of the light?\n> ").lower

if collor() == "green":                         # Only one if statment
    print("go")
elif collor() == "red":                         # can be any amount of elif statement
    print("stop!!!")
elif collor() == "yellow":
    print("Stop if you can safley")
else:                                           # Only one statement
    print("get your eyes checked man")



x = 10

if x > 5:
    print ("x is greater than 5")
if x > 8:                                    # it will print both because they are seprate functions
    print ("x is greater than 5")

###########################################
    
x = 10

if x > 5:
    print ("x is greater than 5")
elif x > 8:                                 # because the elif is connected it will only do one of the prints
    print ("x is greater than 5")



def weather():
    temp = int(input("what is the tempature outside today?\n> "))
    temp = int(temp)
    if (temp > 80):
        print("the sun is cooking you alive!!!")
    elif (temp > 70):
        print("its beutiful outside")
    else: 
        print("have some coco its a bit cold out, sit by the fire, and watch a movie")
weather()
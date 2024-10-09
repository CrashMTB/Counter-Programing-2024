x = int(input("what is the wind speed in MPH?\n> "))
if x < 0:
    print("dude not a negative like come on man.")
elif  x < 74:
    print(" It is a Tropical storm.")
elif x < 96:
    print(" It is a Category 1 huricane.")
elif x < 111:
    print(" It is a Category 2 huricane.")
elif x < 130:
    print(" It is a Category 3 huricane.")
elif x < 157:
    print(" It is a Category 4 huricane.")
elif x >= 157:
    print(" It is a Category 5 huricane.")
else: 
    print("Be for real, and Dont waste my precious time.")
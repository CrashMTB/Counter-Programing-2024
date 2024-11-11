import random
x = random.randint(1,101)
guess = ""
y = 0
while guess != str(x):
    try:
        guess = input("guess the number\n>  ")
    except:
        print("thats not right")

    if guess == str(x):
        print("you got it.")
    elif guess < str(x):
        y += 1
        print ("Too low guess again.")
    elif guess > str(x):
        y += 1
        print ("Too high guess again.")
    else:
        print("invalid try again")
print ("You got it in " + str(y) + " Attempts")
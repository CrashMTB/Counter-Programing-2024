#allows you to change hor the loop operate
#like, quit early, skip curent loop , nothing
#break, continue, and pass


# break
# exits a loop before it was supposed to happen

# Example

fruit_bag = ["appple", "orange", "bug", "pear", "strawberry"]

for fruit in fruit_bag:

    if fruit== "bug":
        print("Uh oh a bug stop eating!")
        break
    else:
        print("you ate a " + fruit)


# continue
# skips the current loop
# it doesnt end the loop just moves on
        
#example
        
orders= [115, 30, 35, 23, 100,3 ,10, 22]

#onlt discount 20+ dolars

for i in orders:
    if i < 20:
        continue #skips the rest of the loop it and goes to the next
    print("$" + str(i) + " order discount 5% to $" + str(i * 0.95))

# pass
# pass does nothing
# used as a place holder while writing code
    
if True:
    pass

def soe():
    pass

def ddd():
    pass
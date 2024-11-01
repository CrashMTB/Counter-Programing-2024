#For loops
#BIG deal
#allows programer to repeat or "loop"

#Write a programthat prints the numbers one through ten
# for <temp var> in <List>:
for i in range(0,10):
    print(i)


#goes throgh the function until all list items have been used 


#range(0-10) = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]


#It takes a list and goes one through one through all numbers on the list 
    
# i is the index it will start at 0 and will stop when hits 10
    
#similar to a if else statment
    
#i is a temperary varible
    


top_food = ["fried chicke","egg","mac n cheese"]
for food in top_food:
#go through every food in to food
#reapeats everything in the loop for every item in the loop
#food equals current item its going through
    print(food)





#Creat a list  of groceries - 
#contains mi, eggs, breadlk, butter, apples

#Ask for input on an item they purchase they purchased
    
#if the item was on the list print ("<item> crossed off tghe list and remove that iten")
#use a forloop to search
#if statment to check the list
    
grocieries = ["milk", "eggs", "bread", "butter", "apples"]
item = input("what did you buy?\n> ").lower()
for i in grocieries:
    if i == item:
        print(item + " was checked off the list")
        grocieries.remove(item)
        print(grocieries)
        break
    else:
        print()







        # Create a list of groceries
grocieries = ["milk", "eggs", "bread", "butter", "apples"]

# Ask for input on an item they purchased
item = input("What did you buy?\n> ").lower()  # Use parentheses to call the lower() method

# Use a for loop to search
for i in grocieries:
    if i == item:
        print(item + " was checked off the list.")
        grocieries.remove(item)  # Remove the item from the list
        print("Updated grocery list:", grocieries)
        break  # Exit the loop after removing the item
else:
    print(item + " is not on the grocery list.")  # Inform if the item is not found



#creat a list of a five random numbers from 0-100
#then use a for loop to find the some of those nubers
    
import random
sum = 0
numbers = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
for i in numbers:
    sum = sum + i
print(sum)
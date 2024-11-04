




#import rand
import random


#make rand nums
a=[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)] 

def bubble():         
    steps = 0 #to find # of steps 

    print("unsorted list: ",a)    #

    for n in range(len(a) - 1, 0, -1):
        # Inner loop to compare adjacent elements
         for i in range(n):
                #check if they need swap
            if a[i] > a[i + 1]:
                # Swap elements if they are in the wrong order
                a[i], a[i + 1] = a[i + 1], a[i]


                print (str(a) + " swapped")
                #add a step
                steps +=1
            else:
                print(str(a) + " not swapped")


    print("sotred list :", a)
    print("used " + str(steps) + " steps.")
bubble()
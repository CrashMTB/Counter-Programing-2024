




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

#array -  a special variable, which can hold more than one value at a time
#while - used to repeatedly execute the indented block of code as long as the True-False condition following the word 'while' evaluates to True.
#

def parting(array, low, high):
  
    # First Element as pivot
    pivot = array[low]
    
    # st points to the starting of array
    y = low + 1
    
    # end points to the ending of the array
    z = high

    while True:
        while y <= z and array[z] >= pivot:
            z = z - 1

        while y <= z and array[y] <= pivot:
            y = y + 1

        if y <= z:
            array[y], array[z] = array[z], array[y]
        else:
            break

    array[low], array[z] = array[z], array[low]
    return z

# The main function that implements QuickSort
# b[] --> Array to be sorted,
# low --> Starting index,
# high --> Ending index
def quick_sort(array, start, end):

    # If low is lesser than high
    if start < end:
      
        # idx is index of pivot element which is at its
        # sorted position
        idx = parting(array, start, end)
        
        # Separately sort elements before
        # partition and after partition
        quick_sort(array, start, idx-1)
        quick_sort(array, idx+1, end)

# Function to print an array
def print_a(a, n):
    for i in range(n):
        print(a[i], end=" ")
    print()

# Driver Code
b =[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)] 

quick_sort(b, 0, len(b)-1)
print_a(b, len(b))



def quicksort(arr):
    if len(arr) <= 1:
        return arr
    else:
        pivot = arr[0]
        less_than_pivot = [x for x in arr[1:] if x <= pivot]
        greater_than_pivot = [x for x in arr[1:] if x > pivot]
        return quicksort(less_than_pivot) + [pivot] + quicksort(greater_than_pivot)
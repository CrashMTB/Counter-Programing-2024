#. Start at the beginning of the list.
   # 2. Compare the first two elements. If the first element is greater than the second, swap them.
    #3. Move to the next pair of elements and repeat the comparison and swap process until the end of the list is reached.
    #4. Repeat steps 1-3 until no swaps are needed, indicating that the list is sorted.
    
#**Example**:
#	Imagine sorting a deck of cards by comparing adjacent cards and swapping them if they are out of order. Repeat this process until the deck is sorted from lowest to highest card
import random
bubble=[random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)] 
print("Original List:", bubble)

# sorting list using nested loops
for i in range(0, len(bubble)):
    for j in range(i+1, len(bubble)):
        #swap if nessesary
        if bubble[i] >= bubble[j]:
            bubble[i], bubble[j] = bubble[j],bubble[i] 
            print (str(bubble) + " swapped")
        else:
            print(str(bubble)  + " not swapped")
print("Sorted List", bubble)
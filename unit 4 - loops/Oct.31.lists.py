#4 colection types
#tuple
#Set
#list
#dictionary

#today is list focused
#a list is a way to store more than one calue in a single varible
#those values in the lists are called items
#items can be accsessed bythere index(which is there position in the list)

#use [] not()
#INDEx                          0                    1                 2             3              4
best_elden_ring_weapons = ["Blasphemous Blade", "Moonveil", "Rivers of blood", "Iron Ball", "Bloodhounds's Fang"]

# INDEX         0     1     2     3
best_years = [1776, 1985, 1994, 1957]


print(best_years.index(1985))
#[] = at index
#print best
print (best_elden_ring_weapons[0])

#print worst of the best
#print (best_elden_ring_weapons[len(best_elden_ring_weapons)]) list index out of range so -1
print (best_elden_ring_weapons[len(best_elden_ring_weapons)-1])

#LIST items can be changed
best_elden_ring_weapons[3] = "club"
print(best_elden_ring_weapons)

#remove last item in list
best_elden_ring_weapons.pop(4)
print(best_elden_ring_weapons)
#remove the removes an item by its index

#.remove remove on value
best_elden_ring_weapons.remove("Moonveil")
print(best_elden_ring_weapons)

best_elden_ring_weapons.append("mommmommommmommommmommmommmommm")
print(best_elden_ring_weapons)

import random
numbers = [random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100),random.randint(1,100)]
print(numbers)
print(max(numbers))
print(min(numbers))
numbers.sort()
print(numbers)




#strings- are lists
#string are lists om chartecter
word = "potato"
print(word[0])

# a dictionary is a type of collection like a list
# A list is a collection of items in a sequence
# A Dictionary is different
# Dictionaries store data in Key-value pairs
# you can retrieve data quickly with an unique key
# instead of retrieving it by index

#example

Crash = {
    "name": "Crash",
    "age": 3,
    "CITY": "St. Micheal",
    "pets": 1,
    "height": 5.10
}
# each key must be unique
print(Crash["age"])

# .get allows you to retrieve a value without erroring
# When key doesnt exsist
#the second paramater is what happens if it is ot found
print(Crash.get("height"))
print(Crash.get("Slaves", "Not Found"))

# you can add values

Crash["country"]  = "USA"

# you can modify values

Crash ["age"] = 4
print(Crash)

# Remove entries

Crash.pop("pets")

#Itterate through a dictionary using for loop

for key, value in Crash.items():
    print(key + ": " + str(value))

#dictionary functions
print(Crash.keys())          #returns all keys
print(Crash.values())        #returns all values
print(Crash.items())         #returns all pairs
print(Crash.clear())         #removes all from dictionary

#once apon a time an (crearure0) named (name1) 
#this (creature0) lived in a (object)
#then one day a (adjective) and (adjective 2) (creature1) destoryed (city)
#but the (adjective3) (creature0) named (name1) saved the city
#and all the other (creature0)s in (city) cheered with (emotion) 
#at the end of the the day (name1) partied with (celeberty) all night long the end
creature0 = input("Name a random creature/animal?\n> ")                   # lines 7-16 are user input codes to find the answers for the madlib awnsers
name1 = input("Enter a name for the main charecter?\n> ")
object = input("Give me any object?\n> ")
adjective = input("Give me a random adjective? \n> ")
adjective2 = input("Give me a new random adjective? \n> ")
creature1 = input("Give me a mythical creature?\n> ")
city = input("What is the name of a city?\n> ")
adjective3 = input("Give me a new random adjective? \n> ")
emotion = input("Name any stong emotion?\n> ")
celeberty = input("Name any celeberty?\n> ")
print("Once apon a time there was a " + creature0 +" named " + name1 + ", and " + name1 + " lived in a " + object + ". Then one day a " + adjective + " and " + adjective2 + " " + creature1 + " destroyed " + city + ".\nBut the " + adjective3 + " " + creature0 + " named " + name1 + " saved " + city + ", and all the other " + creature0+ "'s in " + city + " cheered with " + emotion + ". \nAt the end of the the day, " + name1 + " partied with " + celeberty + " all night long.\nTHE END")
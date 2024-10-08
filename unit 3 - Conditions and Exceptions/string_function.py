#string functions
#they are a group of like- functions that manipulate strings
#they modify strings
#SUPER easy to sue
#PYTHON WOULD BE NOT FUN WITH OUT THEM

#    .lower()
# converts strings to all lowercase
#no matter what the input casing is it goes into lower case and the answer is lowercase
input_answer = "lord of the rings"
#input_answer = "lord of the rings".lower()   also works
input_answer = input_answer.lower()
real_answer = "lord of the rings"
print(input_answer == real_answer)


#   .uper()
# Converts a string to uppercase
input_answer = "lord of the rings"
#input_answer = "lord of the rings".lower()   also works
input_answer = input_answer.upper()
real_answer = "LORD OF THE RINGS"
print(input_answer == real_answer)

# .capitalize
# coverts the first letter two upper case and the rest to lowercase
y = "DJE sji WI".capatilize()
print(y) # Dje sji wi

#the beging leter of all words is upper case
y = "DJE sji WI".title()
print(y) # Dje Sji Wi

#switches the upper and lower case
y = "DJE sji WI".swapcase ()
print(y) # dje SJI wi


#2 functions
print("hello, world")    # hello world is the peramiter
input("please enter user name\n> ")     #\n is an escape charecter and 
#\n starts a new line
#input is never required, unless asked for


#variables
#syntax-grammar, name = <value>
x = 5

#snake namine covenction -all lowercase, underscore spaces
#Concise: short discriptive

username = "CrashMTB"               #define string
Fav_animal = "potato"               #define string
yyyyyyyy = 12                 #define int
percent_complete = 2.32             #define float
yes = True                          #define boolian:upercase
yum = 'd'                           #define charecter (single symobl)

yyyyyyyy = 8                 #reassign - changing exsisting functions

#math operaters
# + - * / ** % //
print(4 + 4)                #> 8
print("4" + '4')            #> 44
print("cat" + "dog")        #>catdog
print("cat" * 3)            #catcatcat
print("cat" + 3)            #error

#working programs
#add using inputs 
x = input("whats X?\n> ") #input always gives a string
x = int(x)                #converts to int
y = int(input("whats y?\n> ")) #combinds the two into one
print(x + y)

#2. converts cellcius to fareheight
temp_celcius = 40
temp_fareneight  = (temp_celcius * 1.8) + 32
print(temp_fareneight + "f")

#2 using inputs 
temp_celcius = int(input("what is the temp in celcius?\n> "))
temp_fareneight  = (temp_celcius * 1.8) + 32
print( "it is " + temp_fareneight + " degrees farenheight")

#conversion function
str()
int()
float()
bin()
bool()

#the parenthes house peramiters
#paramiters what hte function need to run i say jump you sat how hi


#functions
#functions are like varibles
#they have names  
#can be recalled from memmory
#they store information
#varibles store data functions store code
def potato():               #def keyword + name + () + :
    print("potato")         #all indendent line underneath are part of the function till the streak of indents are broken
#functions are not ranr they are defined
#must call name to run
potato()        # every function call needs ()
                # even with no peramiters

def jump(how_high):
    print("you jumpped " + str(how_high) + " inches!")

jump(14)

def make_a_word(a, b, c, d, e, f ,g ,h ,j , k):
    print(a+b+c+d+e+f+g+h+j+k)
make_a_word("p", "o", "t", "a", "t", "o", "w", "e" ,"e" ,"e")

def top_games():
    print("1. blackops II")
    print("2. halo 3")
    print("3. smash")
    print("4. darksouls")
    print("5. terraria")
    print("6. minecraft")
    print("7. diablo 3")
    print("8. wow")
    print("9. breath of the wild")
    print("10. mario 64")

#scope: global and local varibles
#scope refereseto the context in which the varible was defined
#Global-defined at no intedation level
#local- defined in a function
    
#global varibels can be used any anywhere
todd = "COOL GUY"           #global varible no indentaion level

def functio():
    smith = "not acool guy"  #Local- defined in funtion
    todd = "strange guy"     #local varibele in the fuction but only in the function
    print(todd)              #when calling  varible in a function it searches localy first
print(todd) #calls globally even tho the function has one ad well


#if you wanna reassign a global veriable inside of a function 
def function():
    global todd                                 #when todd gets called noe it defaults to global not local
    todd = "alright alright alright"            #this now reassings the global varieable


#return functions can also returnvalues
    #the value that was returned is sent back to where the varible was called
    #similar to a vairable
    #tehfunction does its work and returns

def add2(x, y):
    return x + y
answer = add2(2,10)          #does not print 
print(answer)
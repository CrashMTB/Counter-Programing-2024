# while loops - loop an uncertain # of times
#while loops- loop on condition

real = "Crash"
enter = " "
x = 0
while real != enter:                        #chesck if entered = real
    enter = input("Input Password\n> ")     

    #check if password correct 
    if enter == real:
        print("ACCESS GRANTED")
    else:
        print("ACCESS DENIED\n TRY AGAIN")
        x += 1
        print ("you have tried " + str(x) + " times.")

#end passwoed check
print("welcome")



# with while loops - be carful for infinite loops
# when you put computer in rest it has night mares about infnite loops
#y=0
#while True:
#    y  +=1
#    print ("uh oh")
#    print (str(y))
#    will be grayed out if no end
#    print(all done)



#type "exit" to quit

user_input = ""
while user_input != "exit":
    user_input= input("Enter something(typr 'exit' to quit)")
    print ("You entered: " + user_input)

print("All done")
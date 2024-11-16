#Exercise 9 - Hello

#Prints the hello function
def Hello(name):
    print("Hello,", name)

#Calls the hello function
def Main():
    Hello(name)

#Take User input
name = input("Enter Name: ") 

#Check condition
if name == "Josh Aaron":
    Main()
else:
    print("Unregistered Name.")
#Exercise 9 - Hello

#Prints the hello function
def Hello(x):
    print("Hello,", x)

#Calls the hello function
def Main():
    name = input("Enter your Name: ")
    Hello(name)

if __name__ == '__main__':
    Main()
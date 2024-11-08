#Exercise 6 - Brute Force attack

#user must input the password
password = input("Enter your Password to close the program: ")

#define the correct password
correct_password = "123456"

#define attempts
attempts = 4

#check the password if it's correct
while correct_password != password:
    print("Wrong Password!", str(attempts), "attempts left." )
    attempts = attempts - 1
    password = input("Enter your Password: ")
    
    #if five failed attempts have been entered, the computer exits the loop.
    if attempts == 0:
        break

#if the user enters the correct password
else:
    print("Correct Password!")

#block of code to be executed after five failed attempts
if attempts == 0:
    print("Authorities have been alerted.")
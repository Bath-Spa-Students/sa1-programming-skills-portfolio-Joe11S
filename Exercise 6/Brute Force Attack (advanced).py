#Exercise 6 - Brute Force attack

#user must input the password
password = input("Enter your Password to close the program: ")

#define the correct password
correct_password = "123456"

#define attempts
attempts = 4

#check the password if it's correct
while correct_password != password:

    #break this loop if there are no attempts left.
    if attempts == 0:
        print("Authorities have been alerted.")
        break

    #if there are more attempts, repeat this loop until the above code breaks the loop.
    print("Wrong Password!", str(attempts), "attempts left." )
    password = input("Enter your Password: ")
    
    #as long as least one attempt is left, the loop will decrement one attempt.
    attempts = attempts - 1

#if the user enters the correct password
else:
    print("Correct Password!")
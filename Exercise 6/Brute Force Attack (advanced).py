#Exercise 6 - Brute Force attack

#define the correct password
correct_password = "12345"

#define attempts
attempts = 5

#check the password if it's correct
while attempts > 0:

    #if there are more attempts, repeat this loop until the attempts reach 0.
    password = input("Enter your Password: ")

    #if the correct password is entered, exit the loop.
    if password == correct_password:
        print("Correct Password!")
        break
    
    #if the wrong password is entered, keep decrementing attempts.
    else:
        attempts = attempts - 1
        if attempts > 0:
            
            #extra pluralization block
            if attempts > 1:
                print("Wrong Password!", str(attempts), "attempts left." )
            else:
                print("Wrong Password!", str(attempts), "attempt left." )

#alert authorities once attempts reach 0.
else:
    print("Authorities have been alerted.")
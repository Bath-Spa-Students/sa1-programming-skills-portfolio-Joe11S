#Exercise 6 - Brute Force attack

#user must input the password
password = input("Enter your Password: ")

#define the correct password
correct_password = "12345"

#check the password if it's correct
while correct_password != password:
    print("Wrong Password!")
    password = input("Enter your Password: ")

#if the user enters the correct password
else:
    print("Correct Password!")
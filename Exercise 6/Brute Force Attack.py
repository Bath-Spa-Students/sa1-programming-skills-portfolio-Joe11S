#Exercise 6 - Brute Force attack

#user must input the password
password = input("Enter your Password to close the program: ")

#define the correct password
correct_password = "123456"

#check the password if it's correct
while correct_password != password:
    print("Wrong Password!")
    password = input("Enter your Password: ")
else:
    print("Correct Password!")
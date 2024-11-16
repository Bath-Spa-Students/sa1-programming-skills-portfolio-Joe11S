#Exercise 10 - Odd or Even

#odd or even test block
def odd_or_even_test(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

#take user input
number = int(input("Enter your Number: "))
odd_or_even_test(number)
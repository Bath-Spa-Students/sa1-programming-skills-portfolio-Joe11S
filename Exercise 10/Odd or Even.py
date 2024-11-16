#Exercise 10 - Odd or Even

#odd or even test function
def odd_or_even_test(number):
    if number % 2 == 0:
        x = "The number is even"
    else:
        x = "The number is odd"
    return x

#user input
number1 = odd_or_even_test(int(input("Enter the first Number: ")))
print(number1)

number2 = odd_or_even_test(int(input("Enter the second Number: ")))
print(number2)

number3 = odd_or_even_test(int(input("Enter the third Number: ")))
print(number3)
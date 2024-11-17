#Exercise 10 - Odd or Even

#odd or even test function
def odd_or_even(number):
    if number % 2 == 0:
        x = "The number is even"
    else:
        x = "The number is odd"
    return x
2
#user input
def Main():
    number = int(input("Enter the Number: "))
    result = odd_or_even(number)
    return result

#result
if __name__ == '__main__':
    Main()
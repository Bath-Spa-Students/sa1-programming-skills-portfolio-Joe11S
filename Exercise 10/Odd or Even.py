#Exercise 10 - Odd or Even

def odd_or_even_test(number):
    if number % 2 == 0:
        print("The number is even")
    else:
        print("The number is odd")

def main():
    odd_or_even_test(number)

number = int(input("Enter your Number"))
main()
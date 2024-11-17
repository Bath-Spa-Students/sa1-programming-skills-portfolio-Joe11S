#Exercise 10 - Is it Even?

#odd or even test function
def odd_or_even_test(number):
    if number % 2 == 0:
        x = "The number is even"
    else:
        x = "The number is odd"
    return x

#user input
result = odd_or_even_test(int(input("Enter the first Number: ")))

#result
print(result)
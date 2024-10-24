#Exercise 4 - Primitive Quiz

#define marking
marks = 0

#Ask the user a question 1
attempted_answer = input("Question 1: What is the capital of France?: ").lower()

#Define the correct answer

correct_answer = "paris"

#Give a remark
if attempted_answer == correct_answer:
    marks = marks + 1
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

#Ask the user a question 2
attempted_answer = input("Question 2: What is the capital of Belgium?: ").lower()

#Define the correct answer

correct_answer = "brussels"

#Give a remark
if attempted_answer == correct_answer:
    marks = marks + 1
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

    #Ask the user a question 3
attempted_answer = input("Question 3: What is the capital of Netherlands?: ").lower()

#Define the correct answer

correct_answer = "amsterdam"

#Give a remark
if attempted_answer == correct_answer:
    marks = marks + 1
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

    #Ask the user a question 4
attempted_answer = input("Question 4: What is the capital of Russia?: ").lower()

#Define the correct answer

correct_answer = "moscow"

#Give a remark
if attempted_answer == correct_answer:
    marks = marks + 1
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

    #Ask the user a question 5
attempted_answer = input("Question 5: What is the capital of South Korea?: ").lower()

#Define the correct answer

correct_answer = "seoul"

#Give a remark
if attempted_answer == correct_answer:
    marks = marks + 1
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

    #Ask the user a question 6
attempted_answer = input("Question 6: What is the capital of Japan?: ").lower()

#Define the correct answer

correct_answer = "tokyo"

#Give a remark
if attempted_answer == correct_answer:
    marks = marks + 1
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

    #Ask the user a question 7
attempted_answer = input("Question 7: What is the capital of China?: ").lower()

#Define the correct answer

correct_answer = "beijing"

#Give a remark
if attempted_answer == correct_answer:
    marks = marks + 1
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

    #Ask the user a question 8
attempted_answer = input("Question 8: What is the capital of UAE?: ").lower()

#Define the correct answer

correct_answer = "abu dhabi"

#Give a remark
if attempted_answer == correct_answer:
    marks = marks + 1
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

    #Ask the user a question 9
attempted_answer = input("Question 9: What is the capital of the UK?: ").lower()

#Define the correct answer

correct_answer = "london"

#Give a remark
if attempted_answer == correct_answer:
    marks = marks + 1
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

    #Ask the user a question 10
attempted_answer = input("Question 10: What is the capital of the Galactic Empire?: ").lower()

#Define the correct answer

correct_answer = "coruscant"

#Give a remark
if attempted_answer == correct_answer:
    marks = marks + 1
    print("Your answer is correct!")
else:
    print("Your answer is incorrect!")

#define the final grade

if marks == 10:
    grade = "S"

elif marks >= 8 and marks <10:
    grade = "A"

elif marks >=6 and marks <8:
    grade = "B"

elif marks >=4 and marks <6:
    grade = "C"

elif marks >=1 and marks <4:
    grade = "D"

else:
    grade = "F"

print("You've finished the quiz! Your grade is", grade)
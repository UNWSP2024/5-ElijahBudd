#Elijah Budd
# 2/18/2025

# Program #2: Math Quiz
# Write a program that gives simple math quizzes.  The program should display two random numbers to be added, such as

#     247

# + 129

# ------

# The program should allow the student to enter the answer.
# If the answer is correct, a message of congratulations should be displayed.
# If the answer is incorrect a message showing the correct answer should be displayed.
# The program must use a function that accomplishes part of the needed tasks.
import random

def math_quiz():
    number1 = random.randint(1, 1000)
    number2 = random.randint(1, 1000)

    answer = (number1 + number2)

    print(" ", number1)
    print("+", number2)
    print("------")

    user_answer = float(input("Enter answer: "))

    if user_answer == answer:
        print("Congrats! You got it right!")
    elif user_answer != answer:
        print("Sorry, the correct answer is", answer)

if __name__ == '__main__':
    math_quiz()

Test Run:
  570
+ 180
------
Enter answer: 750
Congrats! You got it right!

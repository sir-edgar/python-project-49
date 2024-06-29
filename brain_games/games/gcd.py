from random import randint


RULES = "Find the greatest common divisor of given numbers."


def is_gcd(num1, num2):
    """The function gets two numbers as arguments,
    then finds the largest common divisor.
    It will create a 'question' variable from the
    arguments and an 'answer' variable from the calculations.
    When the function is called, these variables are returned."""

    question = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    correct_answer = num1 + num2
    return correct_answer, question


def get_question_and_answer():
    """The function performs the function 'is_gcd',
    then writes the variable 'question' and 'answer' and returns them"""

    first_num = randint(5, 50)
    second_num = randint(5, 50)
    correct_answer, question = is_gcd(first_num, second_num)
    return correct_answer, question

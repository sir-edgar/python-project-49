from random import randint


RULES = "Find the greatest common divisor of given numbers."


def is_gcd(num1, num2):
    question = f'{num1} {num2}'
    while num1 != 0 and num2 != 0:
        if num1 > num2:
            num1 = num1 % num2
        else:
            num2 = num2 % num1
    correct_answer = num1 + num2
    return correct_answer, question


def get_question_and_answer():
    first_num = randint(5, 50)
    second_num = randint(5, 50)
    correct_answer, question = is_gcd(first_num, second_num)
    return correct_answer, question

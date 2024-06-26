from random import randint


rules = "Find the greatest common divisor of given numbers."


def task():
    a = randint(5, 50)
    b = randint(5, 50)
    question = (f'{a} {b}')

    while a != 0 and b != 0:

        if a > b:
            a = a % b

        else:
            b = b % a

    correct_answer = a + b
    return correct_answer, question



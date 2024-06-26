import random


rules = ("What is the result of the expression?")


def task():
    r_int = random.randint(1, 3)
    a = random.randint(1, 5)
    b = random.randint(1, 5)
    plus = f'{a} + {b}'
    multiplication = f'{a} * {b}'
    minus = f'{a} - {b}'

    if r_int == 1:
        question = plus
        correct_answer = eval(plus)

    elif r_int == 2:
        question = minus
        correct_answer = eval(minus)

    else:
        question = multiplication
        correct_answer = eval(multiplication)

    return correct_answer, question


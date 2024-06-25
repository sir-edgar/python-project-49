import random


def question_calc():
    global answer
    randomaizer = random.randint(1, 3)
    first_number = random.randint(1, 5)
    second_number = random.randint(1, 5)
    plus = f'{first_number} + {second_number}'
    multiplication = f'{first_number} * {second_number}'
    minus = f'{first_number} - {second_number}'
    if randomaizer == 1:
        print(f'Question: {plus}')
        answer = eval(plus)
    elif randomaizer == 2:
        print(f'Question: {minus}')
        answer = eval(minus)
    else:
        print(f'Question: {multiplication}')
        answer = eval(multiplication)



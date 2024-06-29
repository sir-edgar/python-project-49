from random import randint
from random import choice


RULES = "What is the result of the expression?"


def calculate(operator, num_a, num_b):
    question = f'{num_a} {operator} {num_b}'
    if operator == '+':
        correct_answer = num_a + num_b
    elif operator == '-':
        correct_answer = num_a - num_b
    else:
        correct_answer = num_a * num_b
    return correct_answer, question


def get_answer_and_question():
    frst_num = randint(1, 10)
    sec_num = randint(1, 10)
    rand_operator = choice(['+', '-', '*'])
    correct_answer, question = calculate_exam(rand_operator, frst_num, sec_num)
    return correct_answer, question


def calculate_exam(operator, num_a, num_b):
    question = f'{num_a} {operator} {num_b}'
    if operator == '+':
        correct_answer = num_a + num_b
    elif operator == '-':
        correct_answer = num_a - num_b
    else:
        correct_answer = num_a * num_b
    return correct_answer, question

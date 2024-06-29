from random import randint
from random import choice

RULES = "What is the result of the expression?"


def get_answer_and_question():
    frst_num = randint(1, 10)
    sec_num = randint(1, 10)
    rand_operator = choice(['+', '-', '*'])
    question = f'{frst_num} {rand_operator} {sec_num}'
    if rand_operator == '+':
        correct_answer = frst_num + sec_num
    elif rand_operator == '-':
        correct_answer = frst_num - sec_num
    else:
        correct_answer = frst_num * sec_num
    return correct_answer, question
    
from random import randint
from random import choice


RULES = "What is the result of the expression?"


def calculate_expression(operator, num_a, num_b):
    """This function get three arguments: two numbers and an operator.
    This function then performs simple mathematical calculations with
    the resulting data. At the output, we get a question and an answer
    that will be needed in the next function."""

    question = f'{num_a} {operator} {num_b}'
    if operator == '+':
        correct_answer = num_a + num_b
    elif operator == '-':
        correct_answer = num_a - num_b
    else:
        correct_answer = num_a * num_b
    return correct_answer, question


def get_question_and_answer():
    """This function performs the 'calculate_expression' function,
    and then transmits variables - correct_answer and question."""

    frst_num = randint(1, 10)
    sec_num = randint(1, 10)
    rand_operator = choice(['+', '-', '*'])
    correct_answer, question = (calculate_expression
                                (rand_operator, frst_num, sec_num))
    return correct_answer, question

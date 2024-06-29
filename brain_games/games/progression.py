from random import randint


RULES = "What number is missing in the progression?"


def make_progression(a, b):
    i = 0
    index_missing_number = randint(1, 10)
    question = str(a) + ' '
    while i < 10:
        c = (a + b)
        a = c
        i += 1
        if i != index_missing_number:
            question += str(c) + ' '
        else:
            correct_answer = c
            question += '.. '
    return correct_answer, question


def get_question_and_answer():
    first_number = randint(1, 50)
    second_number = randint(1, 5)
    correct_answer, question = make_progression(first_number, second_number)
    return correct_answer, question

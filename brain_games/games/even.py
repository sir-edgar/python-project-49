from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 100)

    if question % 2 == 0:
        correct_answer = 'yes'

    else:
        correct_answer = 'no'

    return correct_answer, question

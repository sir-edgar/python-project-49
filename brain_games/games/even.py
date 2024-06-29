from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False


def get_question_and_answer():
    question = randint(1, 100)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question

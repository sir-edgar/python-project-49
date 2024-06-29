from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def get_question_and_answer():
    question = randint(1, 100)
    num = question
    if num > 1:
        for n in range(2, num):
            if (num % n) == 0:
                correct_answer = 'no'
                return correct_answer, question
            correct_answer = 'yes'
    else:
        correct_answer = 'no'
        return correct_answer, question
    return correct_answer, question

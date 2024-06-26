from random import randint


rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def task():
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

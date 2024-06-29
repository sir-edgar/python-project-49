from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def get_question_and_answer():
    question = randint(1, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question

from random import randint


RULES = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(num):
    """This function get a number as an argument,
     then checks if it is a prime number or not. Returns a Boolean"""
    if num == 1:
        return False
    for n in range(2, int(num ** 0.5) + 1):
        if num % n == 0:
            return False
    return True


def get_question_and_answer():
    """This function calls the 'is_prime' function.
    The function then returns the variables 'correct_answer' and 'question'"""

    question = randint(1, 100)
    if is_prime(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question

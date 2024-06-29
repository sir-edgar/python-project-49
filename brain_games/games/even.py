from random import randint


RULES = 'Answer "yes" if the number is even, otherwise answer "no".'


def is_even(num):
    """This function checks the number for parity,
    then returns a Boolean"""

    if num % 2 == 0:
        return True
    else:
        return False


def get_question_and_answer():
    """This function creates a number,
    then passes it to the 'is_even' function.
    The received data is converted to the desired format
    and transmitted further"""
    question = randint(1, 100)
    if is_even(question):
        correct_answer = 'yes'
    else:
        correct_answer = 'no'
    return correct_answer, question

from random import randint


rules = "What number is missing in the progression?"


def task():
    i = 0
    a = randint(1, 50)
    b = randint(1, 5)
    int_fot_points = randint(1, 10)
    question = str(a) + ' '
    while i < 10:
        c = (a + b)
        a = c
        i += 1
        if i != int_fot_points:
            question += str(c) + ' '
        else:
            correct_answer = c
            question += '.. '
    return correct_answer, question

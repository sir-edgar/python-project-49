import random
import prompt


def question_even():
    global correct_answer
    random_number = random.randint(1, 100)
    print(f'Question: {random_number}')
    if random_number % 2 == 0:
        correct_answer = 'yes'
    else:
        correct_answer = 'no'


def even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    points = 0
    THREE_POINTS = 3
    while points < THREE_POINTS:
        question_even()
        users_answer = input('Your answer: ')
        if correct_answer == users_answer:
            points += 1
            print('Correct!')
        else:
            print(f"'{users_answer}' is wrong answer ;(. Correct answer was '{correct_answer}'. \nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')





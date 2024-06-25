import prompt
import random


answer = 0
def question_calc():
    global answer
    randomaizer = random.randint(1, 3)
    first_number = random.randint(1, 5)
    second_number = random.randint(1, 5)
    plus = f'{first_number} + {second_number}'
    multiplication = f'{first_number} * {second_number}'
    minus = f'{first_number} - {second_number}'
    if randomaizer == 1:
        print(f'Question: {plus}')
        answer = eval(plus)
    elif randomaizer == 2:
        print(f'Question: {minus}')
        answer = eval(minus)
    else:
        print(f'Question: {multiplication}')
        answer = eval(multiplication)


def calc_game():
    print("Welcome to the Brain Games!")
    global name
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What is the result of the expression?")
    points = 0
    THREE_POINTS = 3
    while points < THREE_POINTS:
        question_calc()
        users_answer = input('Your answer: ')
        if users_answer == str(answer):
            points += 1
            print('Correct!')
        else:
            points = 0
            print(f"'{users_answer}' is wrong answer ;(. Correct answer was '{answer}'.\nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    calc_game()


if __name__ == '__main__':
    main()
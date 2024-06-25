import random
import prompt


def gcd():
    a = random.randint(5, 50)
    b = random.randint(5, 50)
    print(f'Question: {a} {b}')
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    global result
    result = a + b


def gcd_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Find the greatest common divisor of given numbers.")
    points = 0
    THREE_POINTS = 3
    while points < THREE_POINTS:
        gcd()
        users_answer = input('Your answer: ')
        if users_answer == str(result):
            points += 1
            print(f'Correct!')
        else:
            points = 0
            print(f"'{users_answer}' is wrong answer;(. Correct answer was '{result}'. \nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    gcd_game()


if __name__ == '__main__':
    main()
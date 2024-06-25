import random
import prompt



def progression():
    i = 0
    a = random.randint(1, 50)
    b = random.randint(1, 5)
    int_fot_points = random.randint(1, 10)
    result = str(a) + ' '
    while i < 10:
        c = (a + b)
        a = c
        i += 1
        if i != int_fot_points:
            result += str(c) + ' '
        else:
            global answer
            answer = c
            result += '.. '
    print(f'Question: {result}')


def progression_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("What number is missing in the progression?")
    points = 0
    THREE_POINTS = 3
    while points < THREE_POINTS:
        progression()
        users_answer = input('Your answer: ')
        if str(answer) == users_answer:
            print(f'Correct!')
            points += 1
        else:
            print(f"'{users_answer}' is wrong answer ;(. Correct answer was '{answer}'. \nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    progression_game()

if __name__ == '__main__':
    main()
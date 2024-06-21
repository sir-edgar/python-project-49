import random
import prompt


beg = 1
end = 20
username = ''


def random_int():
    result = random.randint(beg, end)
    return result


def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    global username
    username = name


def even_game():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    points = 0
    THREE_POINTS = 3
    while points < THREE_POINTS:
        random_number = random_int()
        print(f'Question: {random_number}')
        answer = input('Your answer: ')
        if is_even(random_number) == answer:
            points += 1
            print('Correct!')
        else:
            points = 0
            print("'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {name}!")
    print(f'Congratulations, {username}!')
#is_even(random_int())
#print(is_even(12))
welcome_user()
even_game()




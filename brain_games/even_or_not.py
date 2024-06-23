import random
import prompt



def is_even(num):
    if num % 2 == 0:
        return 'yes'
    else:
        return 'no'

def even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Answer 'yes' if the number is even, otherwise answer 'no'.")
    points = 0
    THREE_POINTS = 3
    while points < THREE_POINTS:
        random_number = random.randint(1, 100)
        print(f'Question: {random_number}')
        answer = input('Your answer: ')
        if is_even(random_number) == answer:
            points += 1
            print('Correct!')
        elif answer == 'yes':
            print(f"'yes' is wrong answer ;(. Correct answer was 'no'. \nLet's try again, {name}!")
            return
        elif answer == 'no':
            print(f"'no' is wrong answer ;(. Correct answer was 'yes'. \nLet's try again, {name}!")
            return
        else:
            print(f'invalid value! \nAnswer "yes" if the number is even, otherwise answer "no".')
            return
    print(f'Congratulations, {name}!')


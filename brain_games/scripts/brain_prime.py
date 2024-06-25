import random
import prompt


def is_prime():
    global number
    global answer
    number = random.randint(1, 100)
    print(f'Question: {number}')
    if number <= 1:
        answer = 'no'
        return False
    for i in range(2, int(number ** 0.5) + 1):
        if number % i == 0:
            answer = 'no'
            return False
    answer = 'yes'
    return True


def prime_game():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print("Answer 'yes' if given number is prime. Otherwise answer 'no'.")
    points = 0
    THREE_POINTS = 3
    while points < THREE_POINTS:
        is_prime()
        users_answer = input('Your answer: ')
        if users_answer == answer:
            points += 1
            print('Correct!')
        else:
            print(f"'{users_answer}' is wrong answer ;(. Correct answer was '{answer}'. \nLet's try again, {name}!")
            return
    print(f'Congratulations, {name}!')


def main():
    prime_game()

if __name__ == '__main__':
    main()
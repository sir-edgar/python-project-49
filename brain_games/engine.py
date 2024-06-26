import prompt


POINTS_FOR_WIN = 3


def welcome_user():
    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def universal_engine(game):
    name = welcome_user()
    print(game.rules)
    counter = 0

    while counter < POINTS_FOR_WIN:
        correct_answer, question = game.task()
        print(f'Question: {question}')
        users_answer = input('Your answer: ')

        if str(correct_answer) == users_answer:
            counter += 1
            print('Correct!')

        else:
            print(f"'{users_answer}' is wrong answer ;(.\
            Correct answer was '{correct_answer}'.\
             \nLet's try again, {name}!")
            return

    print(f'Congratulations, {name}!')

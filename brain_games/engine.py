import prompt


POINTS_FOR_WIN = 3


def welcome_user():
    """The function asks for a name and prints several lines.
    Then she returns variable 'name'"""

    print("Welcome to the Brain Games!")
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    return name


def start_game(game):
    """This function calls the 'welcome_user' function and prints the 'RULES' variable.
    As an argument, she gets a module with game logic to write the variables 'correct_answer'
    and 'question' from it. Then you are asked to enter a response from the user,
    after which the received data is checked against the correct answer.
    The function also tells you whether the user gave the correct answer or not."""

    name = welcome_user()
    print(game.RULES)
    counter = 0

    while counter < POINTS_FOR_WIN:
        correct_answer, question = game.get_question_and_answer()
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

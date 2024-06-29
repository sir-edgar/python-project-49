import prompt


def welcome_user():
    """The function asks for a name and prints several lines"""

    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')

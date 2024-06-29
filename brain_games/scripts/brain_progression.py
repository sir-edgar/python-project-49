#!/usr/bin/env python3
from brain_games.games import progression
from brain_games.engine import start_game


def main():
    """This function calls the 'start_game' function
     and passes the logic of the game to it as an argument."""

    start_game(progression)


if __name__ == '__main__':
    main()

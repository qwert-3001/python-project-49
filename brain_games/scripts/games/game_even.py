import random

from brain_games.scripts.game_engine import run_game


def generate_even_question():

    number = random.randint(1, 25)
    question = number
    answer = 'yes' if abs(number % 2) == 0 else 'no'

    return question, answer


def game_even():
    rules = 'yes" if the number is even, otherwise answer "no".'
    run_game(rules, generate_even_question)
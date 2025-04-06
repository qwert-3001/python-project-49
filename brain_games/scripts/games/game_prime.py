import random

from brain_games.scripts.game_engine import run_game


def generate_prime_question():
    
    SIMPLE_NUMBER = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
    answer = ''

    question = random.randint(1, 54)
    if question in SIMPLE_NUMBER:
        answer = 'yes'
    else:
        answer = 'no'

    return question, answer 


def game_prime():
    rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'
    run_game(rules, generate_prime_question)
import random

from brain_games.scripts.game_engine import run_game


def generate_prime_question():
    
    simple_number = (2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37, 41, 43, 47, 53)
    answer = ''

    question = random.randint(1, 54)
    if question in simple_number:
        answer = 'yes'
    else:
        answer = 'no'

    return question, answer 


def game_prime(user_name):
    rules = '"yes" if given number is prime. Otherwise answer "no"'
    run_game(user_name, rules, generate_prime_question)
import random

from brain_games.scripts.game_engine import run_game


def generate_gcd_question():

    number_one, number_two = random.randint(1, 25), random.randint(30, 150)
    question = f'{number_one} and {number_two}'
    # Алгоритм Евклида
    while number_one != 0 and number_two != 0:
        if number_one > number_two:
            number_one = number_one % number_two
        else:
            number_two = number_two % number_one
    
    answer = str(number_one + number_two)
    
    return question, answer


def game_gcd(user_name):
    rules = 'Find the greatest common divisor of given numbers.'
    run_game(user_name, rules, generate_gcd_question)


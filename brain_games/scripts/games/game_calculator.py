import random

from brain_games.scripts.game_engine import run_game


def generate_calc_question():
    x, y = random.randint(1, 10), random.randint(1, 10)
    operator = random.choice(['+', '-', '*'])
    
    if operator == '+':
        question = f'{x} + {y}'
        answer = str(x + y)
    elif operator == '-':
        question = f'{x} - {y}'
        answer = str(x - y)
    else:
        question = f'{x} * {y}'
        answer = str(x * y)
    
    return question, answer


def game_calculator():
    rules = 'What is the result of the expression?'
    run_game(rules, generate_calc_question)
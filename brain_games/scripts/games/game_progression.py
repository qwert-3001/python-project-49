import random

from brain_games.scripts.game_engine import run_game


def generate_progression_question():

    progression_line = []
    random_pos = random.randint(2, 9)
    number_from_pos = 0
    iter_number = random.randint(2, 8)

    for i in range(0, 10):
        progression_line.append(str(i * iter_number))
    
    progression_line[random_pos], number_from_pos = \
    '..', progression_line[random_pos]

    question = ' '.join(progression_line)
    answer = number_from_pos

    return question, answer 


def game_progression():
    rules = 'What number is missing in the progression?'
    run_game(rules, generate_progression_question)
import prompt

from brain_games.cli import welcome_user
from brain_games.scripts.brain_games import greet


def run_game(game_rules, generate_question_answer, round=3):
    
    greet()
    user_name = welcome_user()

    print(game_rules)

    correct_answers = 0

    while correct_answers < round:
        question, correct_answer = generate_question_answer()
        print(f'Question: {question}')

        user_answer = prompt.string('Your answer: ')

        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(f'''{user_answer} is wrong answer ;(.
                  Correct answer was {correct_answer}.
                  Let's try again, {user_name}!''')
            return
        
    print(f'Congratulations, {user_name}!')
    return True


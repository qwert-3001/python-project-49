import random

import prompt


def brain_even(user_name):
    
    print('Answer "yes" if the number is even, otherwise answer "no".')

    sum_correct_answer = 0

    while sum_correct_answer < 3:

        rnd_number = random.randint(1, 25)
        print(f'Question: {rnd_number}')

        user_answer_is = prompt.string('Your answer: ')

        if (rnd_number % 2 == 0 and user_answer_is == 'yes') or \
           (rnd_number % 2 != 0 and user_answer_is == 'no'):
            print('Correct!')
            sum_correct_answer += 1
        else:
            correct_answer = 'yes' if rnd_number % 2 == 0 else 'no'
            print(f'''{user_answer_is} is wrong answer ;(. 
Correct answer was {correct_answer}.
Let's try again, {user_name}''')
            sum_correct_answer = 0
    
    print(f'Congratulations, {user_name}')
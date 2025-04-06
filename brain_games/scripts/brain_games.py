from brain_games.cli import welcome_user
from brain_games.scripts.games import (
	game_calculator,
	game_even,
	game_gcd,
	game_progression,
)
#from brain_games.scripts.games.game_calculator import game_calculator
#rom brain_games.scripts.games.game_even import game_even
#from brain_games.scripts.games.game_gcd import game_gcd
#from brain_games.scripts.games.game_progression import game_progression


def greet():
	print('Welcome to the Brain Games!')


def main():
    greet()
    user_name = welcome_user()
    game_even(user_name)
    game_calculator(user_name)
    game_gcd(user_name)
    game_progression(user_name)
    

if __name__ == "__main__":
    main()
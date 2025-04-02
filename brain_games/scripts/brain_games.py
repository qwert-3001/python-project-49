from brain_games.cli import welcome_user
from brain_games.scripts.brain_even import brain_even


def greet():
	print('Welcome to the Brain Games!')


def main():
    greet()
    user_name = welcome_user()
    brain_even(user_name)


if __name__ == "__main__":
    main()
import random
from numpy import arange
from time import sleep

def welcome_screen() -> None:
    sleep(2)
    print("WELCOME TO THE GAME - GUESSING NUMBERS!!!!")
    sleep(2)
    print("------------------------------------------")
    sleep(2)
    print("Rules: THERE ARE NO RULES!!")
    sleep(4)
    print("ACTUALLY I LIED!! THERE IS ONLY ONE RULE: ENJOY THE GAME.")
    sleep(3)
    print("FORGET ABOUT YOUR WORRIES AND INSECURITIES; JUST FOCUS ON THE GAME!")
    sleep(4)
    print("***** HAVE FUN *******")
    sleep(2)

def prompt() -> int | None:
    while True:
        try:
            question = int(input("Enter a number from 1 to 10: "))
            if 1 <= question <= 10:
                return question
            else:
                print("😠😠😠😠😠😠 (1-10)")
        except ValueError:
            print("You were instructed to ONLY ENTER A NUMBER FROM 1-10 😠😠")

def computer_choice() -> int:
    choices = arange(1,11)
    return random.choice(choices)

def player_guess(computer: int, player: int) -> None:
    
    print(f"Player = {player}")
    sleep(2)
    print(f"Computer = {computer}")
    sleep(1)
    if player == computer:
        print("YES!! YOU GOT IT RIGHT")
    else:
        print("OOPS! Too bad :(")

def main() -> None:
    welcome_screen()
    while True:
        computer = computer_choice()
        player = prompt()
        player_guess(computer, player)
        try:
            
            play_again = input("Do you want to try again? (Yes/No): ").lower()
            if play_again != "yes":
                print("Bye")
                break
        except Exception as e:
            print(e)

if __name__ == "__main__":
    main()

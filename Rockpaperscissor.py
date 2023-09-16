#import random from python library
import random

#function to get the user's choice and ensure it's valid
def get_user_choice():
    while True:
        user_choice =input("choose rock, paper or scissors:").strip().lower()
        if user_choice in ['rock','paper','scissor']:
            return user_choice
        else:
            print("invalid choice.Please choose rock,paper or scissor")


#function to get the computer's random choice
def get_computer_choice():
    return random.choice(['rock','paper','scissor'])


#function to determine the winner of the game
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "it's a tie!"
    elif(
        (user_choice == 'rock' and computer_choice == 'scissor') or
        (user_choice == 'scissor' and computer_choice == 'paper') or
        (user_choice == 'paper' and computer_choice =='rock')
    ):
        return 'you win'
    else:
        return 'computer win'
while True:
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print(f'you chose {user_choice}')
    print(f'computer chose {computer_choice}')
    result = determine_winner(user_choice,computer_choice)
    print(result)

    play_again = input("do you want to play again?(Y/N):")
    if play_again != 'Y':
        break
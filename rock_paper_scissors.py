import random

# Define a function to get the user's choice
def get_user_choice():
    while True:
        user_choice = input("Choose rock, paper, or scissors: ").lower()
        if user_choice in ['rock', 'paper', 'scissors']:
            return user_choice
        else:
            print("Invalid choice, please try again.")

# Define a function to get the computer's choice
def get_computer_choice():
    choices = ['rock', 'paper', 'scissors']
    computer_choice = random.choice(choices)
    return computer_choice

# Define a function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "Tie!"
    elif user_choice == 'rock' and computer_choice == 'scissors':
        return "You win!"
    elif user_choice == 'paper' and computer_choice == 'rock':
        return "You win!"
    elif user_choice == 'scissors' and computer_choice == 'paper':
        return "You win!"
    else:
        return "Computer wins!"

# Define a function to play the game
def play_game():
    print("Let's play Rock-Paper-Scissors!")
    user_choice = get_user_choice()
    computer_choice = get_computer_choice()
    print("You chose", user_choice)
    print("Computer chose", computer_choice)
    result = determine_winner(user_choice, computer_choice)
    print(result)

# Play the game
play_game()

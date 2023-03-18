import random

# Define the possible moves and the rules
MOVES = ['rock', 'paper', 'scissors']
RULES = {
    'rock': {'win': 'scissors', 'lose': 'paper'},
    'paper': {'win': 'rock', 'lose': 'scissors'},
    'scissors': {'win': 'paper', 'lose': 'rock'}
}

# Define a function to get the player's move
def get_player_move():
    while True:
        move = input('Enter your move (rock, paper, or scissors): ')
        if move in MOVES:
            return move
        else:
            print('Invalid move. Please try again.')

# Define a function to get the computer's move
def get_computer_move():
    return random.choice(MOVES)

# Define a function to determine the winner
def get_winner(player_move, computer_move):
    if player_move == computer_move:
        return 'tie'
    elif RULES[player_move]['win'] == computer_move:
        return 'player'
    else:
        return 'computer'

# Define the main function
def main():
    print('Welcome to Rock, Paper, Scissors!')
    player_wins = 0
    computer_wins = 0
    ties = 0
    while True:
        print(f'\nPlayer wins: {player_wins}, Computer wins: {computer_wins}, Ties: {ties}')
        player_move = get_player_move()
        computer_move = get_computer_move()
        print(f'Player: {player_move}, Computer: {computer_move}')
        winner = get_winner(player_move, computer_move)
        if winner == 'player':
            print('Player wins!')
            player_wins += 1
        elif winner == 'computer':
            print('Computer wins!')
            computer_wins += 1
        else:
            print('It\'s a tie!')
            ties += 1

# Call the main function
if __name__ == '__main__':
    main()

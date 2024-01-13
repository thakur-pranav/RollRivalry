import random


def roll():
    min_value = 1
    max_value = 6
    roll = random.randint(min_value, max_value)
    
    return roll


def get_number_of_players():
    while True:
        try:
            players = int(input("Enter the number of players (2 - 4): "))
            if min_players <= players <= max_players:
                return players
            else:
                print("Must be between 2 - 4 players.")
        
        except ValueError:
            print("Invalid input, try again.")
            

def get_roll_decision():
    while True:
        decision = input("Would you like to roll (y/n)? ")
        if decision in ['y', 'n']:
            return decision
        else:
            print("Invalid input. Please enter 'y' for yes or 'n' for no.")

            

def player_turn(player_idx, player_score):
    print(f"\nPlayer number {player_idx + 1}'s turn has just started!!!")
    print("Your total score is: ", player_score[player_idx])
    current_score = 0
    
    while True:
        should_roll = get_roll_decision()
        if should_roll.lower() == "n":
            break
        
        value = roll()
        if value == 1:
            print("You rolled a 1! Turn done!")
            current_score = 0
            break
        else:
            current_score += value
        
        print("You rolled:", value)
    
    player_score[player_idx] += current_score
    print(f"NOW your total score is: {player_score[player_idx]}")


min_players = 2
max_players = 4
max_score = int( input("Set your winning score of this game: "))

players = get_number_of_players()

player_score = [0 for _ in range(players)]

while max(player_score) < max_score :
    for player_idx in range(players):
        player_turn(player_idx, player_score)
        
max_score = max(player_score)
winning_idx = player_score.index(max_score)

print(f"Player number {winning_idx + 1} is the winner with a score of {max_score}!")
print("CONGRATULATIONS!!! Player", winning_idx + 1)
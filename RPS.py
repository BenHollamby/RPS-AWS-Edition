#Welcome to RPS AWS Edition
import sys
import random
from turtle import xcor

rock_paper_scissor = [0,1,2]

computer1_wins = 0
computer1_losses = 0
ties = 0
computer2_wins = 0
computer2_losses = 0
number_of_games = 0

results = {}

for i in range(int(sys.argv[1])):
    computer1_choice = random.choice(rock_paper_scissor)
    computer2_choice = random.choice(rock_paper_scissor)
    number_of_games += 1
    round = 'Round' + str(number_of_games)
    
    if computer1_choice == computer2_choice:
        ties += 1
        results[round] = {}
        results[round]['computer1_choice'] = computer1_choice
        results[round]['computer2_choice'] = computer2_choice
        results[round]['Won'] = 'None'
        results[round]['Lost'] = 'None'
        results[round]['Tie'] = 'True'
        
    elif computer1_choice == 0 and computer2_choice == 2 or computer1_choice == 1 and computer2_choice == 0 or computer1_choice == 2 and computer2_choice == 1:
        computer1_wins += 1
        computer2_losses += 1
        results[round] = {}
        results[round]['computer1_choice'] = computer1_choice
        results[round]['computer2_choice'] = computer2_choice
        results[round]['Won'] = 'Computer1'
        results[round]['Lost'] = 'Computer2'
        results[round]['Tie'] = 'False'

    elif computer1_choice == 2 and computer2_choice == 0 or computer1_choice == 1 and computer2_choice == 2 or computer1_choice == 0 and computer2_choice == 1:
        computer2_wins += 1
        computer1_losses += 1
        results[round] = {}
        results[round]['computer1_choice'] = computer1_choice
        results[round]['computer2_choice'] = computer2_choice
        results[round]['Won'] = 'Computer2'
        results[round]['Lost'] = 'Computer1'
        results[round]['Tie'] = 'False'
        
print(f"There were {number_of_games} games played!")
print(f"{ties} of those were tied games!")

print(f"Computer 1 won {computer1_wins} games,and lost {computer1_losses} games!")
print(f"Computer 2 won {computer2_wins} games and lost {computer2_losses} games!")

if computer1_wins == computer2_wins:
    print(f"The result is a tie after {number_of_games}!")

elif computer1_wins > computer2_wins:
    computer1_by = (computer1_wins - computer2_wins)
    print(f"Computer 1 is the overall winner with {computer1_wins} to {computer2_wins} winning by {computer1_by} match points!")

else:
    computer2_by = (computer2_wins - computer1_wins)
    print(f"Computer 2 is the winner with {computer2_wins} to {computer1_wins} winning by {computer2_by} match points!")

print()
for x in results:
    print(x, results[x])
import random
def roll():
    min_value=1
    max_value=6
    roll=random.randint(min_value,max_value)
    return roll

while(True):
    total_players = input("Enter the Number of players 2 - 4: ")
    if total_players.isdigit():
        total_players=int(total_players)
        if 2 <= total_players <= 4:
            break
        else:
            print("Input a number btn 2 - 4: ")
    else:
        print("Enter a number try again")       
max_score=50
player_score = [0 for _ in range(total_players)]

while max(player_score) < max_score:
    for player_count in range(total_players):
        print("Player",player_count+1,"Turn Begins: ")
        currentscore=0
        while(True):
            wana_roll = input("Do u want to roll 'y' for yes and 'n' for no: ")
            if wana_roll.lower() !="y":
                break
            score=roll()
            print("You Rolled ",score)
            if score == 1:
                currentscore=0
                break
            else:
                currentscore= currentscore + score
        player_score[player_count]=player_score[player_count]+currentscore
        print("Total Score of ",player_count+1,"is",player_score[player_count])

winning_score=max(player_score)
winning_index=player_score.index(winning_score)
print("Player Number",winning_index+1,"Won with Score of",winning_score)

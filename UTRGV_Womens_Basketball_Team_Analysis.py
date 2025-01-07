# -*- coding: utf-8 -*-
"""
Created on Wed Nov 13 15:48:21 2024

@author: vgarz

Project: UTRGV Women's Basketball Team Score Analysis

Description:
This project analyzes the scores of the UTRGV Women's basketball team from a set of 10 games during the 2023 season.
The program provides several functionalities, including displaying all game scores, retrieving specific game scores,
counting UTRGV wins, and calculating statistical insights using Python and Pandas.

Features:
1. Display all game scores with opponent results for the season.
2. Retrieve the score of a specific game based on user input.
3. Count and display the total number of games won by the UTRGV Women's basketball team.
4. Create a Pandas DataFrame with game scores and calculate descriptive statistics, including:
   - Highest and lowest UTRGV scores
   - Average UTRGV score
   - Average opponent score

Tools and Libraries:
- Python (for core logic)
- Pandas (for data manipulation and statistical analysis)
"""

#Step 1: Print all UTRGV Women's basketball team scores
print("Step 1: Print all UTRGV Women's basketball team scores")
scores = [
    [55, 84],  # Southern Utah (2/4/2023)
    [42, 76],  # SFA (2/9/2023)
    [75, 71],  # ACU (2/11/2023)
    [66, 73],  # Southern Utah (2/16/2023)
    [86, 89],  # Utah Tech (2/18/2023)
    [66, 58],  # Tarleton (2/22/2023)
    [65, 61],  # Sam Houston (2/25/2023)
    [69, 59],  # Utah Valley (2/28/2023)
    [76, 81],  # Cal Baptist (3/2/2023)
    [49, 65]   # NM State (3/6/2023)
]

for game in scores:
    print(game)

print()
    

 
#Step 2: Get game score
print("Step 2: Get game score")
def get_game_score():
    game_number = int(input("Which game would you like to see the score for? (1 - 10): "))
    
    index = game_number - 1
    return game_number, scores[index]

for i in range(2):
    game_num, score = get_game_score()
    print("You requested game #" + str(game_num))
    print("The score in game #" + str(game_num) + " was UTRGV: " + str(score[0]) + ", Opponent: " + str(score[1]))
print()


#Step 3: Count UTRGV wins
print("Step 3: Count UTRGV wins")

def count_utrgv_wins():
    win_count = 0
    
    for i in scores:
        if i[0] > i[1]:
            win_count += 1
        else:
            pass
    
    return win_count

win_count = count_utrgv_wins()
print("UTRGV won " + str(win_count) + " games.")
print()


# Step 4: Create a pandas DataFrame with custom column headers
import pandas as pd

print("Step 4: Create a pandas DataFrame with custom column headers")

df = pd.DataFrame(scores, columns=["UTRGV", "Opponent"])
print("Game Scores DataFrame:")
print(df)
print()

# Function to calculate descriptive statistics
def calculate_statistics():
    highest_utrgv = df["UTRGV"].max()  # Highest UTRGV score
    lowest_utrgv = df["UTRGV"].min()   # Lowest UTRGV score
    avg_utrgv = df["UTRGV"].mean()     # Average UTRGV score
    avg_opponent = df["Opponent"].mean()  # Average opponent score

    return highest_utrgv, lowest_utrgv, avg_utrgv, avg_opponent

# Main logic to call the function and print the results
highest, lowest, avg_utrgv, avg_opp = calculate_statistics()
print("Highest UTRGV score: " + str(highest))
print("Lowest UTRGV score: " + str(lowest))
print("Average UTRGV score: " + str(round(avg_utrgv, 2)))
print("Average Opponent score: " + str(round(avg_opp, 2)))


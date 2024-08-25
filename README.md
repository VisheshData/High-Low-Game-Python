# 🥇 High-Low Game
This is a simple command-line game where you compare the follower counts of famous personalities and guess who has more. The goal is to score as many points as possible by selecting the correct option.

## 🎮 Game Rules
Compare Follower Counts:
You are presented with two options: A and B. Guess which personality has more followers. If you guess correctly, you score 1 point, and the game continues.

## Winning Streak:
If your selected option has more followers, it becomes the new "A" for the next round, and a new option is presented as "B". The game continues until you make a wrong guess.

## Game Over:
The game ends when your guess is incorrect. Your final score is displayed.

## 🚀 How to Play
Run the game in your terminal.
Choose between 'A' or 'B' based on who you think has more followers.
The game continues until you guess incorrectly.
## 📁 Project Structure
main.py: The main game logic.
art.py: Contains ASCII art for the game (like the logo and separator).
game_data.py: Stores data about the personalities, including their follower counts.
## 🧠 Code Explanation
The game logic is implemented in several sections:

### 1. Initial Setup and Importing Libraries
```python

from art import logo, vs
from game_data import data
import random
from replit import clear

```

The game starts by importing the necessary libraries. The art.py file contains the logo and versus symbols, while game_data.py stores the dataset.
The random module is used to select accounts at random.
The replit library is used for clearing the screen during gameplay. On Replit, clear() helps refresh the console, giving a smooth user experience as the game progresses.
### 2. Getting Random Accounts
```python

def get_random_account(data):
  return random.randint(0, len(data) - 1)
```
This function returns a random index from the data list, which is used to select a personality for comparison.
### 3. Main Game Loop
The main game loop continues until the user guesses incorrectly:

```python

while win_loose:
    # Logic for comparing follower counts and updating the score
```
The game checks whether the user's choice (A or B) has more followers and updates the score accordingly.
If the user guesses correctly, the screen is cleared using clear() from the replit library, and the next comparison begins.
### 4. Ending the Game
```python

else:
    print(f"Sorry, your answer was wrong. Your final score: {score}")
    win_loose = False
```

The game ends when the user guesses incorrectly, displaying their final score.
## 🛠️ Requirements
Python 3.x

Replit environment (if running on Replit)
The replit package is specific to the Replit platform. It’s used here to clear the screen between rounds for better visual flow. If you are running this locally, you can replace clear() with any method that works in your environment, like:

```python

import os
os.system('cls' if os.name == 'nt' else 'clear')

```
## ▶️ How to Run
Clone the repository.
Ensure all three files (main.py, art.py, and game_data.py) are in the same directory.
Run the following command:
```bash

python main.py
```
Follow the prompts and enjoy the game!

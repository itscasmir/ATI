Dino Runner Game
Overview
The Dino Runner Game is a 2D side-scrolling endless runner game where the player controls a dinosaur, dodging various obstacles such as cacti and birds. The goal is to survive as long as possible while accumulating points. The game also features high scores, which are saved and can be displayed or searched by player name.

Features
Endless Running: The game continues indefinitely until the player hits an obstacle.
Obstacles: Includes small cacti, large cacti, and birds with varying behaviors.
Score System: Points increase as the player progresses; speed increases at regular intervals.
High Scores: Player's high scores are saved locally and can be displayed or searched.
User Interface: Menu for starting the game, restarting, switching users, searching scores, and displaying high scores.

Requirements
Python 3.x
Pygame
Installation
Install Python from the official website.
Install Pygame using pip:

pip install pygame


Ensure the following directory structure for the images:
pic/
├── bird/
│   ├── Bird1.png
│   └── Bird2.png
├── cactus/
│   ├── LargeCactus1.png
│   ├── LargeCactus2.png
│   ├── LargeCactus3.png
│   ├── SmallCactus1.png
│   ├── SmallCactus2.png
│   └── SmallCactus3.png
└── dino/
    ├── DinoDuck1 (1).png
    ├── DinoDuck2 (1).png
    ├── DinoJump.png
    ├── DinoRun1.png
    └── DinoRun2.png
└── other/
    ├── Cloud.png
    └── Track.png

    
Running the Game
Save the provided game code into a file, for example, dino.py.
Execute the game by running the script:


python dino.py
How to Play
Starting the Game:
Enter your player name when prompted.
At the main menu, press any key to start.
Game Controls:
Up Arrow Key: Jump
Down Arrow Key: Duck
Game Over:
When the game ends, the menu will display options:
Press any key to restart.
Press S to switch user.
Press F to search for a user's high score.
Press P to display sorted high scores.
High Scores
High scores are saved in highscores.json.
The game saves the highest score achieved by each player.
High scores can be displayed in descending order or searched by player name.
Code Structure
Global Constants: Screen dimensions, asset loading.



Class Definitions:
Dinosaur: Handles the dinosaur's behavior and animations.
Cloud: Manages cloud behavior and drawing.
Obstacle: Base class for obstacles.
SmallCactus, LargeCactus, Bird: Derived classes for specific obstacles.
Functions:
read_high_scores, write_high_scores: Handle high score file operations.
get_player_name: Prompts user for player name.
search_high_score, sort_high_scores, display_high_scores, display_user_high_score: Manage and display high scores.
main: The main game loop.
menu: Displays the main menu and handles user input.

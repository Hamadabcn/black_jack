# Welcome to the BlackJack Game

## Table of Contents
- [Overview](#overview)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [Functionality](#functionality)
  - [Game Logic](#game-logic)
- [How It Works](#how-it-works)
- [License](#license)
- [Contributing](#contributing)

## Overview
- The Blackjack game is a Python-based Pygame application that simulates the classic card game. Players compete against the dealer, aiming to reach a hand value as close to 21 as possible without exceeding it.

## Features
- Realistic card dealing and shuffling
- Player vs. dealer gameplay
- Score tracking for wins and losses
- Customizable betting options

## Installation
To run this project, ensure you have Python and Pygame installed on your system. To set it up, follow these steps:

1. Install Pygame using pip:
   ```bash
   pip install pygame

2. Clone the repository:
   ```bash
   https://github.com/Hamadabcn/black_jack.git

3. Navigate to the project directory:
   ```bash
   cd black_jack

4. Run the application:
   ```bash
   python main.py

## Usage
- Upon running the application, you will be prompted to place your bet and then dealt two cards. You can choose to "Hit" for another card or "Stand" to hold your total. The dealer will play according to standard rules, and the winner will be determined at the end of the round.

# Functionality
## Game Logic
The Game class implements the core functionalities of Blackjack:
- Card Dealing: Randomly draws cards for the player and dealer.
- Score Calculation: Computes the total value of the hands.
- Game Rules: Implements the rules for hitting, standing, and determining the winner.

## How It Works
- When the application starts, it initializes a new game. Players can place their bets and are then dealt two cards. The player can choose to hit or stand, while the dealer follows specific rules for drawing cards. The results of each round are displayed, and players can continue to play multiple rounds.

## License
- This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
- If you would like to contribute to this project, please fork the repository and submit a pull request.

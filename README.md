![blackjack](https://github.com/user-attachments/assets/679f909e-b676-4c0f-b249-51351b95dbff)
![blackjack 01](https://github.com/user-attachments/assets/22002427-732f-41fe-8f8a-0d0f8bae46b6)
![blackjack 02](https://github.com/user-attachments/assets/45929964-1c54-466f-aa70-70fd8c6efb2f)
![blackjack 03](https://github.com/user-attachments/assets/82a2a3c6-ac75-4179-a59a-0ae4d44a0f5b)
![blackjack 04](https://github.com/user-attachments/assets/33402862-ee55-42d3-91db-da18b2918486)
![blackjack 05](https://github.com/user-attachments/assets/dc5bfdf8-6446-4307-8447-c12d6df5a716)

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
- This game is a simplified version of Blackjack and does not involve any betting. Upon running the application, you will be dealt two cards and can choose to "Hit" for another card or "Stand" to hold your total. The dealer will play according to standard rules, and the winner will be determined at the end of the round.

# Functionality
## Game Logic
The Game class implements the core functionalities of Blackjack:
- Card Dealing: Randomly draws cards for the player and dealer.
- Score Calculation: Computes the total value of the hands.
- Game Rules: Implements the rules for hitting, standing, and determining the winner.

## How It Works
- When the application starts, it initializes a new game of Blackjack. Players are dealt two cards and can choose to "Hit" to receive another card or "Stand" to hold their total. The dealer will play according to standard Blackjack rules, drawing cards until reaching a specified total. The winner is determined based on the final hands, and players can continue playing multiple rounds without any betting involved.

## License
- This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
- If you would like to contribute to this project, please fork the repository and submit a pull request.

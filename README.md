![imagen](./img/hundir-la-flota-juego-de-mesa.jpg)

# sink_the_fleet
 
# Battleship Game

This is a simple implementation of the Battleship game in Python. The game allows you to play against an AI opponent. 

## Getting Started

To run the game, follow these steps:

1. Ensure you have Python installed on your system (version 3.6 or later).
2. Clone the repository to your local machine or download the code as a ZIP file and extract it.
3. Open a terminal or command prompt and navigate to the project directory.
4. Install the required dependencies by running the following command:
   
   ```
   pip install -r requirements.txt
   ```

5. Run the game by executing the following command:

   ```
   python main.py
   ```

## Gameplay

1. Upon running the game, a menu will be displayed with different options.
2. Enter the number corresponding to the desired option.
3. If you choose option 1, you will start a game against the AI opponent.
4. In each turn, you will be prompted to enter the coordinates to target on the opponent's board.
5. The game will display the result of your shot (hit, miss, or sunk) and update the boards accordingly.
6. The game will continue until one of the players' fleets is completely destroyed.
7. Once the game ends, a message will be displayed indicating the winner.

**Note:** The game currently supports playing against an AI opponent only.

## File Structure

The codebase is organized as follows:

- `main.py`: The entry point of the game. Run this file to start the game.
- `game/`
  - `main_process_functions.py`: Contains functions for loading the menu and other game-related processes.
  - `board_process.py`: Defines the Board class responsible for managing the game board and fleet deployment.
  - `combat_process.py`: Implements the Combat_Process class that handles the game logic and combat between players.
  - `data_game.py`: Contains the Data_Game class that stores and manages game data.
- `utils/`
  - `utils.py`: Provides utility functions, including a function for clearing the console screen.

## Contributing

Contributions to the game are welcome! If you find any issues or have suggestions for improvements, feel free to open an issue or submit a pull request on the [GitHub repository](https://github.com/your-username/your-repository).

## License

This project is licensed under the [MIT License](https://opensource.org/licenses/MIT). Feel free to use, modify, and distribute the code as you see fit.
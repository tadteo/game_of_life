# game_of_life

A python implementation of the game of life (just for fun)

### Some history

The Game of Life: Basic Principles
Conway's Game of Life is a cellular automaton devised by the British mathematician John Horton Conway in 1970. It's a zero-player game, meaning its evolution is determined by its initial state, requiring no further input. The game is played on a two-dimensional orthogonal grid of square cells, each of which is in one of two possible states: alive or dead. The state of each cell changes from one generation to the next based on a set of simple rules related to the states of neighboring cells.

## Project Overview

This project builds upon the classic Game of Life, introducing an innovative twist: each cell is equipped with a neural network, enabling it to make decisions based on its environment. The architecture of these neural networks evolves over time using evolutionary algorithms, and they train during their lifespan. This approach explores the intersection of artificial life, machine learning, and evolutionary computation, pushing the boundaries of emergent behavior in computational systems.

## Code Structure

The main code is found in the src folder.

### Modules

#### Main Module (main.py):

The entry point of the application.
Manages the game loop and integrates the game logic with the GUI.

#### Game Logic Module (game.py):

Manages the state and behavior of each cell, including the neural network logic (to be expanded).
Handles the overall game state and updates it.

#### Conway's Game of Life Module (conway.py):

Implements the traditional rules of Conway's Game of Life.
Used for comparison with the neural network-based version.

#### GUI Module (gui.py):

Handles all graphical interface elements using Pygame.
Responsible for drawing the grid and updating the screen based on the game state.

#### Configuration (config.py):

Contains configuration and constants like screen size and colors.

### How It Works

The main.py module initializes the game and enters the main loop, where it updates the game logic and the GUI in each iteration.
The game.py or conway.py module updates the state of the game grid, either using neural networks (for an intelligent response to the environment) or following Conway's rules.
The gui.py module visualizes the current state of the game grid, rendering cells as alive or dead based on the game logic.

## Running the Project


### Setup and Execution

- Clone the Repository
- Install Dependencies:

```bash
pip install -r requirements.txt
```

- Run the Application:

- Activate your Conda environment (if you are using one).
- Run the main script:
python main.py

## Contributing

Contributions to the project are welcome! Whether it's enhancing the neural network logic, improving the GUI, or optimizing performance, your input is valuable.

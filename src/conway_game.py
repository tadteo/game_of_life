import random
from game import Game
from config import color_palette

class ConwayGame(Game):
    def __init__(self, width, height):
        super().__init__(width, height)
        # Initialize with some random alive cells
        for _ in range(int(width * height * 0.2)):  # 20% of the grid
            x = random.randint(0, width - 1)
            y = random.randint(0, height - 1)
            self.grid[y][x] = True

    def update(self):
        new_grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                new_grid[y][x] = self._update_cell(x, y)
        self.grid = new_grid

    def _update_cell(self, x, y):
        # Initialize the count of live neighbors
        live_neighbors = 0
        
        # Check all surrounding cells (the neighbors)
        for i in range(-1, 2):  # This will loop through -1, 0, 1
            for j in range(-1, 2):  # This will also loop through -1, 0, 1
                # Skip the check for the cell itself (when both i and j are 0)
                if not (i == 0 and j == 0):
                    # Check if the neighboring cell is within the grid boundaries
                    if (0 <= x + i < self.width) and (0 <= y + j < self.height):
                        # If the neighbor is alive (True), increase the count
                        if self.grid[y + j][x + i]:
                            live_neighbors += 1
        
        # Apply Conway's Game of Life rules:
        # 1. Any live cell with two or three live neighbors survives.
        # 2. Any dead cell with three live neighbors becomes a live cell.
        # 3. All other live cells die in the next generation. Similarly, all other dead cells stay dead.
        # The method returns True if the cell should be alive in the next generation, and False otherwise.
        return self.grid[y][x] and live_neighbors in [2, 3] or not self.grid[y][x] and live_neighbors == 3

import random
from game import Game

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
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    if (0 <= x + i < self.width) and (0 <= y + j < self.height):
                        if self.grid[y + j][x + i]:
                            live_neighbors += 1

        return self.grid[y][x] and live_neighbors in [2, 3] or not self.grid[y][x] and live_neighbors == 3

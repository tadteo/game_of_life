class ConwayGame:
    def __init__(self, width, height):
        # Initialize the game grid
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(width)] for _ in range(height)]

    def update(self):
        # Update the game state based on Conway's rules
        new_grid = [[False for _ in range(self.width)] for _ in range(self.height)]
        for y in range(self.height):
            for x in range(self.width):
                new_grid[y][x] = self._update_cell(x, y)
        self.grid = new_grid

    def _update_cell(self, x, y):
        # Determine the new state of a cell based on Conway's rules
        live_neighbors = 0
        for i in range(-1, 2):
            for j in range(-1, 2):
                if not (i == 0 and j == 0):
                    if (0 <= x + i < self.width) and (0 <= y + j < self.height):
                        if self.grid[y + j][x + i]:
                            live_neighbors += 1

        if self.grid[y][x]:
            return live_neighbors == 2 or live_neighbors == 3
        else:
            return live_neighbors == 3

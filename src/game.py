class Game:
    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.grid = [[False for _ in range(width)] for _ in range(height)]
        self.is_running = True  # Game state control

    def pause(self):
        self.is_running = False

    def resume(self):
        self.is_running = True
        
    def update(self):
        # To be implemented by child classes
        self.print_grid(debug=True)
        raise NotImplementedError("Update method must be implemented by subclass")
    
    def print_grid(self, debug=False):
        if debug:
            for row in self.grid:
                print(' '.join(['#' if cell else '.' for cell in row]))
            print("\n")

import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE

class GUI:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Intelligent Game of Life")

    def draw_grid(self):
        # Example: Draw a simple grid
        self.screen.fill(BLACK)
        for x in range(0, WINDOW_WIDTH, 40):  # Example grid size
            for y in range(0, WINDOW_HEIGHT, 40):
                rect = pygame.Rect(x, y, 40, 40)
                pygame.draw.rect(self.screen, WHITE, rect, 1)

    def update(self):
        # Update the display
        pygame.display.flip()

    def clear(self):
        # Clear the screen
        self.screen.fill(BLACK)

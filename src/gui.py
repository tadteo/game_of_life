import pygame
from config import WINDOW_WIDTH, WINDOW_HEIGHT, BLACK, WHITE, color_palette


class GUI:
    def __init__(self, game):
        pygame.init()
        self.screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
        pygame.display.set_caption("Intelligent Game of Life")
        self.game = game

        # Font setup
        self.font = pygame.font.Font(None, 24)

        # Top bar setup
        self.top_bar_height = 30
        self.iterations = 0

        # Bottom bar setup
        self.bottom_bar_height = 50
        self.pause_button = pygame.Rect(10, WINDOW_HEIGHT - 40, 80, 30)
        self.speed_slider_rect = pygame.Rect(WINDOW_WIDTH - 90, WINDOW_HEIGHT - 40, 80, 20)
        self.speed = 2  # Default speed

        # Colors from the palette
        self.top_bar_color = pygame.Color(color_palette['dark_slate_gray'])
        self.text_color = pygame.Color(color_palette['sand'])
        self.button_color = pygame.Color(color_palette['dark_red'])
        self.slider_color = pygame.Color(color_palette['magenta'])
        self.slider_button_color = pygame.Color(color_palette['cyan'])
        self.background_color = pygame.Color(color_palette['night_blue'])
        self.cell_color = pygame.Color(color_palette['sand'])

    def draw_top_bar(self):
        """Draws the top status bar."""
        top_bar_rect = pygame.Rect(0, 0, WINDOW_WIDTH, self.top_bar_height)
        pygame.draw.rect(self.screen, self.top_bar_color, top_bar_rect)

        # Display game status and iterations
        status_text = self.font.render(f'Status: {"Running" if self.game.is_running else "Paused"}', True, self.text_color)
        iterations_text = self.font.render(f'Iterations: {self.iterations}', True, self.text_color)
        speed_text = self.font.render(f'Speed: {self.speed} Hz', True, self.text_color)

        self.screen.blit(status_text, (10, 6))
        self.screen.blit(iterations_text, (200, 6))
        self.screen.blit(speed_text, (self.speed_slider_rect.x-15, 6))

    def draw_bottom_bar(self):
        """Draws the bottom settings bar for game control."""
        bottom_bar_rect = pygame.Rect(0, WINDOW_HEIGHT - self.bottom_bar_height, WINDOW_WIDTH, self.bottom_bar_height)
        pygame.draw.rect(self.screen, self.top_bar_color, bottom_bar_rect)

        # Update and Draw Pause button
        pause_text_label = 'Pause' if self.game.is_running else 'Resume'
        pygame.draw.rect(self.screen, self.button_color, self.pause_button)
        pause_text = self.font.render(pause_text_label, True, self.text_color)
        self.screen.blit(pause_text, (self.pause_button.x + 10, self.pause_button.y + 5))

        # Draw speed control slider
        pygame.draw.rect(self.screen, self.slider_color, self.speed_slider_rect)
        slider_pos = self.speed_slider_rect.x + (self.speed - 1) / 99 * self.speed_slider_rect.width
        pygame.draw.circle(self.screen, self.slider_button_color, (int(slider_pos), self.speed_slider_rect.centery), 10)

    def draw_grid(self):
        """Draws the cell grid."""
        self.screen.fill(self.background_color)
        grid = self.game.grid
        cell_size = WINDOW_WIDTH // len(grid[0])
        
        for y, row in enumerate(grid):
            for x, cell in enumerate(row):
                if cell:
                    pygame.draw.rect(self.screen, self.cell_color, (x * cell_size, y * cell_size, cell_size, cell_size))

    def update_status(self, is_running):
        status = 'Running' if is_running else 'Paused'
        self.status_text = self.font.render(status, True, WHITE)

    def update(self):
        """Updates the entire GUI including the grid, top bar, and bottom bar."""
        if self.game.is_running:
            self.iterations += 1

        self.draw_grid()
        self.draw_top_bar()
        self.draw_bottom_bar()

        pygame.display.flip()

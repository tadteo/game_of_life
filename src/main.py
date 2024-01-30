import pygame
import time
from gui import GUI
from conway_game import ConwayGame  # Import Conway's Game of Life logic
from ai_game import AIGame  # Import the custom game logic

def main_menu(screen):
    # Create a simple text-based menu to choose the game version
    font = pygame.font.Font(None, 36)  # Set the font for the text
    text = font.render("Press 1 for Custom Game, 2 for Conway's Game", True, (255, 255, 255))
    text_rect = text.get_rect(center=(screen.get_width()/2, screen.get_height()/2))  # Center the text

    screen.blit(text, text_rect)  # Render the text on the screen
    pygame.display.flip()  # Update the screen to show the text

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return None  # Exit if the window is closed
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    return AIGame(50, 50)  # Start custom game if '1' is pressed
                elif event.key == pygame.K_2:
                    return ConwayGame(50, 50)  # Start Conway's game if '2' is pressed
        pygame.time.wait(100)  # Small delay to reduce CPU usage

def main():
    pygame.init()  # Initialize Pygame
    screen = pygame.display.set_mode((800, 600))  # Set the screen size
    pygame.display.set_caption("Intelligent Game of Life")  # Set the window title

    game = main_menu(screen)  # Display the main menu and get the chosen game
    if game is None:
        return  # Exit if the menu returned None (window closed)

    gui = GUI(game)  # Initialize the GUI with the chosen game

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False # End the loop if the window is closed

            if event.type == pygame.MOUSEBUTTONDOWN:
                if gui.pause_button.collidepoint(event.pos):
                    game.is_running = not game.is_running  # Toggle the game state
                    gui.update_status(game.is_running)

            # Check if the click is on the speed slider
                if gui.speed_slider_rect.collidepoint(event.pos):
                    # Calculate new speed based on mouse position
                    gui.speed = int(1 + (event.pos[0] - gui.speed_slider_rect.x) / gui.speed_slider_rect.width * 99)
                    gui.game.speed = gui.speed  # Update game speed

        if game.is_running:
            pygame.time.delay(int(1000 / gui.speed))  # Adjust update frequency
            game.update() # Update the game state
        gui.update()  # Update the GUI based on the game state
        
    pygame.quit()  # Quit Pygame when the loop ends

if __name__ == "__main__":
    main()  # Run the main function when the script is executed

import pygame
from gui import GUI

def main():
    gui = GUI()
    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        gui.clear()
        gui.draw_grid()
        gui.update()

    pygame.quit()

if __name__ == "__main__":
    main()

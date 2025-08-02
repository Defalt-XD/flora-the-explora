import pygame
from level1 import start_level1
from level2 import start_level_2
from level3 import start_level_3
def game_window(width, height):
    pygame.init()
    game_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Learn Window")
    
    # Load background image
    background = pygame.image.load("menubg.jpg")
    background = pygame.transform.scale(background, (width, height))
    
    # Define button colors
    BUTTON_COLOR = (100, 100, 255)
    BUTTON_TEXT_COLOR = (255, 255, 255)

    # Function to create a button
    def create_button(text, x, y, width, height, color):
        pygame.draw.rect(game_screen, color, (x, y, width, height), border_radius=10)
        button_font = pygame.font.Font(None, 36)
        label = button_font.render(text, True, BUTTON_TEXT_COLOR)
        text_rect = label.get_rect(center=(x + width // 2, y + height // 2))
        game_screen.blit(label, text_rect)
        return pygame.Rect(x, y, width, height)  # Return button rectangle for event handling

    # Main loop
    running_game = True
    
    # Create buttons
    button1 = create_button("Level 1", 100, 300, 150, 50, BUTTON_COLOR)
    button2 = create_button("Level 2", 330, 300, 150, 50, BUTTON_COLOR)
    button3 = create_button("Level 3", 530, 300, 150, 50, BUTTON_COLOR)

    while running_game:
        game_screen.blit(background, (0, 0))  # Draw the background image
        
        # Redraw buttons every frame
        button1 = create_button("Level 1", 100, 300, 150, 50, BUTTON_COLOR)
        button2 = create_button("Level 2", 330, 300, 150, 50, BUTTON_COLOR)
        button3 = create_button("Level 3", 530, 300, 150, 50, BUTTON_COLOR)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if button1.collidepoint(mouse_pos):
                    start_level1()
                    print("Level 1 clicked!")
                elif button2.collidepoint(mouse_pos):
                    start_level_2()
                    print("Level 2 clicked!")
                elif button3.collidepoint(mouse_pos):
                    start_level_3()
                    print("Level 3 clicked!")

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":
    game_window(800, 600)

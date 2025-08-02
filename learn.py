import pygame

def learn_window(width, height):
    pygame.init()
    game_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Learn Window")
    
    # Load background image
    background = pygame.image.load("menubg.jpg")
    background = pygame.transform.scale(background, (800, 600))
    
    # Load foreground images (replace with your own image paths)
    foreground_image_1 = pygame.image.load("fruits/fruit.jpg")
    foreground_image_2 = pygame.image.load("flowers/plant.jpg")
    
    # Resize foreground images
    foreground_image_1 = pygame.transform.scale(foreground_image_1, (200, 200))
    foreground_image_2 = pygame.transform.scale(foreground_image_2, (200, 200))

    # Define button colors
    BUTTON_COLOR = (100, 100, 255)
    BUTTON_TEXT_COLOR = (255, 255, 255)

    # Font for colorful text
    font = pygame.font.Font(None, 50)

    # Function to display colorful text
    def display_text(text, color, x, y):
        label = font.render(text, True, color)
        game_screen.blit(label, (x, y))

    # Function to create a button
    def create_button(text, x, y, width, height, color):
        pygame.draw.rect(game_screen, color, (x, y, width, height))
        button_font = pygame.font.Font(None, 36)
        label = button_font.render(text, True, BUTTON_TEXT_COLOR)
        game_screen.blit(label, (x + width // 4, y + height // 4))

    # Main loop
    running_game = True
    while running_game:
        game_screen.fill((255, 255, 255))  # White background
        game_screen.blit(background, (0, 0))  # Draw the background image
        
        # Draw the colorful "Learn" text at the top
        display_text("LEARN", (0, 0, 0), 350, 120)  # Colorful magenta text

        # Draw the foreground images side by side
        game_screen.blit(foreground_image_1, (width // 4 - 100, height // 2 - 100)) # Image for "Flower"
        game_screen.blit(foreground_image_2, (3 * width // 4 - 100, height // 2 - 100)) # Image for "Fruit"
        
        # Create the buttons beneath the images
        create_button("Fruits", 130, 450, 150, 50, BUTTON_COLOR)
        create_button("Flowers", 530, 450, 150, 50, BUTTON_COLOR)
        
        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_x, mouse_y = pygame.mouse.get_pos()
                # Check for "Flower" button click
                if 130 <= mouse_x <= 280 and 450 <= mouse_y <= 500:  # Button bounds
                    print("You chose to learn about: Flower")
                    running_game = False
                    from wind1 import window1 # Close the current window
                    window1(width, height)  # Pass the required arguments to window1
                # Check for "Fruit" button click
                elif 530 <= mouse_x <= 680 and 450 <= mouse_y <= 500:  # Button bounds
                    print("You chose to learn about: Fruit")
                    running_game = False
                    from wind01 import window01# Close the current window
                    window01(width, height)  # 

        pygame.display.flip()

    pygame.quit()


if __name__ == "__main__":  # Ensures this runs ONLY when executing learn.py directly
    learn_window(800, 600)

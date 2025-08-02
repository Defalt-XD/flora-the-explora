import pygame,sys

def over_window(width, height):
    pygame.init()
    game_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Lesson Over")

    # Load background image
    background = pygame.image.load("end.png")
    background = pygame.transform.scale(background, (width, height))

    # Fonts
    font = pygame.font.Font(None, 50)
    button_font = pygame.font.Font(None, 36)

    # Button properties
    BUTTON_COLOR = (50, 150, 250)
    BUTTON_TEXT_COLOR = (255, 255, 255)
    BUTTON_WIDTH = 150
    BUTTON_HEIGHT = 50

    # Function to create a button
    def create_button(text, x, y, width, height, color):
        pygame.draw.rect(game_screen, color, (x, y, width, height))
        label = button_font.render(text, True, BUTTON_TEXT_COLOR)
        game_screen.blit(label, (x + 30, y + 10))
        return pygame.Rect(x, y, width, height)

    # Main loop
    running_game = True
    while running_game:
        game_screen.fill((255, 255, 255))  # White background
        game_screen.blit(background, (0, 0))  # Draw the background image

        # Display message
        #message = font.render("Lesson is over! want to learn Again ?", True, (0, 0, 0))
        #game_screen.blit(message, (width // 3, height // 3))

        # Create "Yes" and "No" buttons
        yes_button = create_button("Yes", 180, 500, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR)
        no_button = create_button("No", 500, 500, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR)

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()

                # Handle Yes button click
                if yes_button.collidepoint(mouse_pos):
                    print("Yes button clicked!")
                    # You can add functionality to load the next lesson here
                    from learn import learn_window  # Assuming learn_window is your next lesson
                    learn_window(800, 600)  # Open the next window (learn_window)
                    running_game = False  # Exit this window

                # Handle No button click
                elif no_button.collidepoint(mouse_pos):
                    pygame.quit()
                    sys.exit()
 # Exit this window

        pygame.display.flip()

    pygame.quit()

# Example call to start the lesson over window


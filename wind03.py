import pygame

def window03(width, height):
    pygame.init()
    game_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Window1")
    
    # Load background image
    background = pygame.image.load("flbg.jpg")
    background = pygame.transform.scale(background, (width, height))

    # Load images
    image1 = pygame.image.load("flowers/lotus.jpg")
    image2 = pygame.image.load("flowers/marigold.jpg")
    image3 = pygame.image.load("flowers/orchid.jpg")
    


    # Resize images
    image_size = (200, 200)
    image1 = pygame.transform.scale(image1, image_size)
    image2 = pygame.transform.scale(image2, image_size)
    image3 = pygame.transform.scale(image3, image_size)
    
    
    sound1 = pygame.mixer.Sound("flower_aud/lotus.wav")  # Sound for the first image
    sound2 = pygame.mixer.Sound("flower_aud/marigold.wav")   # Sound for the second image
    sound3 = pygame.mixer.Sound("flower_aud/orchid.wav")    # Sound for the third image
    
        # Define image areas for hover detection
    image1_rect = pygame.Rect(100, 150, *image_size)
    image2_rect = pygame.Rect(300, 150, *image_size)
    image3_rect = pygame.Rect(500, 150, *image_size)
    
    sound_played = [False, False, False]

    # Fonts
    font = pygame.font.Font(None, 36)
    button_font = pygame.font.Font(None, 30)

    # Button properties
    BUTTON_COLOR = (50, 150, 250)
    BUTTON_TEXT_COLOR = (255, 255, 255)
    BUTTON_WIDTH = 100
    BUTTON_HEIGHT = 50

    # Function to create a button
    def create_button(text, x, y, width, height, color):
        pygame.draw.rect(game_screen, color, (x, y, width, height))
        label = button_font.render(text, True, BUTTON_TEXT_COLOR)
        game_screen.blit(label, (x + 10, y + 10))
        return pygame.Rect(x, y, width, height)

    # Main loop
    running_game = True
    while running_game:
        game_screen.fill((255, 255, 255))  # White background
        game_screen.blit(background, (0, 0))

        # Display images
        game_screen.blit(image1, (50, 200))
        game_screen.blit(image2, (300, 200))
        game_screen.blit(image3, (550, 200))

        # Display names beneath images
        label1 = font.render("Lotus", True, (255,255,255))
        label2 = font.render("Marigold", True, (255,255,255))
        label3 = font.render("Orchid", True, (255,255,255))
        game_screen.blit(label1, (120, 420))
        game_screen.blit(label2, (350, 420))
        game_screen.blit(label3, (610, 420))

        # Create "Back" and "Next" buttons
        back_button = create_button("Back", 100, 500, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR)
        next_button = create_button("Next", 600, 500, BUTTON_WIDTH, BUTTON_HEIGHT, BUTTON_COLOR)
        
        
        mouse_pos = pygame.mouse.get_pos()

        # Check for hover and play sounds
        if image1_rect.collidepoint(mouse_pos) and not sound_played[0]:
            sound1.play()
            sound_played[0] = True
        elif not image1_rect.collidepoint(mouse_pos):
            sound_played[0] = False

        if image2_rect.collidepoint(mouse_pos) and not sound_played[1]:
            sound2.play()
            sound_played[1] = True
        elif not image2_rect.collidepoint(mouse_pos):
            sound_played[1] = False

        if image3_rect.collidepoint(mouse_pos) and not sound_played[2]:
            sound3.play()
            sound_played[2] = True
        elif not image3_rect.collidepoint(mouse_pos):
            sound_played[2] = False

        # Event handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running_game = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = pygame.mouse.get_pos()
                if back_button.collidepoint(mouse_pos):
                    print("Back button clicked!")
                    from wind02 import window02
                    window02(800, 600)
                    running_game = False  # Exit this windows
                elif next_button.collidepoint(mouse_pos):
                    print("Next button clicked!")
                    from wind04 import window04
                    window04(800, 600) 
                    running_game = False
                    # Add functionality for the next button if needed

        pygame.display.flip()

    pygame.quit()

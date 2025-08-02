import pygame

def window1(width, height):
    pygame.init()
    pygame.mixer.init()  # Initialize the mixer for audio

    game_screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption("Hover Sound Game")
    
    # Load background image
    background = pygame.image.load("1.png")
    background = pygame.transform.scale(background, (width, height))

    # Load images
    image1 = pygame.image.load("fruit.jpg")  # Replace with your "flower" image path if needed
    image2 = pygame.image.load("learn.jpg")
    image3 = pygame.image.load("11.jpg")

    # Resize images
    image_size = (200, 200)
    image1 = pygame.transform.scale(image1, image_size)
    image2 = pygame.transform.scale(image2, image_size)
    image3 = pygame.transform.scale(image3, image_size)

    # Load sounds
    sound1 = pygame.mixer.Sound("flower.wav")  # Sound for the first image
    sound2 = pygame.mixer.Sound("learn.wav")   # Sound for the second image
    sound3 = pygame.mixer.Sound("11.wav")    # Sound for the third image

    # Fonts
    font = pygame.font.Font(None, 36)

    # Define image areas for hover detection
    image1_rect = pygame.Rect(100, 150, *image_size)
    image2_rect = pygame.Rect(300, 150, *image_size)
    image3_rect = pygame.Rect(500, 150, *image_size)

    # Keep track of sounds already played
    sound_played = [False, False, False]

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
        label1 = font.render("Flower", True, (255,255,255))
        label2 = font.render("Learn", True, (0, 0, 0))
        label3 = font.render("Item", True, (0, 0, 0))
        game_screen.blit(label1, (120, 420))
        game_screen.blit(label2, (350, 420))
        game_screen.blit(label3, (610, 420))

        # Get mouse position
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

        pygame.display.flip()
    
    pygame.quit()

# Run the game
if __name__ == "__main__":
    window1(800, 600)

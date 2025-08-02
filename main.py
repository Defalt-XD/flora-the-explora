import pygame
import sys
from play import game_window
from learn import learn_window
# Initialize Pygame
pygame.init()

# Set up screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Background Image Example")

# Load background image
background = pygame.image.load("main.png")  # Make sure the path is correct

# Define colors
WHITE = (255, 255, 255)
BLUE = (0, 0, 255)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
HOVER_COLOR = (200, 200, 200)

# Define font
font = pygame.font.SysFont('Arial', 30)

# Button class to handle button creation and interaction
class Button:
    def __init__(self, text, x, y, width, height, color, hover_color, action=None):
        self.text = text
        self.rect = pygame.Rect(x, y, width, height)
        self.color = color
        self.hover_color = hover_color
        self.action = action
        self.is_hovered = False

    def draw(self, screen):
        # Check for hover effect
        mouse_pos = pygame.mouse.get_pos()
        self.is_hovered = self.rect.collidepoint(mouse_pos)
        color = self.hover_color if self.is_hovered else self.color
        
        # Draw the button with gradient
        pygame.draw.rect(screen, color, self.rect, border_radius=15)
        pygame.draw.rect(screen, WHITE, self.rect, width=3, border_radius=15)  # Border around the button
        
        # Draw the text on the button
        text_surface = font.render(self.text, True, (255, 255, 255))
        screen.blit(text_surface, (self.rect.x + (self.rect.width - text_surface.get_width()) // 2, 
                                  self.rect.y + (self.rect.height - text_surface.get_height()) // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Define actions for buttons
def exit_game():
    pygame.quit()
    sys.exit()

def play_game():
    game_window(WIDTH, HEIGHT)
    # You can add functionality to start the game here

def learn_game():
    learn_window(WIDTH, HEIGHT)
    # You can add functionality to show the tutorial/learn section here

# Create buttons
play_button = Button('Play', 50, 400, 200, 50, GREEN, HOVER_COLOR, play_game)
learn_button = Button('Learn', 300, 400, 200, 50, BLUE, HOVER_COLOR, learn_game)
exit_button = Button('Exit', 550, 400, 200, 50, RED, HOVER_COLOR, exit_game)

# Main Game Loop
running = True
while running:
    screen.fill((255, 255, 255))  # Optional: fill screen with white before drawing background

    # Draw the background image
    screen.blit(background, (0, 0))  # (0, 0) is the position to start drawing the image
    
    # Draw buttons
    play_button.draw(screen)
    learn_button.draw(screen)
    exit_button.draw(screen)

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button.is_clicked(event.pos):
                play_button.action()
            elif learn_button.is_clicked(event.pos):
                learn_button.action()
            elif exit_button.is_clicked(event.pos):
                exit_button.action()

    # Update the screen
    pygame.display.flip()

# Quit the game
pygame.quit()
sys.exit()

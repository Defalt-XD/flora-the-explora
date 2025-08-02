import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge - Level 3")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

GRAPE_WIDTH = 20
GRAPE_HEIGHT = 20
ORANGE_WIDTH = 30
ORANGE_HEIGHT = 30  # Changed fruit size
FRUIT_VEL = 4  # Increased speed

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, grapes, oranges, score):
    WIN.blit(BG, (0, 0))

    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    
    score_text = FONT.render(f"Score: {score}", 1, "white")
    WIN.blit(score_text, (10, 60))
    
    instruction_text = FONT.render("Eat Oranges!", 1, "white")
    WIN.blit(instruction_text, (WIDTH - 230, 10))

    pygame.draw.rect(WIN, "purple", player)

    for grape in grapes:
        pygame.draw.ellipse(WIN, "purple", grape)
    for orange in oranges:
        pygame.draw.ellipse(WIN, "orange", orange)

    pygame.display.update()

def start_level_3():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0

    fruit_add_increment = 1800  # Faster spawn rate
    fruit_count = 0
    
    grapes = []
    oranges = []
    score = 0
    lost = False

    while run:
        fruit_count += clock.tick(60)
        elapsed_time = time.time() - start_time

        if fruit_count > fruit_add_increment:
            for _ in range(2):
                grape_x = random.randint(0, WIDTH - GRAPE_WIDTH)
                orange_x = random.randint(0, WIDTH - ORANGE_WIDTH)
                
                grape = pygame.Rect(grape_x, -GRAPE_HEIGHT, GRAPE_WIDTH, GRAPE_HEIGHT)
                orange = pygame.Rect(orange_x, -ORANGE_HEIGHT, ORANGE_WIDTH, ORANGE_HEIGHT)
                
                grapes.append(grape)
                oranges.append(orange)

            fruit_add_increment = max(500, fruit_add_increment - 50)
            fruit_count = 0

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
                break

        keys = pygame.key.get_pressed()
        if keys[pygame.K_LEFT] and player.x - PLAYER_VEL >= 0:
            player.x -= PLAYER_VEL
        if keys[pygame.K_RIGHT] and player.x + PLAYER_VEL + player.width <= WIDTH:
            player.x += PLAYER_VEL

        for grape in grapes[:]:
            grape.y += FRUIT_VEL
            if grape.y > HEIGHT:
                grapes.remove(grape)
            elif grape.colliderect(player):
                lost = True
                break

        for orange in oranges[:]:
            orange.y += FRUIT_VEL
            if orange.y > HEIGHT:
                oranges.remove(orange)
            elif orange.colliderect(player):
                oranges.remove(orange)
                score += 1

        if lost:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break

        draw(player, elapsed_time, grapes, oranges, score)

    pygame.quit()

if __name__ == "__main__":
    start_level_3()

import pygame
import time
import random
pygame.font.init()

WIDTH, HEIGHT = 800, 600
WIN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Space Dodge - Level 2")

BG = pygame.transform.scale(pygame.image.load("bg.jpeg"), (WIDTH, HEIGHT))

PLAYER_WIDTH = 40
PLAYER_HEIGHT = 60
PLAYER_VEL = 5

APPLE_WIDTH = 20
APPLE_HEIGHT = 20
BANANA_WIDTH = 15
BANANA_HEIGHT = 60
FRUIT_VEL = 3

FONT = pygame.font.SysFont("comicsans", 30)

def draw(player, elapsed_time, apples, bananas, score):
    WIN.blit(BG, (0, 0))
    
    time_text = FONT.render(f"Time: {round(elapsed_time)}s", 1, "white")
    WIN.blit(time_text, (10, 10))
    
    score_text = FONT.render(f"Score: {score}", 1, "white")
    WIN.blit(score_text, (10, 60))
    
    instruction_text = FONT.render("Eat Bananas!", 1, "white")
    WIN.blit(instruction_text, (WIDTH - 230, 10))
    
    pygame.draw.rect(WIN, "purple", player)
    
    for apple in apples:
        pygame.draw.ellipse(WIN, "red", apple)
    for banana in bananas:
        pygame.draw.ellipse(WIN, "yellow", banana)
    
    pygame.display.update()

def start_level_2():
    run = True
    player = pygame.Rect(200, HEIGHT - PLAYER_HEIGHT, PLAYER_WIDTH, PLAYER_HEIGHT)
    clock = pygame.time.Clock()
    start_time = time.time()
    elapsed_time = 0
    
    fruit_add_increment = 2000
    fruit_count = 0
    
    apples = []
    bananas = []
    score = 0
    lost = False

    while run:
        fruit_count += clock.tick(60)
        elapsed_time = time.time() - start_time
        
        if fruit_count > fruit_add_increment:
            for _ in range(2):
                apple_x = random.randint(0, WIDTH - APPLE_WIDTH)
                banana_x = random.randint(0, WIDTH - BANANA_WIDTH)
                
                apple = pygame.Rect(apple_x, -APPLE_HEIGHT, APPLE_WIDTH, APPLE_HEIGHT)
                banana = pygame.Rect(banana_x, -BANANA_HEIGHT, BANANA_WIDTH, BANANA_HEIGHT)
                
                apples.append(apple)
                bananas.append(banana)
            
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
        
        for apple in apples[:]:
            apple.y += FRUIT_VEL
            if apple.y > HEIGHT:
                apples.remove(apple)
            elif apple.colliderect(player):
                lost = True
                break
        
        for banana in bananas[:]:
            banana.y += FRUIT_VEL
            if banana.y > HEIGHT:
                bananas.remove(banana)
            elif banana.colliderect(player):
                bananas.remove(banana)
                score += 1
        
        if lost:
            lost_text = FONT.render("You Lost!", 1, "white")
            WIN.blit(lost_text, (WIDTH/2 - lost_text.get_width()/2, HEIGHT/2 - lost_text.get_height()/2))
            pygame.display.update()
            pygame.time.delay(4000)
            break
        
        draw(player, elapsed_time, apples, bananas, score)
    
    pygame.quit()

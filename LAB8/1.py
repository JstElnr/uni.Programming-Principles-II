import pygame
import random
pygame.init()
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer")
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
player_img = pygame.Surface((40, 60))
player_img.fill(RED)
player = player_img.get_rect(center=(width // 2, height - 100))
player_speed = 5
coin_img = pygame.Surface((20, 20))
coin_img.fill(YELLOW)
coins = []
coin_spawn_time = 0
coin_spawn_interval = 60
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and player.left > 0:
        player.x -= player_speed
    if keys[pygame.K_RIGHT] and player.right < width:
        player.x += player_speed
    coin_spawn_time += 1
    if coin_spawn_time >= coin_spawn_interval:
        coin = coin_img.get_rect(center=(random.randint(20, width - 20), -20))
        coins.append(coin)
        coin_spawn_time = 0
    for coin in coins[:]:
        coin.y += 3
        if coin.colliderect(player):
            coins.remove(coin)
            score += 1
        elif coin.top > height:
            coins.remove(coin)
    screen.fill(WHITE)
    screen.blit(player_img, player)
    for coin in coins:
        screen.blit(coin_img, coin)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (width - score_text.get_width() - 10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
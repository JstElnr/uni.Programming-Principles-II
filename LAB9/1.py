import pygame
import random
pygame.init()
width, height = 400, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Racer")
WHITE = (255, 255, 255)
YELLOW = (255, 255, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
BRONZE = (205, 127, 50)
SILVER = (192, 192, 192)
player_img = pygame.Surface((40, 60))
player_img.fill(BLUE)
player = player_img.get_rect(center=(width // 2, height - 100))
player_speed = 5
coins = []
coin_spawn_time = 0
coin_spawn_interval = 60
enemy_img = pygame.Surface((40, 60))
enemy_img.fill(RED)
enemies = []
enemy_spawn_time = 0
enemy_spawn_interval = 120
enemy_speed = 3
speed_increase_threshold = 5
speed_increase_amount = 0.5
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
        coin_type = random.randint(1, 3)
        if coin_type == 1:
            value = 1
            color = BRONZE
        elif coin_type == 2:
            value = 2
            color = SILVER
        else:
            value = 3
            color = YELLOW
        coin_surface = pygame.Surface((20, 20))
        coin_surface.fill(color)
        coin_rect = coin_surface.get_rect(center=(random.randint(20, width - 20), -20))
        coins.append([coin_rect, value, color, coin_surface])
        coin_spawn_time = 0
    for coin in coins[:]:
        coin[0].y += 3
        if coin[0].colliderect(player):
            coins.remove(coin)
            score += coin[1]
            if score % speed_increase_threshold == 0:
                enemy_speed += speed_increase_amount
        elif coin[0].top > height:
            coins.remove(coin)
    enemy_spawn_time += 1
    if enemy_spawn_time >= enemy_spawn_interval:
        enemy_rect = enemy_img.get_rect(center=(random.randint(30, width - 30), -30))
        enemies.append(enemy_rect)
        enemy_spawn_time = 0
    for enemy in enemies[:]:
        enemy.y += enemy_speed
        if enemy.colliderect(player):
            running = False
        elif enemy.top > height:
            enemies.remove(enemy)
    screen.fill(WHITE)
    screen.blit(player_img, player)
    for coin in coins:
        screen.blit(coin[3], coin[0])
    for enemy in enemies:
        screen.blit(enemy_img, enemy)
    score_text = font.render(f"Score: {score}", True, (0, 0, 0))
    screen.blit(score_text, (width - score_text.get_width() - 10, 10))
    speed_text = font.render(f"Speed: {enemy_speed:.1f}", True, (0, 0, 0))
    screen.blit(speed_text, (10, 10))
    pygame.display.flip()
    clock.tick(60)
pygame.quit()
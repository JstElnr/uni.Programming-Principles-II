import pygame
import random
pygame.init()
width, height = 600, 400
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Snake")
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)
WHITE = (255, 255, 255)
block_size = 20
snake = [(width // 2, height // 2)]
snake_dir = (block_size, 0)
food = (random.randrange(0, width, block_size), random.randrange(0, height, block_size))
speed = 10
level = 1
score = 0
font = pygame.font.Font(None, 36)
clock = pygame.time.Clock()
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and snake_dir != (0, block_size):
                snake_dir = (0, -block_size)
            elif event.key == pygame.K_DOWN and snake_dir != (0, -block_size):
                snake_dir = (0, block_size)
            elif event.key == pygame.K_LEFT and snake_dir != (block_size, 0):
                snake_dir = (-block_size, 0)
            elif event.key == pygame.K_RIGHT and snake_dir != (-block_size, 0):
                snake_dir = (block_size, 0)
    head_x, head_y = snake[0]
    new_head = (head_x + snake_dir[0], head_y + snake_dir[1])
    snake.insert(0, new_head)
    if new_head[0] < 0 or new_head[0] >= width or new_head[1] < 0 or new_head[1] >= height:
        running = False
    if new_head == food:
        score += 1
        while True:
            food = (random.randrange(0, width, block_size), random.randrange(0, height, block_size))
            if food not in snake:
                break
        if score % 3 == 0:
            level += 1
            speed += 2
    else:
        snake.pop()
    if new_head in snake[1:]:
        running = False
    screen.fill(BLACK)
    for segment in snake:
        pygame.draw.rect(screen, GREEN, (segment[0], segment[1], block_size, block_size))
    pygame.draw.rect(screen, RED, (food[0], food[1], block_size, block_size))
    score_text = font.render(f"Score: {score}  Level: {level}", True, WHITE)
    screen.blit(score_text, (10, 10))
    pygame.display.flip()
    clock.tick(speed)
pygame.quit()
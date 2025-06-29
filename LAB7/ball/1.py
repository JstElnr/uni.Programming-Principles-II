import pygame
RADIUS = 25
COLOR = (255, 0, 0)
POS = [640, 360]
SPEED = 20
WIDTH, HEIGHT = 1280, 720
BG_COLOR = (255, 255, 255)
pygame.init()
SCREEN = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Circle")
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    keys = pygame.key.get_pressed()
    POS[0] += (keys[pygame.K_RIGHT] - keys[pygame.K_LEFT]) * SPEED
    POS[1] += (keys[pygame.K_DOWN] - keys[pygame.K_UP]) * SPEED
    POS[0] = max(RADIUS, min(POS[0], WIDTH - RADIUS))
    POS[1] = max(RADIUS, min(POS[1], HEIGHT - RADIUS))
    SCREEN.fill(BG_COLOR)
    pygame.draw.circle(SCREEN, COLOR, POS, RADIUS)
    pygame.display.flip()
    pygame.time.Clock().tick(60)
pygame.quit()

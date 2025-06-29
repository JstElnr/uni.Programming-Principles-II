import pygame
import datetime
import sys
pygame.init()
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("Mickey Clock")
mickey = pygame.transform.scale(pygame.image.load('mickey.png'), (450, 450))
minute = pygame.transform.scale(pygame.image.load('right_hand.png'), (400, 400))
second = pygame.transform.scale(pygame.image.load('left_hand.png'), (400, 400))
def blit(surf, img, pos, angle):
    rotated_img = pygame.transform.rotate(img, -angle)
    rect = rotated_img.get_rect(center=pos)
    surf.blit(rotated_img, rect)
clock = pygame.time.Clock()
while True:
    screen.fill((255, 255, 255))
    screen.blit(mickey, (75, 75))
    now = datetime.datetime.now()
    blit(screen, minute, (300, 300), now.minute * 6 + now.second * 0.1+30)
    blit(screen, second, (300, 300), now.second * 6)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.flip()
    clock.tick(60)
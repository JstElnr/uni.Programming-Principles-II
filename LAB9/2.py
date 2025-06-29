import pygame
import sys
import copy
import random
import time
pygame.init()
scale = 15
score = 0
level = 0
SPEED = 10
display = pygame.display.set_mode((500, 500))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)
white = (255, 255, 255)
class Snake:
    def __init__(self, x_start, y_start):
        self.x = x_start
        self.y = y_start
        self.w = 15
        self.h = 15
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1
    def reset(self):
        self.x = 500 / 2 - scale
        self.y = 500 / 2 - scale
        self.w = 15
        self.h = 15
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1
    def show(self):
        for i in range(self.length):
            pygame.draw.rect(display, red, (self.history[i][0], self.history[i][1], self.w, self.h))
    def check_eaten(self, food_x, food_y):
        if abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale:
            return True
    def check_level(self):
        global level
        if self.length % 5 == 0:
            return True
    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])
    def death(self):
        i = self.length - 1
        while i > 0:
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h and self.length > 2:
                return True
            i -= 1
    def update(self):
        i = self.length - 1
        while i > 0:
            self.history[i] = copy.deepcopy(self.history[i - 1])
            i -= 1
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale
class Food:
    def __init__(self):
        self.x = random.randrange(1, int(500 / scale) - 1) * scale
        self.y = random.randrange(1, int(500 / scale) - 1) * scale
        self.spawn_time = time.time()
    def new_location(self):
        self.x = random.randrange(1, int(500 / scale) - 1) * scale
        self.y = random.randrange(1, int(500 / scale) - 1) * scale
        self.spawn_time = time.time()
    def show(self):
        pygame.draw.rect(display, blue, (self.x, self.y, scale, scale))
    def is_expired(self):
        return time.time() - self.spawn_time > 5
def show_score():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Score: " + str(score), True, white)
    display.blit(text, (scale, scale))
def show_level():
    font = pygame.font.SysFont(None, 20)
    text = font.render("Level: " + str(level), True, white)
    display.blit(text, (90 - scale, scale))
def gameLoop():
    global score
    global level
    global SPEED
    snake = Snake(500 / 2, 500 / 2)
    food = Food()
    last_food_check = time.time()
    while True:
        current_time = time.time()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    pygame.quit()
                    sys.exit()
                if snake.y_dir == 0:
                    if event.key == pygame.K_UP:
                        snake.x_dir = 0
                        snake.y_dir = -1
                    if event.key == pygame.K_DOWN:
                        snake.x_dir = 0
                        snake.y_dir = 1
                if snake.x_dir == 0:
                    if event.key == pygame.K_LEFT:
                        snake.x_dir = -1
                        snake.y_dir = 0
                    if event.key == pygame.K_RIGHT:
                        snake.x_dir = 1
                        snake.y_dir = 0
        display.fill(black)
        snake.show()
        snake.update()
        food.show()
        show_score()
        show_level()
        if food.is_expired():
            food.new_location()
        if snake.check_eaten(food.x, food.y):
            food.new_location()
            score += random.randint(1, 5)
            snake.grow()
        if snake.check_level():
            level += 1
            SPEED += 1
            snake.grow()
        if snake.death():
            score = 0
            level = 0
            font = pygame.font.SysFont(None, 100)
            text = font.render("Game Over!", True, red)
            display.blit(text, (50, 200))
            pygame.display.update()
            time.sleep(3)
            snake.reset()
        if snake.history[0][0] > 500:
            snake.history[0][0] = 0
        if snake.history[0][0] < 0:
            snake.history[0][0] = 500
        if snake.history[0][1] > 500:
            snake.history[0][1] = 0
        if snake.history[0][1] < 0:
            snake.history[0][1] = 500
        pygame.display.update()
        clock.tick(SPEED)
gameLoop()
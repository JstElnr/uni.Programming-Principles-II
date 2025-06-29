import pygame
import sys
import copy
import random
import time
from snake_db import get_or_create_user, get_last_level, save_game_state, close_connection
pygame.init()
scale = 15
score = 0
level = 0
SPEED = 10
paused = False
username = input("username: ")
user_id = get_or_create_user(username)
level = get_last_level(user_id)
SPEED += level
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
        self.x_dir = 1
        self.y_dir = 0
        self.history = [[self.x, self.y]]
        self.length = 1
    def show(self):
        for i in range(self.length):
            pygame.draw.rect(display, red, (self.history[i][0], self.history[i][1], self.w, self.h))
    def check_eaten(self, food_x, food_y):
        return abs(self.history[0][0] - food_x) < scale and abs(self.history[0][1] - food_y) < scale
    def check_level(self):
        return self.length % 5 == 0
    def grow(self):
        self.length += 1
        self.history.append(self.history[self.length - 2])
    def death(self):
        for i in range(1, self.length):
            if abs(self.history[0][0] - self.history[i][0]) < self.w and abs(self.history[0][1] - self.history[i][1]) < self.h:
                return True
        return False
    def update(self):
        for i in range(self.length - 1, 0, -1):
            self.history[i] = copy.deepcopy(self.history[i - 1])
        self.history[0][0] += self.x_dir * scale
        self.history[0][1] += self.y_dir * scale
class Food:
    def __init__(self):
        self.new_location()
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
    global score, level, SPEED, paused
    snake = Snake(500 / 2, 500 / 2)
    food = Food()
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                close_connection()
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_q:
                    close_connection()
                    pygame.quit()
                    sys.exit()
                elif event.key == pygame.K_p:
                    paused = not paused
                    if paused:
                        save_game_state(user_id, level, score, snake.history, (food.x, food.y), direction=sprite_direction(snake))
                if not paused:
                    if snake.y_dir == 0:
                        if event.key == pygame.K_UP:
                            snake.x_dir, snake.y_dir = 0, -1
                        elif event.key == pygame.K_DOWN:
                            snake.x_dir, snake.y_dir = 0, 1
                    if snake.x_dir == 0:
                        if event.key == pygame.K_LEFT:
                            snake.x_dir, snake.y_dir = -1, 0
                        elif event.key == pygame.K_RIGHT:
                            snake.x_dir, snake.y_dir = 1, 0
        if not paused:
            display.fill(black)
            snake.update()
            snake.show()
            food.show()
            show_score()
            show_level()
            if food.is_expired():
                food.new_location()
            if snake.check_eaten(food.x, food.y):
                food.new_location()
                score += random.randint(1, 5)
                grow_pending = True
            else:
                grow_pending = False
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
            if snake.history[0][0] >= 500:
                snake.history[0][0] = 0
            elif snake.history[0][0] < 0:
                snake.history[0][0] = 500
            if snake.history[0][1] >= 500:
                snake.history[0][1] = 0
            elif snake.history[0][1] < 0:
                snake.history[0][1] = 500
            if grow_pending:
                snake.grow()
            pygame.display.update()
            clock.tick(SPEED)
def sprite_direction(snake):
    if snake.x_dir == 1:
        return "RIGHT"
    elif snake.x_dir == -1:
        return "LEFT"
    elif snake.y_dir == 1:
        return "DOWN"
    elif snake.y_dir == -1:
        return "UP"
gameLoop()

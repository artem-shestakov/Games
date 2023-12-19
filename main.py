import pygame, sys
from models.game import Game
from pygame.math import Vector2

FRAMERATE = 60
SECTOR = 40
SECTOR_COUNT=20
WIDTH = HEIGHT = SECTOR * SECTOR_COUNT

pygame.mixer.pre_init()
pygame.init()
display = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()

UPDATE = pygame.USEREVENT
pygame.time.set_timer(UPDATE, 150)

game = Game(display, SECTOR, SECTOR_COUNT)

# game loop
while True:
    # event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        if event.type == UPDATE:
            game.update()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                if game.snake.direction.y != 1:
                    game.snake.direction = Vector2( 0,-1)
            if event.key == pygame.K_DOWN:
                if game.snake.direction.y != -1:
                    game.snake.direction = Vector2(0,1)
            if event.key == pygame.K_RIGHT:
                if game.snake.direction.x != -1:
                    game.snake.direction = Vector2(1,0)
            if event.key == pygame.K_LEFT:
                if game.snake.direction.x != 1 and game.snake.direction != Vector2(0,0):
                    game.snake.direction = Vector2(-1,0)

    display.fill((175,215,70))
    game.draw_models()

    pygame.display.update()
    clock.tick(FRAMERATE)
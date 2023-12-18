import pygame, sys
from .fruit import Fruit
from .snake import Snake

class Game():
    def __init__(self, surface, sector_size, display_size):
        self.surface = surface
        self.display_size = display_size
        self.snake = Snake(sector_size)
        self.fruit = Fruit(sector_size, display_size)

    def update(self):
        self.snake.move()
        self.if_hit_fruit()
        self.is_fail()

    def draw_models(self):
        self.fruit.draw(self.surface)
        self.snake.draw_body(self.surface)
    
    def if_hit_fruit(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.recreate(self.display_size)
            self.snake.grow()

    def is_fail(self):
        if not 0 <= self.snake.body[0].x < self.display_size or not 0 <= self.snake.body[0].y < self.display_size:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()

    def game_over(self):
        pygame.quit()
        sys.exit(0)
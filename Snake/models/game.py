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

    def draw_models(self):
        self.fruit.draw(self.surface)
        self.snake.draw_body(self.surface)
    
    def if_hit_fruit(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.recreate(self.display_size)
            self.snake.grow()
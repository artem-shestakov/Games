import pygame, sys
from .fruit import Fruit
from .snake import Snake

class Game():
    def __init__(self, surface: pygame.Surface, sector_size, display_size):
        self.surface = surface
        self.display_size = display_size
        self.sector_size = sector_size
        self.snake = Snake(self.sector_size)
        self.fruit = Fruit(self.sector_size, self.display_size)
        self.score = 0
        self.font = pygame.font.Font('fonts/PoetsenOne-Regular.ttf', 25)

    def update(self):
        self.snake.move()
        self.if_hit_fruit()
        self.is_fail()

    def draw_bg(self):
        grass_clr = (167,209,61)
        for row in range(self.display_size):
            if row % 2 == 0:
                for col in range(self.display_size):
                    if col % 2 == 0:
                        grass_rect = pygame.Rect(
                            col * self.sector_size,
                            row * self.sector_size,
                            self.sector_size, self.sector_size
                        )
                        pygame.draw.rect(self.surface, grass_clr, grass_rect)
            else:
                for col in range(self.display_size):
                    if col % 2 != 0:
                        grass_rect = pygame.Rect(
                            col * self.sector_size,
                            row * self.sector_size,
                            self.sector_size, self.sector_size
                        )
                        pygame.draw.rect(self.surface, grass_clr, grass_rect)

    def draw_models(self):
        self.draw_bg()
        self.fruit.draw(self.surface)
        self.snake.draw_body(self.surface)
        self.draw_score()
    
    def if_hit_fruit(self):
        if self.fruit.position == self.snake.body[0]:
            self.fruit.recreate(self.display_size)
            self.snake.grow()
            self.score += 1
            self.snake.play_crunch()
        
        for body in self.snake.body[1:]:
            if body == self.fruit.position:
                self.fruit.recreate(self.display_size)

    def is_fail(self):
        if not 0 <= self.snake.body[0].x < self.display_size or not 0 <= self.snake.body[0].y < self.display_size:
            self.game_over()
        for block in self.snake.body[1:]:
            if block == self.snake.body[0]:
                self.game_over()
    
    def draw_score(self):
        score_surface = self.font.render(str(self.score), True, (55,75,15))
        score_rect = score_surface.get_rect(center=(self.sector_size * self.display_size - 60, self.sector_size * self.display_size - 40))
        fruit_rect = self.fruit.apple.get_rect(midright=(score_rect.left, score_rect.centery))

        self.surface.blit(score_surface, score_rect)
        self.surface.blit(self.fruit.apple, fruit_rect)

    def restart(self):
        self.snake.restart()
        self.fruit.recreate(self.display_size)
        self.score = 0

    def game_over(self):
        self.restart()

import pygame
from pygame.math import Vector2
from pygame import Rect


class Snake():
    def __init__(self, body_size):
        self.size = body_size
        self.body = [Vector2(5,10),Vector2(6,10),Vector2(7,10)]
        self.direction = Vector2(1,0)
    
    def draw_body(self, surface):
        for block in self.body:
            rect = Rect(block.x * self.size, block.y * self.size, self.size, self.size)
            pygame.draw.rect(surface, (125,165,115), rect)

    def move(self):
        body_clone = self.body[:-1]
        body_clone.insert(0,body_clone[0] + self.direction)
        self.body = body_clone

    def grow(self):
        self.body.append(self.body[-1])
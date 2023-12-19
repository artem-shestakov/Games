from pygame.math import Vector2
from pygame import Rect
import pygame, random


class Fruit:
    def __init__(self, fruit_size, display_size):
        self.size = fruit_size
        self.recreate(display_size)
        self.apple = pygame.image.load('sprites/apple.png').convert_alpha()
        
    def draw(self, surface):
        rect = Rect(self.position.x * self.size, self.position.y * self.size,self.size,self.size)
        surface.blit(self.apple, rect)

    def recreate(self, display_size):
        self.x = random.randint(0, display_size - 1)
        self.y = random.randint(0, display_size - 1)
        self.position = Vector2(self.x, self.y)
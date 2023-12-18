import pygame
from pygame.math import Vector2
from pygame import Rect


class Snake():
    def __init__(self, body_size):
        self.size = body_size
        self.body = [Vector2(5,10),Vector2(4,10),Vector2(3,10)]
        self.direction = Vector2(1,0)

        # Head
        self.head_up = pygame.image.load('sprites/head_up.png').convert_alpha()
        self.head_down = pygame.image.load('sprites/head_down.png').convert_alpha()
        self.head_left = pygame.image.load('sprites/head_left.png').convert_alpha()
        self.head_right = pygame.image.load('sprites/head_right.png').convert_alpha()
        # Tail
        self.tail_up = pygame.image.load('sprites/tail_up.png').convert_alpha()
        self.tail_down = pygame.image.load('sprites/tail_down.png').convert_alpha()
        self.tail_left = pygame.image.load('sprites/tail_left.png').convert_alpha()
        self.tail_right = pygame.image.load('sprites/tail_right.png').convert_alpha()
        # Body
        self.body_bl = pygame.image.load('sprites/body_bl.png').convert_alpha()
        self.body_br = pygame.image.load('sprites/body_br.png').convert_alpha()
        self.body_tl = pygame.image.load('sprites/body_tl.png').convert_alpha()
        self.body_tr = pygame.image.load('sprites/body_tr.png').convert_alpha()
        self.body_horizontal = pygame.image.load('sprites/body_horizontal.png').convert_alpha()
        self.body_vertical = pygame.image.load('sprites/body_vertical.png').convert_alpha()
    
    def draw_body(self, surface):
        for block in self.body:
            rect = Rect(block.x * self.size, block.y * self.size, self.size, self.size)
            pygame.draw.rect(surface, (0,225,0), rect)

    def move(self):
        body_clone = self.body[:-1]
        body_clone.insert(0,body_clone[0] + self.direction)
        self.body = body_clone

    def grow(self):
        self.body.append(self.body[-1])
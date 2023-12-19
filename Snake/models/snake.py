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
    
    def draw_body(self, surface: pygame.Surface):
        self.set_head_graphics()
        self.set_tail_graphics()

        for index, block in enumerate(self.body):
            rect = Rect(block.x * self.size, block.y * self.size, self.size, self.size)
            
            if index == 0:
                surface.blit(self.head,rect)
            elif index == len(self.body) - 1:
                surface.blit(self.tail,rect)
            else:
                prev_block_vector = self.body[index+1] - block
                next_block_vector = self.body[index-1] - block
                if next_block_vector.x == prev_block_vector.x:
                    surface.blit(self.body_vertical, rect)
                elif next_block_vector.y == prev_block_vector.y:
                    surface.blit(self.body_horizontal, rect)
                else:
                    if prev_block_vector.x == -1 and next_block_vector.y == -1 or prev_block_vector.y == -1 and next_block_vector.x == -1:
                        surface.blit(self.body_tl, rect)
                    elif prev_block_vector.y == -1 and next_block_vector.x == 1 or prev_block_vector.x == 1 and next_block_vector.y == -1:
                        surface.blit(self.body_tr, rect)
                    elif prev_block_vector.y == 1 and next_block_vector.x == -1 or prev_block_vector.x == -1 and next_block_vector.y == 1:
                        surface.blit(self.body_bl, rect)
                    else:
                        surface.blit(self.body_br, rect)


    def set_head_graphics(self):
        head_direction = self.body[1] - self.body[0]
        if head_direction == Vector2(1,0): self.head = self.head_left
        elif head_direction == Vector2(-1,0): self.head = self.head_right
        elif head_direction == Vector2(0,1): self.head = self.head_up
        elif head_direction == Vector2(0,-1): self.head = self.head_down

    def set_tail_graphics(self):
        tail_direction = self.body[-2] - self.body[-1]
        if tail_direction == Vector2(1,0): self.tail = self.tail_left
        elif tail_direction == Vector2(-1,0): self.tail = self.tail_right
        elif tail_direction == Vector2(0,1): self.tail = self.tail_up
        elif tail_direction == Vector2(0,-1): self.tail = self.tail_down

    def move(self):
        body_clone = self.body[:-1]
        body_clone.insert(0,body_clone[0] + self.direction)
        self.body = body_clone

    def grow(self):
        self.body.append(self.body[-1])
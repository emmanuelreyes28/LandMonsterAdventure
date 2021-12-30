import pygame
import random


class Obstacle(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.x = x
        self.y = y
        self.speed = 5
        self.sprites = []
        for i in range(1, 5):
            self.sprites.append(pygame.transform.scale(
                pygame.image.load("spike-%s.png" % i), (25, 50)))
        self.image = random.choice(self.sprites)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def update(self):
        self.x -= self.speed
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,  self.y)
        # if self.rect.x <= -10:
        #     self.kill()
        # self.current_sprite += 1
        # if self.current_sprite >= len(self.sprites):
        #     self.current_sprite = 0

        # self.image = self.sprites[self.current_sprite]

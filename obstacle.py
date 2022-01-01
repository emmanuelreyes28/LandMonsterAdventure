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
        self.rect = self.rect.inflate(-10, -10)
        self.rect.center = (x, y)
        # create hitbox for collision detection
        self.hitbox = pygame.rect.Rect((0, 0), (25, 40))
        self.hitbox.midbottom = self.rect.midbottom

    def update(self, screen):
        pygame.draw.rect(screen, (0, 0, 0), self.hitbox, 1)
        # obstacle moves to the left and off the screen
        self.x -= self.speed
        # update hitbox position to move with obstacle
        self.hitbox.midbottom = self.rect.midbottom
        self.rect = self.image.get_rect()
        self.rect.center = (self.x,  self.y)
        if self.rect.x <= -10:
            self.kill()

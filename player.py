import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, x, y):
        super().__init__()
        self.animate = False
        self.jumping = False
        self.jump_power = 12
        self.sprites = []  # array of sprite images
        # append 8 sprite images into array of sprites
        for i in range(1, 9):
            # flip image horizontally and scale to fit screen
            self.sprites.append(pygame.transform.scale(pygame.transform.flip(
                pygame.image.load("idle-%s.png" % i), True, False), (50, 50)))
        self.current_sprite = 0
        self.image = self.sprites[self.current_sprite]
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def animated(self):
        self.animate = True

    def update(self, anim_speed):
        if self.animate:
            # set sprite image for desired amount of frames
            self.current_sprite += anim_speed
            # if reach end of the array start from first sprite
            if int(self.current_sprite) >= len(self.sprites):
                self.current_sprite = 0
                self.animate = False

        # set sprite image
        self.image = self.sprites[int(self.current_sprite)]
        self.jump()

    def jump(self):
        keystate = pygame.key.get_pressed()

        if not self.jumping and keystate[pygame.K_SPACE]:
            self.jumping = True

        # avoid player from double jumping, must be touching ground to jump again
        if self.jumping:
            self.rect.y -= self.jump_power
            self.jump_power -= 1
            if self.jump_power < -12:
                self.jumping = False
                self.jump_power = 12

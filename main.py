import pygame
from player import Player

pygame.init()
clock = pygame.time.Clock()

SCREEN_WIDTH = 500
SCREEN_HEIGHT = 250

SCREEN = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

# background
bg = pygame.transform.scale(pygame.image.load(
    "full-background.png"), (SCREEN_WIDTH, SCREEN_HEIGHT))
bg_x = 0

player = Player(50, 195)
player_group = pygame.sprite.Group()
player_group.add(player)


while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.display.quit()
            pygame.quit()
            quit()

    # screen scroll
    rel_x = bg_x % bg.get_rect().width
    SCREEN.blit(bg, (rel_x - bg.get_rect().width, 0))
    if rel_x < SCREEN_WIDTH:
        SCREEN.blit(bg, (rel_x, 0))
    bg_x -= 1

    # draw player
    player_group.draw(SCREEN)
    player.animated()
    player_group.update(0.20)
    pygame.display.update()

    clock.tick(60)

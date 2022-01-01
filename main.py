import pygame
from obstacle import Obstacle
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
player_group = pygame.sprite.GroupSingle()
player_group.add(player)

obstacle_group = pygame.sprite.Group()

timer = 0
spawn = False
instantiate_time = 1000

# callback function for collision detection


def collided(sprite, other):
    return sprite.hitbox.colliderect(other.hitbox)


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

    # check for collisions
    if pygame.sprite.spritecollide(player_group.sprite, obstacle_group, False, collided):
        print("Colllided")

    # spawn obstacles every 1 second
    if pygame.time.get_ticks() - timer >= instantiate_time:
        spawn = True

    if spawn:
        obstacle = Obstacle(SCREEN_WIDTH, 195)
        obstacle_group.add(obstacle)
        timer = pygame.time.get_ticks()
        spawn = False

    # draw player
    player_group.draw(SCREEN)
    player.animated()
    player_group.update(0.20, SCREEN)  # get rid of screen arg

    # draw obstacles
    obstacle_group.draw(SCREEN)
    obstacle_group.update(SCREEN)  # get rid of screen arg

    clock.tick(60)
    pygame.display.update()

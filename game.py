import pygame

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test project")

hero = pygame.image.load("hero.png")
hero_rect = hero.get_rect()
hero_rect.x = window_size[0] / 2 - hero_rect[2] / 2
hero_rect.y = window_size[1] - hero_rect[3] - 20

dragon = pygame.image.load("dragon.png")
dragon_rect = dragon.get_rect()

monster = pygame.image.load("monster.png")
monster = pygame.transform.scale(monster, (64, 64))
monster_rect = monster.get_rect()

hero_speed = 1
monsters_speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # if hero_rect.colliderect(enemy_rect):
    #     print("collide")

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] & hero_rect.x > 0:
        hero_rect.x -= hero_speed
    if keys[pygame.K_RIGHT] & hero_rect.x < window_size[0] - hero_rect[2]:
        hero_rect.x += hero_speed

    screen.fill((221, 216, 206))
    screen.blit(hero, hero_rect)
    screen.blit(dragon, dragon_rect)
    pygame.display.flip()

pygame.quit()

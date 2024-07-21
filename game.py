import pygame
import random
import time
import math


def wait_for_key():
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
            elif event.type == pygame.KEYDOWN:
                waiting = False


pygame.init()
clock = pygame.time.Clock()
FPS = 60
time_of_last_enemy_generation = time.time()
start_time = time.time()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test project")

pygame.font.init()
font = pygame.font.SysFont('Arial', 30)  # You can also load a font file using pygame.font.Font()

# Render the text
enemies_bypassed = 0
text_surface = font.render(f'Enemies bypassed: {enemies_bypassed}', True, (0, 0, 0))  # Black color
# Get the rect of the text surface and position it
text_rect = text_surface.get_rect(topleft=(20, 5))  # Center of the screen
text_surface_2 = font.render(f'Time passed: {round(-start_time + time.time(), 1)}', True, (0, 0, 0))  # Black color
# Get the rect of the text surface and position it
text_rect_2 = text_surface.get_rect(topleft=(window_size[0] - 250, 5))  # Center of the screen

hero = pygame.image.load("hero.png")
hero_rect = hero.get_rect()
hero_rect.x = window_size[0] / 2 - hero_rect[2] / 2
hero_rect.y = window_size[1] - hero_rect[3] - 20

hero_speed = 7
enemies_speed = 1
enemies_generation_interval = 3

enemies = []
enemies_rect = []

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    keys = pygame.key.get_pressed()
    if keys[pygame.K_LEFT] and hero_rect.x > 0:
        hero_rect.x -= hero_speed
    if keys[pygame.K_RIGHT] and hero_rect.x < window_size[0] - hero_rect[2]:
        hero_rect.x += hero_speed
    if keys[pygame.K_UP] and hero_rect.y > 200:
        hero_rect.y -= hero_speed
    if keys[pygame.K_DOWN] and hero_rect.y < window_size[1] - hero_rect[3]:
        hero_rect.y += hero_speed

    # Enemy generation
    enemies_generation_interval = 15 / (enemies_bypassed + 5) + 0.2

    if time.time() - time_of_last_enemy_generation > enemies_generation_interval:
        enemies.append(pygame.image.load(random.choice(["dragon.png", "monster.png"])))
        enemies_rect.append(enemies[-1].get_rect())
        enemies_rect[-1].x = random.randint(0, window_size[0] - enemies_rect[-1][2])
        enemies_rect[-1].y = 24
        time_of_last_enemy_generation = time.time()

    # Enemy motion
    if enemies_bypassed > 0:
        enemies_speed = 1 + math.log10(enemies_bypassed)

    enemies_to_remove = []
    for i, enemy_rect in enumerate(enemies_rect):
        enemy_rect.y += enemies_speed
        if enemy_rect.y > window_size[1] - enemy_rect[3] / 2:
            enemies_to_remove.append(i)
    for i in reversed(enemies_to_remove):
        del enemies[i]
        del enemies_rect[i]
    enemies_bypassed += len(enemies_to_remove)

    # Collisions check
    for enemy_rect in enemies_rect:
        if enemy_rect.colliderect(hero_rect):
            text_surface_3 = font.render(f'GAME OVER!', True,(0, 0, 0))  # Black color
            text_rect_3 = text_surface.get_rect(center=(window_size[0]/2, window_size[1]/2))  # Center of the screen
            text_surface_4 = font.render(f'You survived {round(-start_time + time.time(), 0)} seconds and bypassed {enemies_bypassed} enemies.', True,
                                         (0, 0, 0))  # Black color
            # Get the rect of the text surface and position it
            text_rect_4 = text_surface.get_rect(center=(window_size[0] / 4, window_size[1] / 2 + 100))  # Center of the screen
            text_surface_5 = font.render(f'Press any key to exit', True, (0, 0, 0))  # Black color
            text_rect_5 = text_surface.get_rect(
                center=(window_size[0] / 2, window_size[1] / 2 - 200))  # Center of the screen
            screen.fill((221, 216, 206))
            screen.blit(text_surface_3, text_rect_3)
            screen.blit(text_surface_4, text_rect_4)
            screen.blit(text_surface_5, text_rect_5)
            pygame.display.flip()
            wait_for_key()
            running = False

    text_surface = font.render(f'Enemies bypassed: {enemies_bypassed}', True, (0, 0, 0))  # Black color
    # Get the rect of the text surface and position it
    text_rect = text_surface.get_rect(topleft=(20, 5))  # Center of the screen
    text_surface_2 = font.render(f'Time passed: {round(-start_time + time.time(), 1)}', True, (0, 0, 0))  # Black color
    # Get the rect of the text surface and position it
    text_rect_2 = text_surface.get_rect(topleft=(window_size[0] - 250, 5))  # Center of the screen

    screen.fill((221, 216, 206))
    screen.blit(text_surface, text_rect)
    screen.blit(text_surface_2, text_rect_2)
    screen.blit(hero, hero_rect)
    for enemy, enemy_rect in zip(enemies, enemies_rect):
        screen.blit(enemy, enemy_rect)
    pygame.display.flip()
    clock.tick(FPS)

# pygame.quit()

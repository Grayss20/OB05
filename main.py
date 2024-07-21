import pygame

pygame.init()

window_size = (800, 600)
screen = pygame.display.set_mode(window_size)
pygame.display.set_caption("Test project")

image = pygame.image.load("image.png")
image = pygame.transform.scale(image, (70, 50))
image_rect = image.get_rect()
image_2 = pygame.image.load("kilka.png")
image_2 = pygame.transform.scale(image_2, (70, 50))
image_rect_2 = image_2.get_rect()

# speed = 1

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.MOUSEMOTION:
            mouseX, mouseY = event.pos
            image_rect.x = mouseX - 35
            image_rect.y = mouseY - 25
    if image_rect.colliderect(image_rect_2):
        print("collide")


    # keys = pygame.key.get_pressed()
    # if keys[pygame.K_LEFT]:
    #     image_rect.x -= speed
    # if keys[pygame.K_RIGHT]:
    #     image_rect.x += speed
    # if keys[pygame.K_UP]:
    #     image_rect.y -= speed
    # if keys[pygame.K_DOWN]:
    #     image_rect.y += speed

    screen.fill((0, 0, 0))
    screen.blit(image, image_rect)
    screen.blit(image_2, image_rect_2)
    pygame.display.flip()

pygame.quit()
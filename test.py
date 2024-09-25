import pygame

pygame.init()
winH = 800
winW = 1400
screen = pygame.display.set_mode((winW, winH))
pygame.display.set_caption("Test")
playerX = 640
playerY = 340
w = 100
h = 100
run = True
while run:
    vel = 0.5
    screen.fill("black")
    pygame.draw.rect(screen, "magenta", pygame.Rect(playerX, playerY, w, h))

# Player movement
    keys = pygame.key.get_pressed()
    if (keys[pygame.K_LEFT] or keys[pygame.K_RIGHT]) and playerX > vel:
        if keys[pygame.K_DOWN] or keys[pygame.K_UP]:
            vel *= 0.7
            print(vel)
    if keys[pygame.K_a] and playerX > vel:
        playerX -= vel
    if keys[pygame.K_d] and playerX < winW - h:
        playerX += vel
    if keys[pygame.K_w] and playerY > vel:
        playerY -= vel
    if keys[pygame.K_s] and playerY < winH - h:
        playerY += vel
    
# Quit button
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
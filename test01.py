import pygame

pygame.init()

winWidth = 1800
winHeight = 1000
screen = pygame.display.set_mode((winWidth, winHeight))

playerHeight = 200
playerThickness = 35

player1PosX = 0
player1PosY = 425
player2PosX = 1800 - playerThickness
player2PosY = 425

run = True

while run:
    screen.fill("black")
# Drawing the objects on the screen
    pygame.draw.rect(screen, "white", pygame.Rect(player1PosX, player1PosY, playerThickness, playerHeight))
    pygame.draw.rect(screen, "white", pygame.Rect(player2PosX, player2PosY, playerThickness, playerHeight))
    pygame.draw.rect(screen, "white", pygame.Rect(player2PosX, player2PosY, playerThickness, playerHeight))
    
# Quit Mechanic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()
pygame.quit()
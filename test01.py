import pygame

pygame.init()

winWidth = 1800
winHeight = 1000
screen = pygame.display.set_mode((winWidth, winHeight))

playerHeight = 250
playerThickness = 35

player1PosX = 0
player1PosY = 425
player2PosX = 1800 - playerThickness
player2PosY = 425

ballPosX = 875
ballPosY = 475
run = True

while run:

    
    screen.fill("black")
    # Getting the time
    time = pygame.time.get_ticks()
    clock = pygame.time.Clock()
    dt = clock.tick(60) * 0.001 * 144
    print(dt)
    time = time/1000

    # Drawing the objects on the screen
    pygame.draw.rect(screen, "white", pygame.Rect(player1PosX, player1PosY, playerThickness, playerHeight))
    pygame.draw.rect(screen, "white", pygame.Rect(player2PosX, player2PosY, playerThickness, playerHeight))
    pygame.draw.rect(screen, "red", pygame.Rect(ballPosX, ballPosY, 50, 50))

    # Player Movement Mechanic

    # Quit Mechanic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
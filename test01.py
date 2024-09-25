import pygame

pygame.init()

winWidth = 1800
winHeight = 1000
screen = pygame.display.set_mode((winWidth, winHeight))

playerHeight = 250
playerThickness = 35

player1Pos = pygame.Vector2(0, (winHeight - playerHeight)/2)
player2Pos = pygame.Vector2(winWidth - playerThickness, (winHeight - playerHeight)/2)

ballPosX = 875
ballPosY = 475
run = True

while run:

    
    screen.fill("black")
    # Getting the delta time
    clock = pygame.time.Clock()
    dt = clock.tick() * 0.001
    print(dt)

    # Drawing the objects on the screen
    pygame.draw.rect(screen, "white", pygame.Rect(player1Pos.x, player1Pos.y, playerThickness, playerHeight))
    pygame.draw.rect(screen, "white", pygame.Rect(player2Pos.x, player2Pos.y, playerThickness, playerHeight))
    pygame.draw.rect(screen, "red", pygame.Rect(ballPosX, ballPosY, 50, 50))

    # Player Movement Mechanic

    # Quit Mechanic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
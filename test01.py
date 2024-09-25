import pygame

pygame.init()

winWidth = 1400
winHeight = 800
screen = pygame.display.set_mode((winWidth, winHeight))

playerHeight = 180
playerThickness = 35

player1Pos = pygame.Vector2(20, (winHeight - playerHeight)/2)
player2Pos = pygame.Vector2(winWidth - playerThickness - 20, (winHeight - playerHeight)/2)

ballHeight = 50
ballWidth = 50
ballPos = pygame.Vector2((winWidth - ballWidth)/2, (winHeight - ballHeight)/2)
ballDirection = pygame.Vector2(1, 1)
ballVel = 5
ballVelY = 1

playerAccelRate = 2
friction = .8
vel1 = 0
vel2 = 0

 # Ball Behaviour

def ballMovement(ballX, ballY, ballSpeed, ballSpeedY, ballDirectionX, ballDirectionY):
    if ballDirectionX == 1 and ballX < winWidth - ballWidth:
        ballX += ballSpeed
    elif ballDirectionX == 1 and ballX >= winWidth - ballWidth:
        ballDirectionX *= -1
    if ballDirectionY == 1 and ballY > 0:
        ballY -= ballSpeedY
    elif ballDirectionY == 1 and ballY <= 0:
        ballDirectionY *= -1
    if ballDirectionX == -1 and ballX > 0:
        ballX -= ballSpeed
    elif ballDirectionX == -1 and ballX <= 0:
        ballDirectionX *= -1
    if ballDirectionY == -1 and ballY < winHeight - ballHeight:
        ballY += ballSpeedY
    elif ballDirectionY == -1 and ballY >= winHeight - ballHeight:
        ballDirectionY *= -1
    return ballX, ballY, ballDirectionX, ballDirectionY

# Main Game loop --->

run = True
while run:
    
    screen.fill("black")
    # Getting the delta time
    clock = pygame.time.Clock()
    dt = clock.tick(60) * 0.001 * 60

    # Drawing the objects on the screen
    pygame.draw.rect(screen, "white", pygame.Rect(player1Pos.x, player1Pos.y, playerThickness, playerHeight))
    pygame.draw.rect(screen, "white", pygame.Rect(player2Pos.x, player2Pos.y, playerThickness, playerHeight))
    pygame.draw.rect(screen, "red", pygame.Rect(ballPos.x, ballPos.y, ballWidth, ballHeight))


    # Ball Behaviour

    ballPos.x, ballPos.y, ballDirection.x, ballDirection.y = ballMovement(ballPos.x, ballPos.y, ballVel, ballVelY, ballDirection.x, ballDirection.y)


    # Player Movement Mechanic
    accel1 = 0
    accel2 = 0
    keys = pygame.key.get_pressed()
    if keys[pygame.K_w] and player1Pos.y > 0:
        accel1 -= playerAccelRate
    if keys[pygame.K_s] and player1Pos.y < winHeight - playerHeight:
        accel1 += playerAccelRate
    if keys[pygame.K_UP] and player2Pos.y > 0:
        accel2 -= playerAccelRate
    if keys[pygame.K_DOWN] and player2Pos.y < winHeight - playerHeight:
        accel2 += playerAccelRate
    accel1 += vel1 * friction
    accel2 += vel2 * friction
    vel1 = accel1 * dt
    vel2 = accel2 * dt
    player1Pos.y += vel1 * dt + accel1/2 * (dt*dt)
    player2Pos.y += vel2 * dt + accel2/2 * (dt*dt)
    # Player 2 Constraints
    if player1Pos.y >= winHeight - playerHeight:
        player1Pos.y = winHeight - playerHeight
    if player1Pos.y <= 0:
        player1Pos.y = 0
    # Player 2 Constraints
    if player2Pos.y >= winHeight - playerHeight:
        player2Pos.y = winHeight - playerHeight
    if player2Pos.y <= 0:
        player2Pos.y = 0

    # Quit Mechanic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    pygame.display.update()

pygame.quit()
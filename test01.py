import pygame

pygame.init()

winWidth = 1400
winHeight = 800
screen = pygame.display.set_mode((winWidth, winHeight))

playerSize = pygame.Vector2(35, 180)

player1Pos = pygame.Vector2(20, (winHeight - playerSize.y)/2)
player2Pos = pygame.Vector2(winWidth - playerSize.x - 20, (winHeight - playerSize.y)/2)

ballRadius = 30
ballPos = pygame.Vector2((winWidth)/2, (winHeight)/2)
ballDirection = pygame.Vector2(1, 1)
ballSpeed = pygame.Vector2(10, 10)

playerAccelRate = 2
friction = .8
vel1 = 0
vel2 = 0

scoreP1 = 0
scoreP2 = 0
run = True

gameIsRunning = False
# Text
font = pygame.font.Font('gameFont.ttf', 42)

# Ball Behaviour
def ballMovement(ballX, ballY, ballSpeed, ballSpeedY, ballDirectionX, ballDirectionY, scoreP1, scoreP2):
    if ballDirectionX == 1 and ballX < winWidth - ballRadius:
        ballX += ballSpeed
    elif ballDirectionX == 1 and ballX >= winWidth - ballRadius:
        ballDirectionX *= -1
        scoreP1 += 1
        ballX = winWidth/2
        ballY = winHeight/2

    if ballDirectionX == -1 and ballX > ballRadius:
        ballX -= ballSpeed
    elif ballDirectionX == -1 and ballX <= ballRadius:
        ballDirectionX *= -1
        scoreP2 += 1
        ballX = winWidth/2
        ballY = winHeight/2

    if ballDirectionY == 1 and ballY > ballRadius:
        ballY -= ballSpeedY
    elif ballDirectionY == 1 and ballY <= ballRadius:
        ballDirectionY *= -1
        
    if ballDirectionY == -1 and ballY < winHeight - ballRadius:
        ballY += ballSpeedY
    elif ballDirectionY == -1 and ballY >= winHeight - ballRadius:
        ballDirectionY *= -1

    return ballX, ballY, ballDirectionX, ballDirectionY, scoreP1, scoreP2

def BallIsColliding(playerPosition, playerSize, ballRadius, ballPosition):
    collisionX = max(playerPosition.x, min(ballPosition.x, playerPosition.x + playerSize.x))
    collisionY = max(playerPosition.y, min(ballPosition.y, playerPosition.y + playerSize.y))

    distanceX = ballPosition.x - collisionX
    distanceY = ballPosition.y - collisionY

    return (distanceX ** 2 + distanceY ** 2) <= (ballRadius ** 2)

# Main Game loop --->

while run:
    
    screen.fill("black")



    if gameIsRunning:
        # Getting the delta time
        clock = pygame.time.Clock()
        dt = clock.tick(60) * 0.001 * 60

    # Drawing the objects on the screen
        pygame.draw.circle(screen, "white", (winWidth/2, winHeight/2), 150)
        pygame.draw.circle(screen, "black", (winWidth/2, winHeight/2), 150 - 4)

        pygame.draw.rect(screen, "white", pygame.Rect(winWidth/2 - 2, 0, 4, winHeight))

        pygame.draw.rect(screen, "white", pygame.Rect(player1Pos.x, player1Pos.y, playerSize.x, playerSize.y))
        pygame.draw.rect(screen, "white", pygame.Rect(player2Pos.x, player2Pos.y, playerSize.x, playerSize.y))
        pygame.draw.circle(screen, "red", ballPos, ballRadius)

        # Ball Behaviour
        ballPos.x, ballPos.y, ballDirection.x, ballDirection.y, scoreP1, scoreP2 = ballMovement(ballPos.x, ballPos.y, ballSpeed.x, ballSpeed.y, ballDirection.x, ballDirection.y, scoreP1, scoreP2)
        
        if BallIsColliding(player1Pos, playerSize, ballRadius, ballPos):
            ballPos.x = player1Pos.x + playerSize.x + ballRadius
            ballDirection.x *= -1
        if BallIsColliding(player2Pos, playerSize, ballRadius, ballPos):
            ballPos.x = player2Pos.x - ballRadius
            ballDirection.x *= -1

        # Player Movement Mechanic
        accel1 = 0
        accel2 = 0
        keys = pygame.key.get_pressed()
        if keys[pygame.K_w] and player1Pos.y > 0:
            accel1 -= playerAccelRate
        if keys[pygame.K_s] and player1Pos.y < winHeight - playerSize.y:
            accel1 += playerAccelRate
        if keys[pygame.K_UP] and player2Pos.y > 0:
            accel2 -= playerAccelRate
        if keys[pygame.K_DOWN] and player2Pos.y < winHeight - playerSize.y:
            accel2 += playerAccelRate
        accel1 += vel1 * friction
        accel2 += vel2 * friction
        vel1 = accel1 * dt
        vel2 = accel2 * dt
        player1Pos.y += vel1 * dt + accel1/2 * (dt*dt)
        player2Pos.y += vel2 * dt + accel2/2 * (dt*dt)
        # Player 2 Constraints
        if player1Pos.y >= winHeight - playerSize.y:
            player1Pos.y = winHeight - playerSize.y
        if player1Pos.y <= 0:
            player1Pos.y = 0
        # Player 2 Constraints
        if player2Pos.y >= winHeight - playerSize.y:
            player2Pos.y = winHeight - playerSize.y
        if player2Pos.y <= 0:
            player2Pos.y = 0
            
        # Score
        text = font.render(str(scoreP1) + "             " + str(scoreP2), True, "white")
        textSurface = text.get_rect()
        textSurface.center = ( winWidth/2, 50)
        screen.blit(text, textSurface)


    # Game win/lose handling
    if scoreP1 > 5:
        gameIsRunning = False
        GameText1 = font.render("Player 1 Won!", True, "white")
        blackBG = GameText1.get_rect()
        screen.blit(blackBG, (0,0))
    elif scoreP2 > 5:
        gameIsRunning = False
        GameText2 = font.render("Player 2 Won!", True, "white")
        blackBG = GameText2.get_rect()
        screen.blit(blackBG, (0,0))
    
    # Quit Mechanic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()


import pygame
from pyvidplayer import Video
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
ballSpeed = pygame.Vector2(8, 10)

playerAccelRate = 2
friction = .8
vel1 = 0
vel2 = 0

scoreP1 = 0
scoreP2 = 0
run = True

gameIsRunning = False
inMenu = True
gameMessage = False
gameMusic = True

text3Color = "white"
text4Color = "white"
text5Color = "white"

bg_video = Video("src/background.mp4")
bg_video.set_size((winWidth, winHeight))

backgroundMusic = pygame.mixer.Sound("src/bg_music.ogg")
selectSFX = pygame.mixer.Sound("src/select.wav")
playerHitSFX = pygame.mixer.Sound("src/playerHit.wav")
wallHitSFX = pygame.mixer.Sound("src/wallHit.wav")
LostPointSFX = pygame.mixer.Sound("src/explosion.wav")
sfxSounds = True
# Text
font1 = pygame.font.Font('gameFont.ttf', 42)
font2 = pygame.font.Font('gameFont.ttf', 15)
txt3Content = "Play"
txt4Content = "Options"
txt5Content = "credits"

# Ball Behaviour
def ballMovement(ballX, ballY, ballSpeed, ballSpeedY, ballDirectionX, ballDirectionY, scoreP1, scoreP2):
    if ballDirectionX == 1 and ballX < winWidth - ballRadius:
        ballX += ballSpeed
        sfxSounds = True
    elif ballDirectionX == 1 and ballX >= winWidth - ballRadius:
        ballDirectionX *= -1
        scoreP1 += 1
        ballX = winWidth/2
        ballY = winHeight/2

    if ballDirectionX == -1 and ballX > ballRadius:
        ballX -= ballSpeed
        sfxSounds = True
    elif ballDirectionX == -1 and ballX <= ballRadius:
        scoreP2 += 1
        ballX = winWidth/2
        ballY = winHeight/2

    if ballDirectionY == 1 and ballY > ballRadius:
        ballY -= ballSpeedY
        sfxSounds = True
    elif ballDirectionY == 1 and ballY <= ballRadius:
        if sfxSounds:
            sfxSounds = False
            wallHitSFX.play()
        ballDirectionY *= -1

    if ballDirectionY == -1 and ballY < winHeight - ballRadius:
        ballY += ballSpeedY
        sfxSounds = True
    elif ballDirectionY == -1 and ballY >= winHeight - ballRadius:
        if sfxSounds:
            sfxSounds = False
            wallHitSFX.play()
        ballDirectionY *= -1

    return ballX, ballY, ballDirectionX, ballDirectionY, scoreP1, scoreP2

def BallIsColliding(playerPosition, playerSize, ballRadius, ballPosition):
    collisionX = max(playerPosition.x, min(ballPosition.x, playerPosition.x + playerSize.x))
    collisionY = max(playerPosition.y, min(ballPosition.y, playerPosition.y + playerSize.y))

    distanceX = ballPosition.x - collisionX
    distanceY = ballPosition.y - collisionY

    return (distanceX ** 2 + distanceY ** 2) <= (ballRadius ** 2)

# Main Game loop --->
if gameMusic and run:
        pygame.mixer.Channel(2).play(backgroundMusic, -1)
while run:

    screen.fill("black")

    if inMenu:
        bg_video.draw(screen, (0,0))
        mousePos = pygame.mouse.get_pos()
        text1 = font2.render("[ More features coming soon ]", True, (203, 0, 0)) 
        text2 = font1.render("Ping Pong", True, "white")
        text3 = font1.render(txt3Content, True, text3Color)
        text4 = font1.render(txt4Content, True, text4Color)
        text5 = font1.render(txt5Content, True, text5Color)
        surface1 = text1.get_rect()
        surface2 = text2.get_rect()
        surface3 = text3.get_rect()
        surface4 = text4.get_rect()
        surface5 = text5.get_rect()
        surface1.center = (winWidth * .5, 50)
        surface2.center = (winWidth * .5, winHeight * 0.4)
        surface3.center = (winWidth * .5, winHeight * 0.4 + 140)
        surface4.center = (winWidth * .5, winHeight * 0.4 + 220)
        surface5.center = (winWidth * .5, winHeight * 0.4 + 300)
        screen.blit(text1, surface1)
        screen.blit(text2, surface2)
        screen.blit(text3, surface3)
        screen.blit(text4, surface4)
        screen.blit(text5, surface5)
        if surface3.collidepoint(mousePos):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selectSFX.play(0, 500, 50)
                    gameIsRunning = True
                    inMenu = False
            text3Color = (150,150,150)
            text4Coler = "white"
            text5Color = "white"
        elif surface4.collidepoint(mousePos):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selectSFX.play(0, 500, 50)

            text4Color = (150, 150, 150)
            text3Color = "white"
            text5Color = "white"
        elif surface5.collidepoint(mousePos):
            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    selectSFX.play(0, 500, 50)

            text5Color = (150,150,150)
            text4Color = "white"
            text3Color = "white"
        else:
            text3Color = "white"
            text4Color = "white"
            text5Color = "white"
    elif gameIsRunning:
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
            if sfxSounds:
                sfxSounds = False
                playerHitSFX.play()
        else:
            sfxSounds = True
        if BallIsColliding(player2Pos, playerSize, ballRadius, ballPos):
            ballPos.x = player2Pos.x - ballRadius
            ballDirection.x *= -1
            if sfxSounds:
                sfxSounds = False
                playerHitSFX.play()
        else:
            sfxSounds = True
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
        text = font1.render(str(scoreP1) + "   " + str(scoreP2), True, "white")
        textSurface = text.get_rect()
        textSurface.center = (winWidth/2, 50)
        screen.blit(text, textSurface)


    # Game win/lose handling
    if scoreP1 > 5:
        gameIsRunning = False
        player1Won = font1.render("Player 1 Won!", True, "white")
        screen.blit(player1Won, surface1)
    elif scoreP2 > 5:
        gameIsRunning = False
        player2Won = font1.render("Player 2 Won!", True, "white")
        screen.blit(player2Won, surface1)
    
    # Quit Mechanic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()


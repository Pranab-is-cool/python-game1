import pygame
import random
import math

#pygame initialization
pygame.init()

# resolution of the screen
screen = pygame.display.set_mode((800, 600))

background = pygame.image.load("bg.png")

pygame.display.set_caption("Impossible")

# player
playerImg = pygame.image.load("robot.png")
playerX = 345
playerY = 450
player_change1 = 0
player_change2 = 0

# enemy
enemyImg = pygame.image.load("bulletnew.png")
enemyX = 756
enemyY = random.randint(250, 450)
enemy_move = 2

# enemyup
enemy1Img = pygame.image.load("bulletup.png")
enemy1X = random.randint(10, 600)
enemy1Y = 12
enemy1_move = 2

# enemyright
enemy2Img = pygame.image.load("bulletR.png")
enemy2X = 12
enemy2Y = random.randint(250, 450)
enemy2_move = 2

# enemy up
enemy3Img = pygame.image.load("bulletD.png")
enemy3X = random.randint(10, 600)
enemy3Y = 556
enemy3_move = 2

n = 0.001

# score
score_value = 100
font = pygame.font.Font("freesansbold.ttf", 32)
textX = 10
textY = 10

#game over
font_ove = pygame.font.Font("freesansbold.ttf", 24)
textoX = 500
textoY = 10

def show_score(textX, textY):
    score = font.render("HEALTH:" + str(score_value), True ,(25,100,150))
    screen.blit(score , (textX, textY))

def game_over_text(textoX,textoY):
    over_text = font_ove.render("0 Health to lose ",True , (25,100,150))
    screen.blit(over_text,(textoX,textoY))

def player(playerX, playerY):
    screen.blit(playerImg, (playerX, playerY))


# adding player
def enemy(enemyX, enemyY):
    screen.blit(enemyImg, (enemyX, enemyY))


def enemy1(enemy1X, enemy1Y):
    screen.blit(enemy1Img, (enemy1X, enemy1Y))


def enemy2(enemy2X, enemy2Y):
    screen.blit(enemy2Img, (enemy2X, enemy2Y))


def enemy3(enemy3X, enemy3Y):
    screen.blit(enemy3Img, (enemy3X, enemy3Y))


def is_collision(playerX, playerY, enemyX, enemyY):
    distance = math.sqrt(math.pow(playerX - enemyX, 2) + math.pow(playerY - enemyY, 2))
    if distance < 10:
        return True
    else:
        return False

def is_collision1(playerX, playerY, enemy1X, enemy1Y):
    distance = math.sqrt(math.pow(playerX - enemy1X, 2) + math.pow(playerY - enemy1Y, 2))
    if distance < 10:
        return True
    else:
        return False

def is_collision2(playerX, playerY, enemy2X, enemy2Y):
    distance = math.sqrt(math.pow(playerX - enemy2X, 2) + math.pow(playerY - enemy2Y, 2))
    if distance < 10:
        return True
    else:
        return False

def is_collision3(playerX, playerY, enemy3X, enemy3Y):
    distance = math.sqrt(math.pow(playerX - enemy3X, 2) + math.pow(playerY - enemy3Y, 2))
    if distance < 10:
        return True
    else:
        return False

# main_loop
run = True
while run:
    screen.fill((0, 0, 0))
    screen.blit(background, (0, 0))
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                player_change1 += 2
            if event.key == pygame.K_LEFT:
                player_change1 -= 2
            if event.key == pygame.K_UP:
                player_change2 += 2
            if event.key == pygame.K_DOWN:
                player_change2 -= 2

        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT or event.key == pygame.K_LEFT or pygame.K_UP:
                player_change1 = 0
                player_change2 = 0

    playerX += player_change1
    if playerX <= 0:
        playerX = 0
    elif playerX >= 756:
        playerX = 756

    playerY -= player_change2
    if playerY <= 250:
        playerY = 250
    elif playerY >= 450:
        playerY = 450

    enemy_move += n

    enemyX -= enemy_move
    if enemyX <= 0:
        enemyX = 756
    elif enemyX >= 756:
        enemyX = 756
        enemyY = random.randint(800, 450)
        enemy_move = 7

    enemy1Y += enemy_move
    if enemy1Y <= 0:
        enemy1Y = 0
    elif enemy1Y >= 598:
        enemy1Y = 0
        enemy1X = random.randint(10, 600)
        enemy1Y = 12
        enemy1_move = 7

    enemy2X += enemy_move
    if enemy2X <= 0:
        enemy2X = 0
    elif enemy2X >= 736:
        enemy2X = 0
        enemy2X = 12
        enemy2Y = random.randint(250, 450)
        enemy2_move = 7

    enemy3Y -= enemy_move
    if enemy3Y <= 0:
        enemy3Y = 598
    elif enemy3Y >= 598:
        enemy3Y = 598
        enemy3X = random.randint(10, 600)
        enemy3Y = 12
        enemy3_move = 7

    collision = is_collision(playerX, playerY, enemyX, enemyY)
    if collision :
        score_value -= int(0.1)
    collision = is_collision1(playerX, playerY, enemy1X, enemy1Y)
    if collision:
        score_value -= int(0.1)
    collision = is_collision2(playerX, playerY, enemy2X, enemy2Y)
    if collision:
        score_value -= int(0.1)
    collision = is_collision3(playerX, playerY, enemy3X, enemy3Y)
    if collision:
        score_value -= int(0.1)

    if score_value == 0:
        game_over_text(textoX,textoY)
        break






    player(playerX, playerY)
    enemy(enemyX, enemyY)
    enemy1(enemy1X, enemy1Y)
    enemy2(enemy2X, enemy2Y)
    enemy3(enemy3X, enemy3Y)
    is_collision(playerX, playerY, enemyX, enemyY)
    is_collision1(playerX, playerY, enemy1X, enemy1Y)
    is_collision2(playerX, playerY, enemy2X, enemy2Y)
    is_collision3(playerX, playerY, enemy3X, enemy3Y)
    show_score(textX, textY)
    game_over_text(textoX,textoY)
    pygame.display.update()

import random
import sys
import time

import pygame
from pygame import mixer
from matplotlib.font_manager import get_font

pygame.init()

SCREEN = pygame.display.set_mode((1000, 600))

Final_Coin_Y = 0
Final_Coin_X = 0

main_font = pygame.font.SysFont("cambria", 30)
BG = pygame.image.load("Background.png")
BG = pygame.transform.scale(BG, (1000, 600))

font = pygame.font.Font('freesansbold.ttf', 26)
odd_show=font.render("Its odd!!", True, (128, 0, 0))
even_show=font.render("Its even!!", True, (128, 0,0))
coin_show=font.render("Coin is moving", True, (128, 0, 0))
snake_show=font.render("OMG!!What's Happening!", True, (255, 125, 0))
Life_text=font.render("Life:", True, (255, 255, 0))
space_show=font.render("Press space to roll the dice", True, (128, 0, 0))



def corOrdinateToNmb(x, y):
    if (x > 150 and x < 250):
        if (y > 50 and y < 150):
            return 21
        if (y > 150 and y < 250):
            return 20
        if (y > 250 and y < 350):
            return 11
        if (y > 350 and y < 450):
            return 10
        if (y > 450 and y < 550):
            return 1
    if (x > 250 and x < 350):
        if (y > 50 and y < 150):
            return 22
        if (y > 150 and y < 250):
            return 19
        if (y > 250 and y < 350):
            return 12
        if (y > 350 and y < 450):
            return 9
        if (y > 450 and y < 550):
            return 2

    if (x > 350 and x < 450):
        if (y > 50 and y < 150):
            return 23
        if (y > 150 and y < 250):
            return 18
        if (y > 250 and y < 350):
            return 13
        if (y > 350 and y < 450):
            return 8
        if (y > 450 and y < 550):
            return 3

    if (x > 450 and x < 550):
        if (y > 50 and y < 150):
            return 24
        if (y > 150 and y < 250):
            return 17
        if (y > 250 and y < 350):
            return 14
        if (y > 350 and y < 450):
            return 7
        if (y > 450 and y < 550):
            return 4

    if (x > 550 and x < 650):
        if (y > 50 and y < 150):
            return 25
        if (y > 150 and y < 250):
            return 16
        if (y > 250 and y < 350):
            return 15
        if (y > 350 and y < 450):
            return 6
        if (y > 450 and y < 550):
            return 5


def nmbToCo_ladder(nmb):
    if nmb == 10:
        return (175, 375)
    if nmb == 9:
        return (275, 375)
    if nmb == 8:
        return (375, 375)
    if nmb == 7:
        return (475, 375)
    if nmb == 6:
        return (575, 375)
    if nmb == 11:
        return (175, 275)
    if nmb == 12:
        return (275, 275)
    if nmb == 13:
        return (375, 275)
    if nmb == 14:
        return (475, 275)
    if nmb == 15:
        return (575, 275)
    if nmb == 20:
        return (175, 175)
    if nmb == 19:
        return (275, 175)
    if nmb == 18:
        return (375, 175)
    if nmb == 17:
        return (475, 175)
    if nmb == 16:
        return (575, 175)
    if nmb == 21:
        return (175, 75)
    if nmb == 22:
        return (275, 75)
    if nmb == 23:
        return (375, 75)
    if nmb == 24:
        return (475, 75)
    if nmb == 25:
        return (575, 75)


# coOrdinateToNmb for Ladder
def nmbToCordinate_green(nmb):
    if nmb == 10:
        return (160, 375)
    if nmb == 9:
        return (260, 375)
    if nmb == 8:
        return (360, 375)
    if nmb == 7:
        return (460, 375)
    if nmb == 6:
        return (560, 375)
    if nmb == 11:
        return (160, 275)
    if nmb == 12:
        return (260, 275)
    if nmb == 13:
        return (360, 275)
    if nmb == 14:
        return (460, 275)
    if nmb == 15:
        return (560, 275)
    if nmb == 20:
        return (160, 175)
    if nmb == 19:
        return (260, 175)
    if nmb == 18:
        return (360, 175)
    if nmb == 17:
        return (460, 175)
    if nmb == 16:
        return (560, 175)
    if nmb == 21:
        return (160, 75)
    if nmb == 22:
        return (260, 75)
    if nmb == 23:
        return (360, 75)
    if nmb == 24:
        return (460, 75)
    if nmb == 25:
        return (560, 75)

crossFlux=True


class Button():
    def __init__(self, image, position, text_input, base_color, hovering_color):
        self.image = image
        self.x_pos = position[0]
        self.y_pos = position[1]
        # self.ont = font
        self.base_color, self.hovering_color = base_color, hovering_color
        self.text_input = text_input
        self.text = main_font.render(self.text_input, True, self.base_color)
        if self.image is None:
            self.image = self.text
        self.rect = self.image.get_rect(center=(self.x_pos, self.y_pos))
        self.text_rect = self.text.get_rect(center=(self.x_pos, self.y_pos))

    def update(self):
        SCREEN.blit(self.image, self.rect)
        SCREEN.blit(self.text, self.text_rect)

    def checkForInput(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            print("Button Press!")
            return True
        return False

    def changeColor(self, position):
        if position[0] in range(self.rect.left, self.rect.right) and position[1] in range(self.rect.top,
                                                                                          self.rect.bottom):
            self.text = main_font.render(self.text_input, True, self.hovering_color)
        else:
            self.text = main_font.render(self.text_input, True, self.base_color)


# background music
mixer.music.load("Background.mp3")
mixer.music.play(-1)


# life_show
def lifeShow(life_count, lifeImg):
    for i in range(0, life_count):
        SCREEN.blit(lifeImg[i], (150 + (i * 80), 0))


# draw board
def draw_board(x, y, board_img):
    SCREEN.blit(board_img, (x, y))


# draw snake
def draw_snake(x, y, rX, rY, snake_img, redSnake_img):
    SCREEN.blit(snake_img, (x, y))
    SCREEN.blit(redSnake_img, (rX, rY))


def draw_ladder(x, y, ladder_image):
    SCREEN.blit(ladder_image, (x, y))


# draw dice
def draw_dice(diceImg, player_score):
    # print("dice = ", player_score)
    SCREEN.blit(diceImg[player_score - 1], (800, 150))


def draw_coin(x, y, coin_img):
    SCREEN.blit(coin_img, (x, y))


def coin_Stable(coin_img_X, coin_img_Y):
    global Final_Coin_X
    Final_Coin_X = coin_img_X
    global Final_Coin_Y
    Final_Coin_Y = coin_img_Y

def changemouseColor(position, rect, img, imgOri):
    if position[0] in range(rect.left, rect.right) and position[1] in range(rect.top,
                                                                            rect.bottom):
        SCREEN.blit(img, (440, 450))
        # pygame.display.update()
        if pygame.mouse.get_pressed()[0] == 1:
            return True


    else:
        SCREEN.blit(imgOri, (440, 450))
        # pygame.display.update()
    return False


def gameOver():
    textFont = pygame.font.SysFont("cambria", 2)
    global crossFlux
    gameOverImg = pygame.image.load("game-over.png")
    playAgainImg = pygame.image.load("play-again.jpg")
    playAgainImg = pygame.transform.scale(playAgainImg, (70, 70))
    playAg = pygame.image.load("playAg.png")
    playAg = pygame.transform.scale(playAg, (70, 70))
    while True:

        SCREEN.fill((204, 229, 255))
        imggg = pygame.image.load("button.png")
        imggg = pygame.transform.scale(imggg, (64, 64.25))
        Back_Button = Button(image=imggg, position=(1150, 250),
                             text_input="Play Again", base_color="#d7fcd4", hovering_color="Green")
        Back_Button.changeColor(pygame.mouse.get_pos())
        Back_Button.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                crossFlux = False
                sys.exit()
            if changemouseColor(pygame.mouse.get_pos(), pygame.Rect(440, 450, 70, 70), playAg, playAgainImg):
                gameMenu()
        if not crossFlux:
            pygame.quit()
            sys.exit()
        gameOverText = textFont.render("Game Over", True, (255, 255, 255))
        SCREEN.blit(gameOverText, (400, 250))
        SCREEN.blit(gameOverImg, (360, 140))
        SCREEN.blit(playAgainImg, (440, 450))
        pygame.display.update()


def youWin():
    textFont = pygame.font.SysFont("cambria", 5)
    fontt = pygame.font.SysFont("None", 35)
    youImg = pygame.image.load("you.png")
    playAgainImg = pygame.image.load("play-again.jpg")
    playAgainImg = pygame.transform.scale(playAgainImg, (70, 70))
    playAg = pygame.image.load("playAg.png")
    playAg = pygame.transform.scale(playAg, (70, 70))
    global crossFlux

    while True:

        SCREEN.fill((255, 102, 102))
        imggg = pygame.image.load("button.png")
        imggg = pygame.transform.scale(imggg, (90, 64.25))
        # Back_Button = Button(image=imggg, position=(0, 0),
        #                      text_input="", base_color="#d7fcd4", hovering_color="Green")
        # Back_Button.changeColor(pygame.mouse.get_pos())
        # Back_Button.update()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                crossFlux = False
                sys.exit()
            if changemouseColor(pygame.mouse.get_pos(), pygame.Rect(440, 450, 70, 70), playAg, playAgainImg):
                gameMenu()

        if not crossFlux:
            pygame.quit()
            sys.exit()

        gameOverText = fontt.render("You won", True, (255, 255, 255))
        SCREEN.blit(playAgainImg, (440, 450))
        SCREEN.blit(youImg, (360, 140))
        pygame.display.update()



def gameMenu():
    clock = pygame.time.Clock()
    time_dice_turned = 0
    left_to_right = 1
    right_to_left = 1
    # player initial score
    player_score = 1
    coin_moving = False
    dice_rolling = False
    player_position = player_score
    eating = False
    redEating = False
    coin_stable = 1
    uthing = False
    odd = 1
    rolling_check = True
    dice_checking = 0

    running = True

    life_count = 3
    board_img = pygame.image.load("25board.png")
    board_img_X = 150
    board_img_Y = 50

    # hard code
    main_font = pygame.font.SysFont("cambria", 50)
    # snake image
    snake_img = pygame.image.load("Snake1.png")
    snake_img_X = 250 + 10
    snake_img_Y = 250 + 25

    # snake2 image
    redSnake_img = pygame.image.load("redSnake.png")
    redSnake_img_X = 450 + 10
    redSnake_img_Y = 150 + 25

    # Danger check
    X_Start = snake_img_X - 10
    Y_Start = snake_img_Y - 25

    # Danger Red Snake
    X_redSnake_Start = redSnake_img_X - 10
    Y_redSnake_Start = redSnake_img_Y - 25

    # ladder image
    ladder_image = pygame.image.load("ladder2.png")
    ladder_image_X = 175
    ladder_image_Y = 75

    # moi otha check
    X_LadderEnd = ladder_image_X - 25
    Y_LadderEnd = ladder_image_Y - 25 + 200

    # coin image
    coin_img = pygame.image.load("coin.png")
    coin_img_X = 150 + 30
    coin_img_Y = 50 + 430

    # load dice images
    diceImg = []
    diceImg.append(pygame.image.load('dice1p2.png'))
    diceImg.append(pygame.image.load('dice2p2.png'))
    diceImg.append(pygame.image.load('dice3p2.png'))
    diceImg.append(pygame.image.load('dice4p2.png'))
    diceImg.append(pygame.image.load('dice5p2.png'))
    diceImg.append(pygame.image.load('dice6p2.png'))

    lifeImg = []
    lifeImg.append(pygame.image.load("life.png"))
    lifeImg.append(pygame.image.load("life.png"))
    lifeImg.append(pygame.image.load("life.png"))
    lifeImg.append(pygame.image.load("life.png"))
    lifeImg.append(pygame.image.load("life.png"))
    global Final_Coin_Y
    Final_Coin_Y = coin_img_Y

    time_dice_turned = 0

    while running:
        print(nmbToCo_ladder(12))
        SCREEN.fill((195, 115, 42))
        SCREEN.blit(pygame.image.load("background3.jpg"), (0, 0))
        draw_board(board_img_X, board_img_Y, board_img)
        draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img, redSnake_img)
        draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
        lifeShow(life_count, lifeImg)
        if player_position == 1:
            draw_coin(coin_img_X, coin_img_Y, coin_img)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    if not dice_rolling:
                        dice_rolling = True
                        dice_sound = mixer.Sound("DiceRolling.mp3")
                        dice_sound.play()
                if event.key == pygame.K_o:
                    odd = 1


        coin_Stable(coin_img_X, coin_img_Y)

        # draw_dice()
        # shap khaile niche namche
        if odd == 1:
            if eating:
                life_count -= 1
                coin_img_Y += 100
                eating = False
                snake_tail_position = corOrdinateToNmb(snake_img_X, snake_img_Y + 100)
                print("downfall")
                player_position = snake_tail_position
                left_to_right *= -1
            if redEating:
                life_count -= 1
                coin_img_Y += 100
                redEating = False
                red_snake_tail_position = corOrdinateToNmb(redSnake_img_X, redSnake_img_Y + 100)
                print("downfall")
                player_position = red_snake_tail_position
                left_to_right *= -1

            if uthing:
                coin_img_Y -= 100
                uthing = False
                ladder_headPosition = corOrdinateToNmb(ladder_image_X, ladder_image_Y)
                print("Flying")
                player_position = ladder_headPosition
                left_to_right *= -1

            # Coin Moving
            if (coin_moving == True and rolling_check == True):
                print("Check:", rolling_check)
                if (player_position < destination and destination <= 25):
                    # print("left to right", left_to_right)

                    if player_position % 5 == 0:
                        coin_img_Y -= 100
                        left_to_right *= -1
                    else:
                        coin_img_X += left_to_right * 100
                    print(coin_img_X, coin_img_Y)
                    player_position += 1

                if destination == player_position:
                    # shap amk khacce
                    if X_Start < coin_img_X and coin_img_X < X_Start + 100:
                        if Y_Start < coin_img_Y and coin_img_Y < Y_Start + 100:
                            eating = True
                            snake_sound = mixer.Sound("SnakeHissing.mp3")
                            snake_sound.play()
                    if (X_redSnake_Start < coin_img_X and coin_img_X < X_redSnake_Start + 100):
                        if (Y_redSnake_Start < coin_img_Y and coin_img_Y < Y_redSnake_Start + 100):
                            print("red shap amk khacce")
                            redEating = True
                            snake_sound = mixer.Sound("SnakeHissing.mp3")
                            snake_sound.play()

                    if (X_LadderEnd < coin_img_X and coin_img_X < X_LadderEnd + 100):
                        if (Y_LadderEnd - 100 < coin_img_Y and coin_img_Y < Y_LadderEnd):
                            print("moi e uthc")
                            uthing = True
                            ladder_sound = mixer.Sound("LadderClimbing.mp3")
                            ladder_sound.play()
                    coin_moving = False

            # Snake_Moving
            if (rolling_check == False and dice_checking != 0):
                # snake_img_X=snake_img_X+player_score*100
                print("Shap nore")
                dice_checking=0

                snake_position = corOrdinateToNmb(snake_img_X, snake_img_Y)
                red_snakePosition = corOrdinateToNmb(redSnake_img_X, redSnake_img_Y)
                ladder_head_pos = corOrdinateToNmb(ladder_image_X, ladder_image_Y)
                ladder_tail_pos = corOrdinateToNmb(ladder_image_X, ladder_image_Y + 100)
                print("ladderHeadPositon:", ladder_head_pos)
                print("LadderTail Pos", ladder_tail_pos)

                print("snake pos:", snake_position)
                #Green snake
                if (snake_position - player_position > 6 and snake_position-player_score>5):
                    if(snake_position<red_snakePosition):
                        snake_position -= player_score
                        print("playerScore:", player_score)
                        print("snakeiiiii:", snake_position)
                        print("In 1st looooooooooooooooooop")

                        (snake_img_X, snake_img_Y) = nmbToCordinate_green(snake_position)
                        print("Snake position:", snake_img_X, snake_img_Y)
                        X_Start = snake_img_X - 10
                        Y_Start = snake_img_Y - 25
                        draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,redSnake_img)
                        if(snake_position==player_position):
                            eating=True
                        if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                    elif(snake_position>red_snakePosition):
                        print("2nd loooooooooooooooop")
                        if(red_snakePosition-player_position>6 and red_snakePosition-player_score>5):
                            red_snakePosition -= player_score
                            (redSnake_img_X, redSnake_img_Y) = nmbToCordinate_green(red_snakePosition)
                            X_redSnake_Start = redSnake_img_X - 10
                            Y_redSnake_Start = redSnake_img_Y - 25
                            draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,
                                       redSnake_img)
                            if(red_snakePosition==player_position):
                                redEating=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                            print("Red snake nore jao")

                        elif(red_snakePosition-player_position<=6 and red_snakePosition-player_position>=0 and snake_position-player_score>5):
                            snake_position -= player_score
                            print("playerScore:", player_score)
                            print("snakeiiiii:", snake_position)

                            (snake_img_X, snake_img_Y) = nmbToCordinate_green(snake_position)
                            print("Snake position:", snake_img_X, snake_img_Y)
                            X_Start = snake_img_X - 10
                            Y_Start = snake_img_Y - 25
                            draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,redSnake_img)
                            if(snake_position==player_position):
                                eating=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)

                        elif(red_snakePosition-player_position<0 and red_snakePosition-player_position>-6 and red_snakePosition+player_score<=25):
                            red_snakePosition += player_score
                            (redSnake_img_X, redSnake_img_Y) = nmbToCordinate_green(red_snakePosition)
                            X_redSnake_Start = redSnake_img_X - 10
                            Y_redSnake_Start = redSnake_img_Y - 25
                            draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,redSnake_img)
                            if(red_snakePosition==player_position):
                                redEating=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                            print("Red snake nore jao")

                        else:
                            print("moi norbe3")
                            if (ladder_tail_pos > player_position and ladder_head_pos - player_score > 5 and ladder_head_pos + player_score <= 25):
                                ladder_head_pos -= player_score
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                                if(ladder_tail_pos==player_position):
                                    uthing=True
                                if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                    life_count-=1
                                    ladder_head_pos -=1
                                    (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                    X_LadderEnd = ladder_image_X - 25
                                    Y_LadderEnd = ladder_image_Y - 25 + 200
                                    draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)

                            elif (ladder_tail_pos < player_position and ladder_head_pos - player_score > 5):
                                ladder_head_pos -= player_score
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                                if(ladder_tail_pos==player_position):
                                    uthing=True
                                if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                    life_count-=1
                                    ladder_head_pos -=1
                                    (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                    X_LadderEnd = ladder_image_X - 25
                                    Y_LadderEnd = ladder_image_Y - 25 + 200
                                    draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                # range er moddhe
                if (snake_position - player_position<=6 and snake_position-player_position>=0):

                    if(red_snakePosition-player_position>6 and red_snakePosition-player_score>5):
                        red_snakePosition -= player_score
                        (redSnake_img_X, redSnake_img_Y) = nmbToCordinate_green(red_snakePosition)
                        X_redSnake_Start = redSnake_img_X - 10
                        Y_redSnake_Start = redSnake_img_Y - 25
                        draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,redSnake_img)
                        if(red_snakePosition==player_position):
                            redEating=True
                        if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                        print("Red snake nore jao")
                    elif(red_snakePosition-player_position<=6 and red_snakePosition-player_position>=0):
                         if (ladder_tail_pos > player_position and ladder_head_pos - player_score > 5 and ladder_head_pos + player_score <= 25):
                            ladder_head_pos -= player_score
                            (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                            X_LadderEnd = ladder_image_X - 25
                            Y_LadderEnd = ladder_image_Y - 25 + 200
                            draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                            if(ladder_tail_pos==player_position):
                                uthing=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)

                         elif (ladder_tail_pos < player_position and ladder_head_pos - player_score > 5):
                            ladder_head_pos -= player_score
                            (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                            X_LadderEnd = ladder_image_X - 25
                            Y_LadderEnd = ladder_image_Y - 25 + 200
                            draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                            if(ladder_tail_pos==player_position):
                                uthing=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)


                    elif(red_snakePosition-player_position<0 and red_snakePosition-player_position>-6 and red_snakePosition+player_score<=25):
                            red_snakePosition += player_score
                            (redSnake_img_X, redSnake_img_Y) = nmbToCordinate_green(red_snakePosition)
                            X_redSnake_Start = redSnake_img_X - 10
                            Y_redSnake_Start = redSnake_img_Y - 25
                            draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,redSnake_img)
                            print("Red snake nore jao")
                            if(red_snakePosition==player_position):
                                redEating=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                    else:
                        print("moi norbe3")
                        if (ladder_tail_pos > player_position and ladder_head_pos - player_score > 5 and ladder_head_pos + player_score <= 25):
                            ladder_head_pos -= player_score
                            (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                            X_LadderEnd = ladder_image_X - 25
                            Y_LadderEnd = ladder_image_Y - 25 + 200
                            draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                            if(ladder_tail_pos==player_position):
                                uthing=True
                            if(ladder_head_pos==snake_position or red_snakePosition==ladder_head_pos):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)

                        elif (ladder_tail_pos < player_position and ladder_head_pos - player_score > 5):
                            ladder_head_pos -= player_score
                            (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                            X_LadderEnd = ladder_image_X - 25
                            Y_LadderEnd = ladder_image_Y - 25 + 200
                            draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                            if(ladder_tail_pos==player_position):
                                uthing=True
                            if(ladder_head_pos==snake_position or red_snakePosition==ladder_head_pos):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)

                #pichone range er moddhe
                if (snake_position - player_position<0 and snake_position-player_position>=-6 and snake_position+player_score<25):
                    if(snake_position>red_snakePosition):
                        snake_position -= player_score
                        print("playerScore:", player_score)
                        print("snakeiiiii:", snake_position)

                        (snake_img_X, snake_img_Y) = nmbToCordinate_green(snake_position)
                        print("Snake position:", snake_img_X, snake_img_Y)
                        X_Start = snake_img_X - 10
                        Y_Start = snake_img_Y - 25
                        draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,redSnake_img)
                        if(snake_position==player_position):
                            eating=True
                        if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                    else:
                        if(red_snakePosition>player_position):
                            snake_position += player_score
                            print("playerScore:", player_score)
                            print("snakeiiiii:", snake_position)

                            (snake_img_X, snake_img_Y) = nmbToCordinate_green(snake_position)
                            print("Snake position:", snake_img_X, snake_img_Y)
                            X_Start = snake_img_X - 10
                            Y_Start = snake_img_Y - 25
                            draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,redSnake_img)
                            if(snake_position==player_position):
                                eating=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                        else:
                            red_snakePosition += player_score
                            (redSnake_img_X, redSnake_img_Y) = nmbToCordinate_green(red_snakePosition)
                            X_redSnake_Start = redSnake_img_X - 10
                            Y_redSnake_Start = redSnake_img_Y - 25
                            draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,redSnake_img)
                            print("Red snake nore jao")
                            if(red_snakePosition==player_position):
                                redEating=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)

                #oneek oneek pichone
                if (snake_position - player_position<-6):
                     if(red_snakePosition-player_position>6 and red_snakePosition-player_score>5):
                        red_snakePosition -= player_score
                        (redSnake_img_X, redSnake_img_Y) = nmbToCordinate_green(red_snakePosition)
                        X_redSnake_Start = redSnake_img_X - 10
                        Y_redSnake_Start = redSnake_img_Y - 25
                        draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,redSnake_img)
                        print("Red snake nore jao")
                        if(red_snakePosition==player_position):
                            redEating=True
                        if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                     elif(red_snakePosition-player_position<=6 and red_snakePosition-player_position>=0):
                         if (ladder_tail_pos > player_position and ladder_head_pos - player_score > 5 and ladder_head_pos + player_score <= 25):
                            ladder_head_pos -= player_score
                            (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                            X_LadderEnd = ladder_image_X - 25
                            Y_LadderEnd = ladder_image_Y - 25 + 200
                            draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                            if(ladder_tail_pos==player_position):
                                uthing=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)

                         elif (ladder_tail_pos < player_position and ladder_head_pos - player_score > 5):
                            ladder_head_pos -= player_score
                            (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                            X_LadderEnd = ladder_image_X - 25
                            Y_LadderEnd = ladder_image_Y - 25 + 200
                            draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                            if(ladder_tail_pos==player_position):
                                uthing=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)


                     elif(red_snakePosition-player_position<0 and red_snakePosition-player_position>-6 and red_snakePosition+player_score<=25):
                            red_snakePosition += player_score
                            (redSnake_img_X, redSnake_img_Y) = nmbToCordinate_green(red_snakePosition)
                            X_redSnake_Start = redSnake_img_X - 10
                            Y_redSnake_Start = redSnake_img_Y - 25
                            draw_snake(snake_img_X, snake_img_Y, redSnake_img_X, redSnake_img_Y, snake_img,
                                       redSnake_img)
                            print("Red snake nore jao")
                            if(red_snakePosition==player_position):
                                redEating=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                     else:
                        print("moi norbe3")
                        if (ladder_tail_pos > player_position and ladder_head_pos - player_score > 5 and ladder_head_pos + player_score <= 25):
                            ladder_head_pos -= player_score
                            (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                            X_LadderEnd = ladder_image_X - 25
                            Y_LadderEnd = ladder_image_Y - 25 + 200
                            draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                            if(ladder_tail_pos==player_position):
                                uthing=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)

                        elif (ladder_tail_pos < player_position and ladder_head_pos - player_score > 5):
                            ladder_head_pos -= player_score
                            (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                            X_LadderEnd = ladder_image_X - 25
                            Y_LadderEnd = ladder_image_Y - 25 + 200
                            draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)
                            if(ladder_tail_pos==player_position):
                                uthing=True
                            if(ladder_head_pos==snake_position or ladder_head_pos==red_snakePosition):
                                life_count-=1
                                ladder_head_pos -=1
                                (ladder_image_X, ladder_image_Y) = nmbToCo_ladder(ladder_head_pos)
                                X_LadderEnd = ladder_image_X - 25
                                Y_LadderEnd = ladder_image_Y - 25 + 200
                                draw_ladder(ladder_image_X, ladder_image_Y, ladder_image)


            # Dice Rolling
            if dice_rolling:
                player_score = random.randint(1, 6)
                # player_score=4
                time_dice_turned += 1
                if time_dice_turned > 2:
                    dice_checking = player_score
                    print("Score in dice roll:", player_score)
                    dice_rolling = False
                    time_dice_turned = 0
                    if (player_score % 2 == 0 and dice_checking != 0):
                        rolling_check = False
                    if (player_score % 2 == 1 and dice_checking != 0):
                        rolling_check = True
                    coin_moving = True
                    # time_dice_turned = 0
                    destination = player_score + player_position

            draw_dice(diceImg, player_score)
            if(player_score%2==0):
                SCREEN.blit(even_show,(740,260))
                SCREEN.blit(snake_show,(650,280))
            if(player_score%2==1):
                SCREEN.blit(odd_show,(740,260))
                SCREEN.blit(coin_show,(720,280))
            draw_coin(coin_img_X, coin_img_Y, coin_img)
            coin_Stable(coin_img_X, coin_img_Y)

            if life_count == 0:
                gameOver()
                print("End Game")
            if player_position==25:
                youWin()
        SCREEN.blit(space_show,(150,555))
        SCREEN.blit(Life_text,(100,22))
        clock.tick(60)
        time.sleep(.5)
        pygame.display.update()

def howToPlay():
    text_color = (255, 100, 0)
    font = pygame.font.SysFont("Adlib BT", 35)
    lines = ["->->->Rules are similar classic Snake & Ladders game, agaist computer.", "You will start from token on "
                                                                                   "square 1 and 3 lives. You will "
                                                                                   "then roll a dice. ",
             "If the number is even, computer will take a turn. Instead of moving token, ","it will either move the "
                                                                                           "snake or the ladder by "
                                                                                           "that number.",
             "if the number is even, your token will move forward by that number.","If you move to the square with a "
                                                                                   "snake's mouth, token will come "
                                                                                   "down to the","square with snake's "
                                                                                                 "tail, and lose a "
                                                                                                 "life.",
    "square with its top."]
    global crossFlux
    # Set the vertical spacing between lines
    line_spacing = 5

    # Set the starting position for the first line

    # font = pygame.font.Font(None, 32)
    # text_color = (0, 0, 0)  # Black
    #
    # # Create a list of lines of text
    # lines = ["Line 1", "Line 2", "Line 3"]
    #
    # # Render the text to a surface
    # text_surf = font.render("\n".join(lines), True, text_color)
    #
    # # Blit the text surface to the screen
    # screen.blit(text_surf, (10, 10))


    while True:
        SCREEN.fill("black")
        SCREEN.blit(BG, (0, 0))
        MENU_MOUSE_POS = pygame.mouse.get_pos()
        SCREEN.blit(BG, (0, 0))
        y = 50

        # Iterate over the lines of text
        for line in lines:
            # Render the text to a surface
            text_surf = font.render(line, True, text_color)

            # Blit the text surface to the screen
            SCREEN.blit(text_surf, (10, y))

            # Increment the vertical position of the text
            y += font.size(line)[1]+15

        # Update the display

        # for line in lines:
        #     text = font.render(line, True, (255, 255, 255), (0, 0, 0))
        #     text_rect = text.get_rect()
        #     text_rect.topleft = (x, y)
        #     y += text_rect.height + line_spacing
        #     SCREEN.blit(text, text_rect)
        imggg = pygame.image.load("button.png")
        imggg = pygame.transform.scale(imggg, (90, 64.25))
        Back_Button = Button(image=imggg, position=(850,500),
                             text_input="BACK", base_color="Black", hovering_color="Green")
        Back_Button.changeColor(MENU_MOUSE_POS)
        Back_Button.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                crossFlux = False
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if Back_Button.checkForInput(MENU_MOUSE_POS):
                    return

        pygame.display.flip()


def main_menu():
    while True:
        SCREEN.blit(BG, (0, 0))

        MENU_MOUSE_POS = pygame.mouse.get_pos()

        # MENU_TEXT = get_font(100).render("MAIN MENU", True, "#b68f40")
        # MENU_RECT = MENU_TEXT.get_rect(center=(640, 100))

        PLAY_BUTTON = Button(image=pygame.image.load("EmpyBox.png"), position=(250, 250),
                             text_input="PLAY", base_color="#d7fcd4", hovering_color="Brown")
        OPTIONS_BUTTON = Button(image=pygame.image.load("EmpyBox2.png"), position=(250, 350),
                                text_input="HOW TO PLAY", base_color="#d7fcd4", hovering_color="Brown")
        QUIT_BUTTON = Button(image=pygame.image.load("EmpyBox.png"), position=(250, 450),
                             text_input="EXIT", base_color="#d7fcd4", hovering_color="Brown")

        # SCREEN.blit(MENU_TEXT, MENU_RECT)

        for button in [PLAY_BUTTON, OPTIONS_BUTTON, QUIT_BUTTON]:
            button.changeColor(MENU_MOUSE_POS)

            button.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if PLAY_BUTTON.checkForInput(MENU_MOUSE_POS):
                    button_sound = mixer.Sound("ButtonClick.mp3")
                    button_sound.play()
                    gameMenu()
                if OPTIONS_BUTTON.checkForInput(MENU_MOUSE_POS):
                     howToPlay()
                if QUIT_BUTTON.checkForInput(MENU_MOUSE_POS):
                    pygame.quit()
                    sys.exit()

        pygame.display.update()


main_menu()


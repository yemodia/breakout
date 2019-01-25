# Yerim Dia
# Introduction to Computer Science
# January 25, 2019
# This project is a breakout game.

import pygame, sys
from pygame.locals import *
import brick
import paddle
import ball


def main():

    # Constants that will be used in the program
    APPLICATION_WIDTH = 400
    APPLICATION_HEIGHT = 600
    PADDLE_Y_OFFSET = 30
    BRICKS_PER_ROW = 10
    BRICK_SEP = 4  # The space between each brick
    BRICK_Y_OFFSET = 70
    BRICK_WIDTH = (APPLICATION_WIDTH - (BRICKS_PER_ROW -1) * BRICK_SEP) / BRICKS_PER_ROW
    BRICK_HEIGHT = 8
    PADDLE_WIDTH = 60
    PADDLE_HEIGHT = 10
    RADIUS_OF_BALL = 10
    NUM_TURNS = 3

    # Sets up the colors
    RED = (255, 0, 0)
    ORANGE = (255, 165, 0)
    YELLOW = (255, 255, 0)
    GREEN =(0, 255, 0)
    CYAN = (0, 255, 255)
    BLACK = (0, 0, 0)
    WHITE = (255, 255, 255)
    colors = [RED, RED, ORANGE, ORANGE,YELLOW, YELLOW, GREEN, GREEN, CYAN, CYAN]

    # Step 1: Use loops to draw the rows of bricks. The top row of bricks should be 70 pixels away from the top of
    # the screen (BRICK_Y_OFFSET)

    pygame.init()
    mainSurface = pygame.display.set_mode((APPLICATION_WIDTH, APPLICATION_HEIGHT), 0, 32)
    mainSurface.fill((BLACK))
    pygame.display.set_caption(" Ultimate Breakout Z")

    background_image = pygame.image.load("Dragonball.png")
    # Changing the background image to a custom one.
    background_rect = background_image.get_rect()
    background_rect.x = 0
    background_rect.y = 0
    mainSurface.blit(background_image, background_rect)

    x = 0
    y = BRICK_Y_OFFSET

    brick_group = pygame.sprite.Group()
    paddle_group = pygame.sprite.Group()

    # Places the Paddle at the center of the application width and at the 30 offset of the bottom
    paddle_ = paddle.Paddle(mainSurface, WHITE, PADDLE_WIDTH, PADDLE_HEIGHT)
    paddle_.rect.x = APPLICATION_WIDTH / 2
    paddle_.rect.y = APPLICATION_HEIGHT - PADDLE_Y_OFFSET
    mainSurface.blit(paddle_.image, paddle_.rect)
    paddle_group.add(paddle_)

    # This places the ball at the center of the application
    bally = ball.Ball(RED, APPLICATION_WIDTH, APPLICATION_HEIGHT, RADIUS_OF_BALL)
    bally.rect.x = APPLICATION_WIDTH / 2
    bally.rect.y = APPLICATION_HEIGHT / 2
    mainSurface.blit(bally.image, bally.rect)

    for m in range(BRICKS_PER_ROW):
        color = colors[m]
        x = 0
        for b in range(BRICKS_PER_ROW):

            bricks = brick.Brick(BRICK_WIDTH, BRICK_HEIGHT, color)

            brick_group.add(bricks)
            bricks.rect.x = x
            bricks.rect.y = y
            mainSurface.blit(bricks.image, bricks.rect)
            x = x + BRICK_WIDTH + BRICK_SEP
            # creates a row of bricks
        pygame.display.update()
        y = y + BRICK_HEIGHT + BRICK_SEP
    #     Creates the other row of bricks under the following one

    while True:
        for event in pygame.event.get():
            if event == QUIT:
                pygame.quit()
                sys.exit()
        mainSurface.blit(background_image, background_rect)
        mainSurface.blit(bally.image, bally.rect)
        for x in brick_group:
            mainSurface.blit(x.image, x.rect)
        paddle_.move()
        mainSurface.blit(paddle_.image, paddle_.rect)
        bally.move()
        bally.collide_paddle(paddle_group)
        # When the ball collides with the paddle
        bally.collide(brick_group)
        # When the ball collides with the bricks
        if bally.rect.bottom >= APPLICATION_HEIGHT:
            bally.rect.x = APPLICATION_WIDTH / 2
            bally.rect.y = APPLICATION_HEIGHT / 2
            NUM_TURNS = NUM_TURNS - 1
            pygame.time.delay(6000)
        if NUM_TURNS == 0:
            pygame.quit()
            sys.exit()
        # Exits the game when the player is out of turns
        mainSurface.blit(bally.image, bally.rect)



        pygame.display.update()

main()

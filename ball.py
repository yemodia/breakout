import pygame


class Ball(pygame.sprite.Sprite):
    def __init__(self, color, windowWidth, windowHeight, radius):
        # initialize sprite super class
        super().__init__()

        # finish setting the class variables to the parameters
        self.color = color
        self.windowWidth = windowWidth
        self.windowHeight = windowHeight
        self.radius = radius
        self.speed_x = 5
        self.speed_y = 3




        # Create a surface, get the rect coordinates, fill the surface with a white color (or whatever color the
        # background of your breakout game will be.
        self.image = pygame.image.load("Ball.png")
        self.rect = self.image.get_rect()

        self.brick_sound = pygame.mixer.Sound("yahoo.wav")
        self.lose_sound = pygame.mixer.Sound("kamehameha.wav")
        # Add a circle to represent the ball to the surface just created.

    def move(self):
        self.rect.x += self.speed_x
        self.rect.y += self.speed_y

        if self.rect.right > self.windowWidth:
            self.speed_x = -self.speed_x
        if self.rect.left < 0:
            self.speed_x = -self.speed_x
        if self.rect.top < 0:
            self.speed_y = -self.speed_y
        if self.rect.bottom >= self.windowHeight:
            self.lose_sound.play()

    def collide(self, block_group):
        if pygame.sprite.spritecollide(self, block_group, True):
            self.speed_y = -self.speed_y
            self.brick_sound.play()

    def collide_paddle(self, paddle_group):
        if pygame.sprite.spritecollide(self, paddle_group, False):
            self.speed_y = -self.speed_y

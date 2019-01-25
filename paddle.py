import pygame


class Paddle(pygame.sprite.Sprite):

    def __init__(self, main_surface, color, width, height):
        # initialize sprite super class

        super().__init__()

        # finish setting the class variables to the parameters
        self.main_surface = main_surface
        self.color = color
        self.width = width
        self.height = height

        # Create a surface with the correct height and width
        self.image = pygame.image.load("Flying_Nimbus.png")

        # Get the rect coordinates
        self.rect = self.image.get_rect()



    def move(self):
        pos = pygame.mouse.get_pos()
        self.rect.x = pos[0]

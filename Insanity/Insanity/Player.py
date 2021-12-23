import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.i = pygame.image.load("images/player.png").convert_alpha()
        self.image = pygame.transform.scale(self.i, (40, 40))
        self.rect = self.image.get_rect()

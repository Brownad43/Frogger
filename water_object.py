import os
import pygame as pg


class Water_Object(pg.sprite.Sprite):
    def __init__(self, startLocation, direction, player):
        super(Water_Object, self).__init__()
        if direction == 1:
            self.image = pg.image.load(os.path.join('assets', 'log.png')).convert_alpha()
        else:
            self.image = pg.image.load(os.path.join('assets', 'turtle.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = startLocation[0]
        self.rect.centery = startLocation[1]
        self.startLocation = startLocation
        self.direction = direction
        self.players = pg.sprite.Group()
        self.players.add(player)

    # Draws in water objects
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Updates positions of water objects
    def update(self, delta):
        self.rect.x += 100 * delta * self.direction
        if (self.rect.x > 1200 and self.direction == 1):
            self.rect.centerx = 0
            self.rect.centery = self.startLocation[1]
        if (self.rect.x < -100 and self.direction == -1):
            self.rect.centerx = 1200
            self.rect.centery = self.startLocation[1]

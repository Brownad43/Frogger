import os
import pygame as pg


class Vehicle(pg.sprite.Sprite):
    def __init__(self, startLocation, direction, player):
        super(Vehicle, self).__init__()
        if direction == 1:
            self.image = pg.image.load(os.path.join('assets', 'red_car.png')).convert_alpha()
        else:
            self.image = pg.image.load(os.path.join('assets', 'blue_car.png')).convert_alpha()
            self.image = pg.transform.rotate(self.image, 180)
        self.rect = self.image.get_rect()
        self.rect.centerx = startLocation[0]
        self.rect.centery = startLocation[1]
        self.startLocation = startLocation
        self.direction = direction
        self.players = pg.sprite.Group()
        self.players.add(player)

    # Draws in vehicles
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Updates position of vehicles and checks if they are in contact with the player
    def update(self, delta):
        self.rect.x += 100 * delta * self.direction
        if (self.rect.x > 1200 and self.direction == 1):
            self.rect.centerx = 0
            self.rect.centery = self.startLocation[1]
        if (self.rect.x < -100 and self.direction == -1):
            self.rect.centerx = 1200
            self.rect.centery = self.startLocation[1]
        collision = pg.sprite.spritecollideany(self, self.players)
        if collision:
            collision.reset()
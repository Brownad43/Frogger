import pygame as pg
from water_object import Water_Object


class Log(Water_Object):
    def __init__(self, startLocation, player):
        Water_Object.__init__(self, startLocation, 1, player)

    # Draws in the log
    def draw(self, screen):
        Water_Object.draw(self, screen)

    # Updates the log to move it and see if the player is on it
    def update(self, delta):
        Water_Object.update(self, delta)
        collision = pg.sprite.spritecollideany(self, self.players)
        if collision:
            collision.set_invincible(True)
            collision.set_log(True)
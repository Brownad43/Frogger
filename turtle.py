import os
import pygame as pg
from water_object import Water_Object


class Turtle(Water_Object):
    def __init__(self, startLocation, player):
        Water_Object.__init__(self, startLocation, -1, player)
        self.submerged = False

    # Gets if the turtle is submerged or not
    def is_submerged(self):
        return self.submerged

    # Sets if the turtle is submerged or not
    def set_submerged(self, sub):
        self.submerged = sub

    # Draws in the turtle
    def draw(self, screen):
        Water_Object.draw(self, screen)

    # Updates the turtle to move it, check if its submerged, and see if the player is on it
    def update(self, delta):
        Water_Object.update(self, delta)
        if self.submerged:
            self.image = pg.image.load(os.path.join('assets', 'turtle_underwater.png')).convert_alpha()
        else:
            self.image = pg.image.load(os.path.join('assets', 'turtle.png')).convert_alpha()
        collision = pg.sprite.spritecollideany(self, self.players)
        if collision:
            if not self.submerged:
                collision.set_invincible(True)
                collision.set_turtle(True)
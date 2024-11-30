import os
import pygame as pg


# Defining Player class
class Player(pg.sprite.Sprite):
    def __init__(self):
        super(Player, self).__init__()
        self.image = pg.image.load(os.path.join('assets', 'frog.png')).convert_alpha()
        self.rect = self.image.get_rect()
        self.rect.centerx = 600
        self.rect.centery = 975
        self.direction = 0
        self.invincible = False
        self.log = False
        self.turtle = False

    # Allows the player to stand on logs and turtles
    def set_invincible(self, inv):
        self.invincible = inv

    # Setters for if the player is on a turtle or log
    def set_turtle(self, turt):
        self.turtle = turt

    def set_log(self, lo):
        self.log = lo

    # Resets to start position if the player dies
    def reset(self):
        self.rect.centerx = 600
        self.rect.centery = 975

    # Checks if player is in water to see if they are on an object or not
    def in_water(self):
        if 50 < self.rect.centery < 450:
            if not self.invincible:
                self.reset()

    # Draws in player
    def draw(self, screen):
        screen.blit(self.image, self.rect)

    # Updates player to carry if it's on a log or turtle
    def update(self, delta):
        if self.log:
            self.rect.x += 100 * delta * 1
            if (self.rect.x > 1200):
                self.rect.centerx = 0
                self.rect.centery = self.rect.centery
        if self.turtle:
            self.rect.x += 100 * delta * -1
            if (self.rect.x < -100):
                self.rect.centerx = 1200
                self.rect.centery = self.rect.centery
        self.in_water()

    # Movement if up key pressed
    def up(self):
        if self.rect.y > 50:
            self.rect.y -= 50
            if self.direction == 1:
                self.image = pg.transform.rotate(self.image, 90)
            if self.direction == 2:
                self.image = pg.transform.rotate(self.image, 180)
            if self.direction == 3:
                self.image = pg.transform.rotate(self.image, -90)
            self.direction = 0

    # Movement if left key pressed
    def left(self):
        if self.rect.x > 25:
            self.rect.x -= 50
            if self.direction == 0:
                self.image = pg.transform.rotate(self.image, 90)
            if self.direction == 1:
                self.image = pg.transform.rotate(self.image, 180)
            if self.direction == 2:
                self.image = pg.transform.rotate(self.image, -90)
            self.direction = 3

    # Movement if right key pressed
    def right(self):
        if self.rect.x < 1175:
            self.rect.x += 50
            if self.direction == 2:
                self.image = pg.transform.rotate(self.image, 90)
            if self.direction == 3:
                self.image = pg.transform.rotate(self.image, 180)
            if self.direction == 0:
                self.image = pg.transform.rotate(self.image, -90)
            self.direction = 1

    # Movement if down key pressed
    def down(self):
        if self.rect.y < 950:
            self.rect.y += 50
            if self.direction == 3:
                self.image = pg.transform.rotate(self.image, 90)
            if self.direction == 0:
                self.image = pg.transform.rotate(self.image, 180)
            if self.direction == 1:
                self.image = pg.transform.rotate(self.image, -90)
            self.direction = 2

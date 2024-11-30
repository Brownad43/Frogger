import pygame as pg
import os
from player import Player
from vehicle import Vehicle
from log import Log
from turtle import Turtle
from background import Background
import random
import time

# Clock variable for turtle switching
time_up = True


# Makes the timer switch to run multiple loops
def switch_time_up():
    time_up = True


# Changes which turtles are submerged randomly
def change_turtles(turtles):
    for t in turtles:
        if t.is_submerged():
            t.set_submerged(False)
        r = random.randint(1,4)
        if r == 1:
            t.set_submerged(True)
    time_up = False


def main():
    # Startup pygame
    pg.init()

    # Get a screen object
    screen = pg.display.set_mode([1200, 1000])

    # Creating background
    bg = Background(os.path.join('assets', 'background.png'), [0, 0])

    # Creating player and entities
    player = Player()

    logs = pg.sprite.Group()
    turtles = pg.sprite.Group()
    vehicles = pg.sprite.Group()

    # Making vehicles
    temp = True
    for i in range(525, 925, 50):
        for j in range(0, 3):
            ran = random.randint(50, 350)
            if temp:
                vehicle = Vehicle((((j * 400) + ran), i), 1, player)
            else:
                vehicle = Vehicle((((j * 400) + ran), i), -1, player)
            vehicles.add(vehicle)
        if temp:
            temp = False
        else:
            temp = True

    # Making water objects
    temp2 = True
    for i in range(75, 475, 50):
        if temp2:
            for j in range(0, 3):
                ran = random.randint(50, 350)
                log = Log((((j * 400) + ran), i), player)
                logs.add(log)
        else:
            for j in range(0, 5):
                ran = random.randint(50, 200)
                turtle = Turtle((((j * 250) + ran), i), player)
                turtles.add(turtle)
        if temp2:
            temp2 = False
        else:
            temp2 = True

    # Startup the main game loop
    running = True
    delta = 0
    fps = 60
    clock = pg.time.Clock()
    clock.tick(fps)
    last_time = time.time()
    change_turtles(turtles)
    while running:
        # Clearing the events
        for event in pg.event.get():
            if event.type == pg.QUIT:
                running = False
            if event.type == pg.KEYDOWN:
                if event.key == pg.K_w:
                    player.up()
                if event.key == pg.K_a:
                    player.left()
                if event.key == pg.K_d:
                    player.right()
                if event.key == pg.K_s:
                    player.down()

        if time_up:
            if round((time.time() - last_time), 2) > 5.00:
                change_turtles(turtles)
                last_time = time.time()
        else:
            if round((time.time() - last_time), 2) > 5.00:
                switch_time_up()
                last_time = time.time()

        # Setting Background
        screen.fill([0, 0, 0])
        screen.blit(bg.image, bg.rect)

        # Updating all entities
        for log in logs:
            log.update(delta)
        for turtle in turtles:
            turtle.update(delta)
        for vehicle in vehicles:
            vehicle.update(delta)

        player.update(delta)

        # Drawing
        logs.draw(screen)
        turtles.draw(screen)
        vehicles.draw(screen)
        player.draw(screen)

        # Flipping buffer
        pg.display.flip()
        delta = clock.tick(fps) / 1000.0

        # Resets the check for if the player in the water or on a log/turtle
        player.set_invincible(False)
        player.set_log(False)
        player.set_turtle(False)


if __name__ == "__main__":
    main()
    pg.quit()

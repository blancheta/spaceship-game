#!/usr/bin/python3
from classes.gameobject import GameObject


class Spaceship(GameObject):

    def __init__(self, screen_size):

        super(Spaceship, self).__init__("./resources/images/spaceship.png")
        pos = (
            screen_size[0] / 2 - self.sprite.width / 2,
            screen_size[1] - self.sprite.height
        )
        self.init_pos(pos)

        self.exploding = False
        self.shoot = False
        self.shooting = False

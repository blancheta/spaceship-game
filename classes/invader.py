#!/usr/bin/python3
from classes.gameobject import GameObject


class Invader(GameObject):

    def __init__(self, pos):

        super(Invader, self).__init__("./resources/images/invader.png")
        self.init_pos(pos)

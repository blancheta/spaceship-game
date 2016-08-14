#!/usr/bin/python3
from gameobject import GameObject


class Bullet(GameObject):

	def __init__(self, pos):

		super(Bullet, self).__init__("./images/bullet.png")
		self.init_pos(pos)

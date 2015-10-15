#!/usr/bin/python3
from gameobject import GameObject

class Life(GameObject):

	def __init__(self,pos):

		super(Life,self).__init__("./images/spaceship_mini.png")
		self.init_pos(pos)
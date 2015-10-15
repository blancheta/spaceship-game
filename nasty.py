#!/usr/bin/python3
from gameobject import GameObject

class Nasty(GameObject):

	def __init__(self,pos):

		super(Nasty,self).__init__("./images/ennemy.png")
		self.init_pos(pos)
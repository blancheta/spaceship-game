#!/usr/bin/python3
from gameobject import GameObject

class Spaceship(GameObject):

	def __init__(self,size):

		super(Spaceship,self).__init__("./images/spaceship.png")
		pos = (size[0]/2 - self.image_rect.width/2,size[1] - self.image_rect.height)
		self.init_pos(pos)
		

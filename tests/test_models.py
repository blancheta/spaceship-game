import pytest
import sys
import os
import pygame
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
from classes.spaceship import Spaceship
from classes.life import Life
from classes.nasty import Nasty
from classes.bullet import Bullet


class TestGameModels:

	scr_width = 400
	scr_height = 500

	def setup_method(self, method):
		print("begin")

	def teardown_method(self, method):
		print("end")

	def get_size(self):
		return self.scr_width, self.scr_height

	def check_instance(self, obj, typ):
		assert isinstance(obj, typ)
		assert obj is not None

	# Spaceship

	def test_can_create_a_valid_spaceship(self):
		sp = Spaceship(self.get_size())
		self.check_instance(sp.image, pygame.Surface)

	def test_spaceship_has_a_good_init_position(self):
		size = self.get_size()
		sp = Spaceship(size)
		expect_pos = (
			size[0] / 2 - sp.image_rect.width / 2,
			size[1] - sp.image_rect.height
		)
		assert (sp.image_rect.x, sp.image_rect.y) == expect_pos

	# Life

	def test_can_create_a_valid_life(self):
		life = Life(self.get_size())
		self.check_instance(life.image, pygame.Surface)

	# Nasty

	def test_can_create_a_valid_nasty(self):
		nasty = Nasty(self.get_size())
		self.check_instance(nasty.image, pygame.Surface)

	# Bullet

	def test_can_create_a_valid_bullet(self):
		bullet = Bullet(self.get_size())
		self.check_instance(bullet.image, pygame.Surface)

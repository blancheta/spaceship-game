import pytest
import sys
import os
import pygame
topdir = os.path.join(os.path.dirname(__file__), "..")
sys.path.append(topdir)
from game import Game
from classes.spaceship import Spaceship
from classes.bullet import Bullet


class TestGame:

	scr_width = 400
	scr_height = 500

	def setup_method(self, method):
		print("begin")

	def teardown_method(self, method):
		print("end")

	def check_instance(self, obj, typ):
		assert isinstance(obj, typ)

	def get_game(self, size):
		size = pygame.display.set_mode(size, 0, 32)
		return Game(size)

	# Settings

	def test_game_window_has_a_correct_size(self):
		# height, width
		expected_size = (640, 480)
		game = self.get_game(expected_size)
		assert game.scr_width == expected_size[0]
		assert game.scr_height == expected_size[1]

	def test_background_is_existing(self):
		game = self.get_game((640, 480))
		self.check_instance(game.bg, pygame.Surface)

	def test_game_can_create_a_spaceship(self):
		game = self.get_game((640, 480))
		self.check_instance(game.sp, Spaceship)

	def test_game_can_create_invaders(self):
		game = self.get_game((640, 480))
		game.invaders_number = 10
		self.check_instance(game.invaders, list)
		assert(game.invaders_number == len(game.invaders))

	def test_game_can_create_lifes(self):
		game = self.get_game((640, 480))
		game.lifes_number = 3
		self.check_instance(game.lifes, list)
		assert(game.lifes_number == len(game.lifes))

	def test_game_can_create_a_spaceship_bullet(self):
		game = self.get_game((640, 480))
		self.check_instance(game.bu, Bullet)

	# Dynamic Models
	def test_spaceship_bullet_has_a_good_init_position(self):
		game = self.get_game((640, 480))
		sp = Spaceship(game.size)
		init_pos_bullet = (
			sp.image_rect.x + sp.image_rect.width / 2, sp.image_rect.y
		)

		assert init_pos_bullet == game.init_pos_bullet

#!/usr/bin/python3
import os
import sys
import pygame
from random import randint
from spaceship import *
from bullet import *
from nasty import *
from life import Life
from threading import Thread

pygame.init()


class Game:

	def __init__(self, screen):

		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.size = self.scr_width, self.scr_height

		# Background Game
		self.bg = pygame.image.load("images/starsbackground.jpg")
		self.bg_rect = self.bg.get_rect()

		# Life Bar
		self.lifes = []

		self.game_over = False
		self.victory = False

		self.font = pygame.font.SysFont(None, 100)
		self.label_game_over = self.font.render("Game Over", 1, (255, 255, 255))
		self.label_victory = self.font.render("Victory is yours", 1, (255, 255, 255))

		# Sound Game
		self.laser_sound = pygame.mixer.Sound('sounds/laser_shot.wav')
		self.laser_sound.set_volume(0.2)
		# Clock
		self.clock = pygame.time.Clock()

		# Init Variables
		self.sp = Spaceship(self.size)
		self.init_pos_bullet = (
			self.sp.image_rect.x + self.sp.image_rect.width / 2, self.sp.image_rect.y
		)
		self.bu = Bullet(self.init_pos_bullet)
		self.init_x = 10
		self.invaders = []
		self.escape_selected = False
		self.has_already_chosen = False

		# Shuttle explosion
		self.shuttle_explosion = False

		self.randinvader = ()
		self.ennemybullet = ()

		# Init Invaders
		for i in range(10):
			self.invaders.append(Nasty((self.init_x, 10)))
			self.init_x += 50

		# Init life bar
		self.init_life_x = self.scr_width - 120

		for i in range(3):
			self.lifes.append(Life((self.init_life_x, 0)))
			self.init_life_x += 40

		self.shoot = False
		self.being_shot = False
		self.explosion = False

		# Time Variables
		self.nasty_move_time = 2000
		self.timecount_m = 0
		self.is_moving = False
		self.nasty_being_shot = False
		self.nasty_shoot_time = 2000
		self.timecount = 0

	def run(self):
		mainloop = True
		while mainloop:
			self.clock.tick(50)
			self.screen.fill([0, 0, 0])
			self.screen.blit(self.bg, self.bg_rect)
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()

			# Keyboard Events
			keys = pygame.key.get_pressed()

			if keys[pygame.K_LEFT]:
				self.sp.image_rect.x -= 10
				if self.being_shot is False:
					self.bu.image_rect.x -= 10
			elif keys[pygame.K_RIGHT]:
				self.sp.image_rect.x += 10
				if self.being_shot is False:
					self.bu.image_rect.x += 10
			elif keys[pygame.K_SPACE]:
				self.shoot = True
			elif keys[pygame.K_ESCAPE]:
				mainloop = False
				self.escape_selected = True
				pygame.mixer.music.rewind()

			if self.shoot is True:
				self.laser_sound.play()

				if self.bu.image_rect.y > 0 is self.explosion is False:
					self.being_shot = True
					self.bu.image_rect = self.bu.image_rect.move([0, -6])
				else:
					self.laser_sound.fadeout(1000)
					self.bu.image_rect.x, self.bu.image_rect.y = (
						self.sp.image_rect.x + self.sp.image_rect.width / 2, self.sp.image_rect.y
					)

					self.shoot = False
					self.being_shot = False
					self.explosion = False

			remove_item = []

			if self.timecount_m > self.nasty_move_time:
				self.is_moving = True
			else:
				self.is_moving = False
				self.timecount_m += self.clock.get_time()

			# Invader Colision + Vertical Movement
			print(len(self.invaders))
			if len(self.invaders) > 0:
				for i, invader in enumerate(self.invaders):
					if invader.image_rect.collidepoint(
						self.bu.image_rect.x, self.bu.image_rect.y
					):
						remove_item.append(i)
						self.explosion = True
					else:
						if self.is_moving and not self.game_over:
							invader.image_rect.y += 15
							self.timecount_m = 0

						self.screen.blit(invader.image, invader.image_rect)

			if not self.has_already_chosen:

				# Select random invader
				if len(self.invaders) > 0 and not self.game_over:
					if len(self.invaders) is not 1:
						self.randinvader = self.invaders[randint(1, len(self.invaders) - 1)]
					else:
						self.randinvader = self.invaders[0]

					self.has_already_chosen = True
					posx = self.randinvader.image_rect.x
					width = self.randinvader.image_rect.width
					height = self.randinvader.image_rect.height
					posy = self.randinvader.image_rect.y
					self.ennemybullet = Bullet((posx + width / 2, posy + height))
				else:
					self.victory = True
					self.screen.blit(
						self.label_victory,
						(
							self.scr_width / 2 - self.label_victory.get_rect().width / 2,
							self.scr_height / 2 - self.label_victory.get_rect().height / 2
						)
					)
					mainloop = False

			self.timecount += self.clock.get_time()

			if self.timecount > self.nasty_shoot_time and self.has_already_chosen:
				self.timecount = 0
				self.has_already_chosen = False

			# 	Invader shoot
			elif self.timecount < self.nasty_shoot_time and self.has_already_chosen:
				if self.ennemybullet.image_rect.y < self.scr_height:
					self.ennemybullet.image_rect = self.ennemybullet.image_rect.move([0, 6])
					self.screen.blit(self.ennemybullet.image, self.ennemybullet.image_rect)

			# Remaining lifes
			pygame.draw.rect(
				self.screen, (255, 255, 255), [self.scr_width - 120, 0, 120, 40], 1
			)

			for life in self.lifes:
				self.screen.blit(life.image, life.image_rect)

			# Shuttle Colision
			if self.sp.image_rect.collidepoint(
				self.ennemybullet.image_rect.x, self.ennemybullet.image_rect.y
			) and self.shuttle_explosion is False:
				self.timecount = self.nasty_shoot_time
				self.has_already_chosen = False
				self.shuttle_explosion = True
			else:
				self.screen.blit(self.bu.image, self.bu.image_rect)
				self.screen.blit(self.sp.image, self.sp.image_rect)

			# Remove life if shuttle has exploded
			if self.shuttle_explosion:
				self.shuttle_explosion = False
				if len(self.lifes) > 0:
					self.lifes.pop()
				else:
					self.game_over = True
					self.shuttle_explosion = False

			if self.game_over:
				self.screen.blit(
					self.label_game_over,
					(
						self.scr_width / 2 - self.label_game_over.get_rect().width / 2,
						self.scr_height / 2 - self.label_game_over.get_rect().height / 2
					)
				)
				mainloop = False

			# Remove dead invaders
			for item in remove_item:
				del self.invaders[item]

			pygame.display.flip()

			if self.game_over or self.victory:
				pygame.time.delay(2000)

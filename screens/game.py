#!/usr/bin/python3
import sys
import pygame
from random import randint
from classes.spaceship import Spaceship
from classes.bullet import Bullet
from classes.invader import Invader
from classes.life import Life

pygame.init()


class Game:

	def __init__(self, screen):

		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height
		self.screen_size = self.scr_width, self.scr_height

		# Background Game
		self.bg = pygame.image.load("resources/images/starsbackground.jpg")
		self.bg_rect = self.bg.get_rect()

		# Sound Game
		self.laser_sound = pygame.mixer.Sound('resources/sounds/laser_shot.wav')
		self.laser_sound.set_volume(0.2)

		# Labels
		self.font = pygame.font.SysFont(None, 100)
		self.label_game_over = self.font.render("Game Over", 1, (255, 255, 255))
		self.label_victory = self.font.render("Victory is yours", 1, (255, 255, 255))

		# Life Bar
		self.lifes = []
		self.lifes_number = 3

		# Invaders
		self.invaders = []
		self.invaders_number = 10

		# Spaceship and bullets
		self.spaceship = Spaceship(self.screen_size)
		self.init_pos_bullet = (
			self.spaceship.sprite.x + self.spaceship.sprite.width / 2, self.spaceship.sprite.y
		)
		self.bullet = Bullet(self.init_pos_bullet)

		self.game_over = False
		self.victory = False
		self.escape_selected = False

		# Objects initialisation
		self.randinvader = ()
		self.ennemybullet = ()

		# Invaders
		self.has_already_chosen = False
		# Go down every second
		self.nasty_move_time = 1000
		# Invader shoot duration
		self.nasty_shoot_time = 1000

		self.invaders_moving = False
		self.invader_exploding = False

		# Time Variables
		self.clock = pygame.time.Clock()

		# Timer for invaders vertical moving
		self.timecount_m = 0

		# Time for invader bullet vertical moving
		self.timecount = 0

		# Init Invaders
		self.init_x = 10
		for i in range(self.invaders_number):
			self.invaders.append(Invader((self.init_x, 10)))
			self.init_x += 50

		# Init life bar
		self.init_life_x = self.scr_width - 120

		for i in range(self.lifes_number):
			self.lifes.append(Life((self.init_life_x, 0)))
			self.init_life_x += 40

	def run(self):
		mainloop = True
		while mainloop:
			self.clock.tick(50)
			self.screen.fill([0, 0, 0])
			self.screen.blit(self.bg, self.bg_rect)

			# Close the game when the red cross is clicked
			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					sys.exit()



			# Keyboard Events
			keys = pygame.key.get_pressed()

			if keys[pygame.K_LEFT]:
				self.spaceship.sprite.x -= 10
				if self.spaceship.shooting is False:
					self.bullet.sprite.x -= 10
			elif keys[pygame.K_RIGHT]:
				self.spaceship.sprite.x += 10
				if self.spaceship.shooting is False:
					self.bullet.sprite.x += 10
			elif keys[pygame.K_SPACE]:
				self.spaceship.shoot = True
			elif keys[pygame.K_ESCAPE]:
				# Go back to the game menu
				mainloop = False
				self.escape_selected = True
				pygame.mixer.music.rewind()



			if self.spaceship.shoot is True:
				self.laser_sound.play()

				if self.bullet.sprite.y > 0 and self.invader_exploding is False:
					self.spaceship.shooting = True
					self.bullet.sprite = self.bullet.sprite.move([0, -6])
				else:
					self.laser_sound.fadeout(1000)
					self.bullet.sprite.x, self.bullet.sprite.y = (
						self.spaceship.sprite.x + self.spaceship.sprite.width / 2, self.spaceship.sprite.y
					)

					self.spaceship.shoot = False
					self.spaceship.shooting = False
					self.invader_exploding = False



			item_to_remove = None

			# Invader Colision + Vertical Movement

			# Allow slowly vertical movement
			if self.timecount_m > self.nasty_move_time:
				self.invaders_moving = True
			else:
				self.invaders_moving = False
				self.timecount_m += self.clock.get_time()

			if len(self.invaders) > 0:
				for i, invader in enumerate(self.invaders):
					if invader.sprite.collidepoint(
						self.bullet.sprite.x, self.bullet.sprite.y
					):
						item_to_remove = i
						self.invader_exploding = True
					else:
						if self.invaders_moving and not self.game_over:
							invader.sprite.y += 15
							self.timecount_m = 0

						self.screen.blit(invader.image, invader.sprite)

			# Remove dead invaders:
			if item_to_remove is not None:
				del self.invaders[item_to_remove]


			if not self.has_already_chosen:

				# Select random invader among survivor invaders

				if len(self.invaders) > 0 and not self.game_over:
					if len(self.invaders) is not 1:
						self.randinvader = self.invaders[randint(1, len(self.invaders) - 1)]
					else:
						self.randinvader = self.invaders[0]

					self.has_already_chosen = True
					posx = self.randinvader.sprite.x
					width = self.randinvader.sprite.width
					height = self.randinvader.sprite.height
					posy = self.randinvader.sprite.y
					self.ennemybullet = Bullet((posx + width / 2, posy + height))
				else:
					self.victory = True



			self.timecount += self.clock.get_time()

			# Handle the bullet shot by the random invader

			if self.timecount > self.nasty_shoot_time and self.has_already_chosen:
				self.timecount = 0
				self.has_already_chosen = False

			elif self.timecount < self.nasty_shoot_time and self.has_already_chosen:
				if self.ennemybullet.sprite.y < self.scr_height:
					self.ennemybullet.sprite = self.ennemybullet.sprite.move([0, 6])
					self.screen.blit(self.ennemybullet.image, self.ennemybullet.sprite)






			# Shuttle Displaying and Colision
			if self.spaceship.sprite.collidepoint(
				self.ennemybullet.sprite.x, self.ennemybullet.sprite.y
			) and self.spaceship.exploding is False:
				self.timecount = self.nasty_shoot_time
				self.has_already_chosen = False
				self.spaceship.exploding = True
			else:
				self.screen.blit(self.bullet.image, self.bullet.sprite)
				self.screen.blit(self.spaceship.image, self.spaceship.sprite)

			# Life Management and Displaying
			if self.spaceship.exploding:
				self.spaceship.exploding = False
				if len(self.lifes) > 0:
					self.lifes.pop()
				else:
					self.game_over = True
					self.spaceship.exploding = False

			# Remaining lifes
			pygame.draw.rect(
				self.screen, (255, 255, 255), [self.scr_width - 120, 0, 120, 40], 1
			)

			for life in self.lifes:
				self.screen.blit(life.image, life.sprite)

			if self.victory:
				self.screen.blit(
					self.label_victory,
					(
						self.scr_width / 2 - self.label_victory.get_rect().width / 2,
						self.scr_height / 2 - self.label_victory.get_rect().height / 2
					)
				)

			if self.game_over:
				self.screen.blit(
					self.label_game_over,
					(
						self.scr_width / 2 - self.label_game_over.get_rect().width / 2,
						self.scr_height / 2 - self.label_game_over.get_rect().height / 2
					)
				)


			pygame.display.flip()

			if self.game_over or self.victory:
				pygame.time.delay(4000)
				mainloop = False

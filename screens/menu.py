#!/usr/bin/python3
import sys
import pygame
pygame.init()


class GameMenu:

	def __init__(
		self, screen, items, bg_color=(0, 0, 0), font=None,
		font_size=100, font_color=(255, 255, 255)):

		self.screen = screen
		self.scr_width = self.screen.get_rect().width
		self.scr_height = self.screen.get_rect().height

		# Background Main Menu
		self.bg_color = bg_color
		self.bg_img = pygame.image.load('resources/images/menubackground.jpg')
		self.bg_img_rect = self.bg_img.get_rect()

		# Sound Menu Change
		self.menu_sound = pygame.mixer.Sound('resources/sounds/menu_noise.wav')
		self.valid_menu_sound = pygame.mixer.Sound('resources/sounds/menu_valid_sound.wav')

		# Menu Music
		self.menu_music = pygame.mixer.music.load('resources/sounds/music.mp3')
		pygame.mixer.music.set_volume(0.5)

		# Main Menu
		self.clock = pygame.time.Clock()
		self.font = pygame.font.SysFont(font, font_size)

		self.paddingx = 8
		self.paddingy = 20

		self.start_selected = False
		self.settings_selected = False
		self.quit_select = False

		self.index_selected = 0
		self.current_item = ()
		self.menu_items = []

		# Position menu titles on the menu screen
		for index, item in enumerate(items):
			label = self.font.render(item, 1, font_color)

			width = label.get_rect().width
			height = label.get_rect().height

			posx = (self.scr_width / 2) - (width / 2)

			# t_h: total height of text block
			t_h = len(items) * height

			posy = (self.scr_height / 2) - (t_h / 2) + (index * height)
			self.menu_items.append([item, label, (width, height), (posx, posy)])

	def run(self):

		mainloop = True
		while mainloop:

			# Limit frame speed to 50 FPS
			# self.clock.tick(20)

			if not pygame.mixer.music.get_busy():
				pygame.mixer.music.rewind()
				pygame.mixer.music.play()

			for event in pygame.event.get():
				if event.type == pygame.QUIT:
					mainloop = False
					sys.exit()
				elif event.type == pygame.KEYDOWN:
					if event.key == pygame.K_UP:
						self.menu_sound.play()
						for index, item in enumerate(self.menu_items):
							if self.current_item[0] == item[0]:
								if self.index_selected > 0:
									self.index_selected -= 1
					if event.key == pygame.K_DOWN:
						self.menu_sound.play()
						for index, item in enumerate(self.menu_items):
							if self.current_item[0] == item[0]:
								if self.index_selected < (len(self.menu_items) - 1):
									self.index_selected += 1
					if event.key == pygame.K_RETURN:
						self.valid_menu_sound.play()
						if len(self.current_item) > 0:
							if self.current_item[0] == "Start":
								self.start_selected = True

							elif self.current_item[0] == "Settings":
								self.settings_selected = True

							elif self.current_item[0] == "Quit":
								self.quit_select = True

							pygame.mixer.music.fadeout(1000)
							mainloop = False

			self.current_item = self.menu_items[self.index_selected]

			# Redraw the background
			self.screen.fill(self.bg_color)

			if not self.start_selected or not self.settings_selected:
				self.screen.blit(self.bg_img, self.bg_img_rect)

				for name, label, (width, height), (posx, posy) in self.menu_items:
					self.screen.blit(label, (posx, posy))

				name, label, (width, height), (posx, posy) = self.current_item

				pygame.draw.rect(
					self.screen, (255, 255, 255),
					[
						posx - self.paddingx, posy - self.paddingy,
						width + self.paddingx + self.paddingx, height + self.paddingy
					], 2)

			pygame.display.flip()

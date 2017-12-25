import pygame
from pygame.locals import *

img_ball = pygame.image.load("assets/ball.bmp")

class Actor(pygame.sprite.Sprite):

	def __init__(self, x, y):
		# Call base class constructor
		pygame.sprite.Sprite.__init__(self)

		self.rect = self.image.get_rect().move(x, y)
		self.xvel, self.yvel = 0, 0

	def update(self):
		self.rect = self.rect.move(self.xvel, self.yvel)
		pass

class Player(Actor):
	def __init__(self, x, y):
		self.image = img_ball
		# Call base class constructor
		Actor.__init__(self, x, y)

class Enemy(Actor):
	def __init__(self, x, y):
		self.image = img_ball
		# Call base class constructor
		Actor.__init__(self, x, y)

class Controller:
	""" TODO create virtual joystick base class"""
	def __init__(self):
		self.keystate = {
			pygame.K_LEFT : False,
			pygame.K_RIGHT : False,
			pygame.K_UP : False,
			pygame.K_DOWN : False,
			pygame.K_x : False}
		self.x, self.y = 0, 0

	def update(self, key, type):
		if type == pygame.KEYDOWN:
			state = True
		elif type == pygame.KEYUP:
			state = False
		else:
			return

		self.keystate[key] = state

		if self.keystate[pygame.K_UP]:
			self.y = -1
		elif self.keystate[pygame.K_DOWN]:
			self.y = 1
		else:
			self.y = 0

		if self.keystate[pygame.K_LEFT]:
			self.x = -1
		elif self.keystate[pygame.K_RIGHT]:
			self.x = 1
		else:
			self.x = 0

	def get_xy(self):
		return self.x,self.y

class App:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.size = self.weight, self.height = 640, 400

	def on_init(self):
		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running = True

		# Create some groups for our actors
		self.g_player = pygame.sprite.Group(Player(200,100))
		self.g_enemies = pygame.sprite.Group(Enemy(100,100), Enemy(300,100))

		# Create a virtual joystick object
		self.joy = Controller()

	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
			self.joy.update(event.key, event.type)

	def on_loop(self):
		self.g_player.update()
		self.g_enemies.update()

	def on_render(self):
		self.g_player.draw(self._display_surf)
		self.g_enemies.draw(self._display_surf)
		pygame.display.flip()
		pass

	def on_cleanup(self):
		pygame.quit()

	def on_execute(self):
		if self.on_init() == False:
			self._running = False

		while( self._running ):
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()

if __name__ == "__main__" :
	theApp = App()
	theApp.on_execute()

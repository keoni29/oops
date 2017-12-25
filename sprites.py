import pygame
from pygame.locals import *

# TODO do not use constants for frame-rate

img_ball = pygame.image.load("assets/ball.bmp")
img_ball_inv = pygame.image.load("assets/ball_inv.bmp")

class Actor(pygame.sprite.Sprite):
	"""	Base class for all objects that can move, interact with terrain and eachother """

	def __init__(self, x, y):
		# Call base class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		self.image = self.image_normal
		self.rect = self.image.get_rect().move(x, y)
		self.xvel, self.yvel = 0, 0
		self.inv_frames = 0


	def update(self, xvel = None, yvel = None):
		# Update velocity
		if xvel is not None:
			self.xvel = xvel
		if yvel is not None:
			self.yvel = yvel
		# Update position based on velocity
		self.rect = self.rect.move(self.xvel, self.yvel)

		# Count down invincibility frame counter
		if self.inv_frames:
			if self.inv_frames % 8 > 4:
				self.image = self.image_inv
			else:
				self.image = self.image_normal

			self.inv_frames -= 1

	def hit(self):
		if not self.inv_frames:
			self.inv_frames = self.max_inv_frames

class Player(Actor):
	max_inv_frames = 60

	def __init__(self, x, y):
		self.image_normal = img_ball
		self.image_inv = img_ball_inv
		# Call base class (Actor) constructor
		Actor.__init__(self, x, y)

class Enemy(Actor):
	max_inv_frames = 15

	def __init__(self, x, y):
		self.image_normal = img_ball
		self.image_inv = img_ball_inv
		# Call base class (Actor) constructor
		Actor.__init__(self, x, y)

	def update(self, xvel = None, yvel = None):
		# Call base class (Actor) update method
		Actor.update(self, xvel = xvel, yvel = yvel)

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

		# Create a clock for limiting the framerate
		self.clk = pygame.time.Clock()

	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
			self.joy.update(event.key, event.type)

	def on_loop(self):
		col = pygame.sprite.groupcollide(self.g_player, self.g_enemies, False, False)

		for spr1,spr2 in col.iteritems():
			spr1.hit()

		x,y = self.joy.get_xy()
		self.g_player.sprites()[0].update(x,y)
		self.g_enemies.update()

	def on_render(self):
		self._display_surf.fill(pygame.Color(0,0,0))
		self.g_player.draw(self._display_surf)
		self.g_enemies.draw(self._display_surf)
		pygame.display.flip()
		self.clk.tick(60)

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

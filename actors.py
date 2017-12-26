import pygame

img_ball = pygame.image.load("assets/ball.bmp")
img_ball_inv = pygame.image.load("assets/ball_inv.bmp")

class Actor(pygame.sprite.Sprite):
	"""	Base class for all objects that can move, interact with terrain and eachother """

	def __init__(self, x, y):
		# Call base class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		self.image = self.image_normal
		self.rect = self.image.get_rect().move(x, y)
		self.fx, self.fy = 0.0, 0.0
		self.vx, self.vy = 0.0, 0.0
		self.inv_frames = 0

	def update(self):
		# Count down invincibility frame counter
		if self.inv_frames:
			if self.inv_frames % 8 > 4:
				self.image = self.image_inv
			else:
				self.image = self.image_normal

			self.inv_frames -= 1

	def move_1d(self, dx, dy):
		""" Move along one axis. dx or dy should be 0"""
		if not dx or not dy:
			self.rect = self.rect.move(dx, dy)
		else:
			raise ValueError

	def hit(self):
		if not self.inv_frames:
			self.inv_frames = self.max_inv_frames

class Player(Actor):
	max_inv_frames = 60
	friction = 0.2
	accel = 0.4
	max_speed = 4

	def __init__(self, x, y):
		self.image_normal = img_ball
		self.image_inv = img_ball_inv
		# Call base class (Actor) constructor
		Actor.__init__(self, x, y)

class Enemy(Actor):
	max_inv_frames = 15
	friction = 0.1
	accel = 0.4
	max_speed = 2

	def __init__(self, x, y):
		self.image_normal = img_ball
		self.image_inv = img_ball_inv
		# Call base class (Actor) constructor
		Actor.__init__(self, x, y)

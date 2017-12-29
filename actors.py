import pygame
from projectile import *

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
		self.dx, self.dy = 0.0, 0.0
		self.inv_frames = 0
		self.shoot_frames = 0

		# TODO remove debug statement
		print 'Created ' + str(self)

	def __del__(self):
		# TODO remove debug statement
		print 'Destroyed ' + str(self)

	def update(self):
		# Count down invincibility frame counter
		if self.inv_frames:
			if self.inv_frames % 8 > 4:
				self.image = self.image_inv
			else:
				self.image = self.image_normal

			self.inv_frames -= 1

		if self.shoot_frames:
			self.shoot_frames -= 1

		# Update velocity
		self.vx = max(min(self.vx + self.fx, self.max_speed), -self.max_speed) * self.friction
		self.vy = max(min(self.vy + self.fy, self.max_speed), -self.max_speed) * self.friction

	def control(self, fx, fy):
		self.fx, self.fy = fx, fy

	def move_1d(self, x, y):
		""" Move along one axis. dx or dy should be 0"""
		if not x or not y:
			self.dx = self.vx if x else 0
			self.dy = self.vy if y else 0
			self.rect = self.rect.move(self.dx, self.dy)
		else:
			raise ValueError

	def hit(self):
		if not self.inv_frames:
			self.inv_frames = self.max_inv_frames

	def shoot(self, direction):
		""" Create a projectile moving left or right. """
		p = None
		if not self.shoot_frames:
			self.shoot_frames = self.max_shoot_frames
			if direction < 0:
				hspeed = -4
			else:
				hspeed = 4
			p = Projectile(self.rect.centerx,self.rect.centery,hspeed,0)

		return p

class Player(Actor):
	max_inv_frames = 60
	friction = 0.90
	accel = 0.4
	max_speed = 4
	max_shoot_frames = 20

	def __init__(self, x, y):
		self.image_normal = img_ball
		self.image_inv = img_ball_inv
		# Call base class (Actor) constructor
		Actor.__init__(self, x, y)

class Enemy(Actor):
	max_inv_frames = 15
	friction = 0.90
	accel = 0.4
	max_speed = 2
	max_shoot_frames = 120

	def __init__(self, x, y):
		self.image_normal = img_ball
		self.image_inv = img_ball_inv
		# Call base class (Actor) constructor
		Actor.__init__(self, x, y)

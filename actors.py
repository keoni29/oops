import pygame
from projectile import *

img_player = None
img_player_inv = None
img_enemy = None
img_enemy_inv = None

def loadActorAssets():
	global img_player, img_player_inv, img_enemy, img_enemy_inv

	img_player = pygame.image.load("assets/player.png").convert_alpha()
	img_player_inv = pygame.image.load("assets/player_inv.png").convert_alpha()

	img_enemy = pygame.image.load("assets/enemy.png").convert_alpha()
	img_enemy_inv = pygame.image.load("assets/enemy_inv.png").convert_alpha()


class Actor(pygame.sprite.Sprite):
	"""	Base class for all objects that can move, interact with terrain and eachother """

	def __init__(self, x, y):
		# Call base class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		self.image = self.image_normal
		self.xforce, self.yforce = 0.0, 0.0
		self.xvel, self.yvel = 0.0, 0.0
		self.dx, self.dy = 0.0, 0.0
		self.inv_frames = 0
		self.shoot_frames = 0
		self.x, self.y = x, y
		self.rect = self.image.get_rect().move(self.x, self.y)

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
		self.xvel = max(min(self.xvel + self.xforce, self.max_speed), -self.max_speed) * self.friction
		self.yvel = max(min(self.yvel + self.yforce, self.max_speed), -self.max_speed) * self.friction

		# Reset force after update
		self.xforce, self.yforce = 0.0, 0.0

	def apply_force(self, xforce, yforce):
		self.xforce += xforce
		self.yforce += yforce

	def move_1d(self, xmove, ymove):
		""" Move along one axis """
		if not xmove and ymove:
			self.dx = 0
			self.dy = self.yvel
			self.y += self.dy
		elif xmove and not ymove:
			self.dx = self.xvel
			self.dy = 0
			self.x += self.dx
		else:
			raise ValueError
		
		self.rect.topleft = (self.x, self.y)

	def hit(self):
		if not self.inv_frames:
			self.inv_frames = self.max_inv_frames

	def shoot(self, xfire, yfire):
		""" Create a projectile moving left or right. """
		p = None
		if not self.shoot_frames:
			self.shoot_frames = self.max_shoot_frames
			p = Projectile(self.rect.centerx,self.rect.centery,xfire * 4,yfire * 4)

		return p

class Player(Actor):
	max_inv_frames = 60
	friction = 0.90
	accel = 0.4
	max_speed = 4.0
	max_shoot_frames = 20

	def __init__(self, x, y):
		self.image_normal = img_player
		self.image_inv = img_player_inv
		# Call base class (Actor) constructor
		Actor.__init__(self, x, y)

	def control(self, x, y):
		self.apply_force(x * self.accel, y * self.accel)

class Enemy(Actor):
	max_inv_frames = 15
	friction = 0.95
	accel = 0.4
	max_speed = 5.0
	max_shoot_frames = 120

	def __init__(self, x, y):
		self.image_normal = img_enemy
		self.image_inv = img_enemy_inv
		# Call base class (Actor) constructor
		Actor.__init__(self, x, y)

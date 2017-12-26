import pygame

img_ball = pygame.image.load("assets/ball.bmp")
img_ball_inv = pygame.image.load("assets/ball_inv.bmp")
img_wall = pygame.image.load("assets/wall.bmp")

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
		# Update velocity based on sum of forces
		self.vx = self.fx
		self.vy = self.fy


		# Update position based on velocity
		self.rect = self.rect.move(self.vx, self.vy)

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

class Terrain(pygame.sprite.Sprite):
	""" Base class for immovable, possibly destructable or solid objects.
		Interact with actors """
	def __init__(self, x, y):
		# Call base class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		self.image = img_wall
		self.rect = self.image.get_rect().move(x, y)

class Wall(Terrain):

	def __init__(self, x, y):
		# Call base class (Sprite) constructor
		Terrain.__init__(self, x, y)
		
		pass

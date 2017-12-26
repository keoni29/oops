import pygame

img_wall = pygame.image.load("assets/wall.bmp")
img_spikes = pygame.image.load("assets/spikes.bmp")

class Terrain(pygame.sprite.Sprite):
	""" Base class for immovable, possibly destructable or solid objects.
		Interact with actors """
	def __init__(self, x, y):
		# Call base class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		self.rect = self.image.get_rect().move(x, y)

	def update(self):
		# Base class does nothing
		pass

class Wall(Terrain):
	solid = True
	damage = False
	def __init__(self, x, y):
		self.image = img_wall
		# Call base class (Sprite) constructor
		Terrain.__init__(self, x, y)

		pass

class Spikes(Terrain):
	solid = False
	damage = True
	def __init__(self, x, y):
		self.image = img_spikes
		# Call base class (Sprite) constructor
		Terrain.__init__(self, x, y)

		pass
import pygame

img_wall = pygame.image.load("assets/wall.bmp")

class Terrain(pygame.sprite.Sprite):
	""" Base class for immovable, possibly destructable or solid objects.
		Interact with actors """
	solid = True
	def __init__(self, x, y):
		# Call base class (Sprite) constructor
		pygame.sprite.Sprite.__init__(self)
		self.image = img_wall
		self.rect = self.image.get_rect().move(x, y)

	def update(self):
		# Base class does nothing
		pass

class Wall(Terrain):

	def __init__(self, x, y):
		# Call base class (Sprite) constructor
		Terrain.__init__(self, x, y)

		pass
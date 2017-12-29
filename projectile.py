import pygame
from math import sqrt

img_bubble = None
snd_bubble_shot = None
snd_bubble_pop = None

def loadProjectileAssets():
	global snd_bubble_shot, snd_bubble_pop, img_bubble
	snd_bubble_shot = pygame.mixer.Sound("assets/bubble-shot.wav")
	snd_bubble_pop = pygame.mixer.Sound("assets/bubble-pop.wav")
	img_bubble = pygame.image.load("assets/bubble.png").convert_alpha()

class Projectile(pygame.sprite.Sprite):
	max_distance = 10
	def __init__(self, x, y, xvel, yvel):
		self.image = img_bubble
		self.rect = self.image.get_rect().move(x, y)
		pygame.sprite.Sprite.__init__(self)
		# Center sprite around origin
		self.rect.center = self.rect.topleft
		self.xvel, self.yvel = xvel, yvel
		self.distance = self.max_distance

		snd_bubble_shot.play()
		# TODO remove debug statement
		print 'Created ' + str(self)

	def update(self):
		self.rect = self.rect.move(self.xvel, self.yvel)
		self.distance -= sqrt(self.xvel ** 2 + self.yvel ** 2)

	def __del__(self):
		snd_bubble_pop.play()
		# TODO remove debug statement
		print 'Destroyed ' + str(self)

	def hit(self):
		pass
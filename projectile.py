import pygame

img_bubble = pygame.image.load("assets/bubble.bmp")
snd_bubble_shot = None

def loadProjectileAssets():
	global snd_bubble_shot
	snd_bubble_shot = pygame.mixer.Sound("assets/bubble-shot.wav")

class Projectile(pygame.sprite.Sprite):
	def __init__(self, x, y, xvel, yvel):
		self.image = img_bubble
		self.rect = self.image.get_rect().move(x, y)
		pygame.sprite.Sprite.__init__(self)
		# Center sprite around origin
		self.rect.center = self.rect.topleft
		self.xvel, self.yvel = xvel, yvel

		snd_bubble_shot.play()

	def update(self):
		self.rect = self.rect.move(self.xvel, self.yvel)

	def hit(self):
		pass
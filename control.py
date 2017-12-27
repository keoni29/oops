import pygame

class vJoystick:
	""" TODO create virtual joystick base class"""
	def __init__(self):
		self.keystate = {
			pygame.K_LEFT : False,
			pygame.K_RIGHT : False,
			pygame.K_UP : False,
			pygame.K_DOWN : False,
			pygame.K_x : False}
		self.x, self.y = 0, 0
		self.fire = False

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

		if self.keystate[pygame.K_x]:
			self.fire = True
		else:
			self.fire = False

	def get_xy_fire(self):
		return self.x,self.y,self.fire
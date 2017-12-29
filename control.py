import pygame

class Analog:
	def __init__(self):
		self.x = 0.0
		self.y = 0.0


class vJoystick:
	""" TODO create virtual joystick base class"""
	def __init__(self):
		self.keystate = {
			pygame.K_LEFT : False,
			pygame.K_RIGHT : False,
			pygame.K_UP : False,
			pygame.K_DOWN : False,
			pygame.K_w : False,
			pygame.K_a : False,
			pygame.K_s : False,
			pygame.K_d : False}
		self.analog = [Analog(), Analog()]

	def update(self, key, type):
		if type == pygame.KEYDOWN:
			state = True
		elif type == pygame.KEYUP:
			state = False
		else:
			return

		self.keystate[key] = state

		if self.keystate[pygame.K_UP]:
			self.analog[0].y = -1
		elif self.keystate[pygame.K_DOWN]:
			self.analog[0].y = 1
		else:
			self.analog[0].y = 0

		if self.keystate[pygame.K_LEFT]:
			self.analog[0].x = -1
		elif self.keystate[pygame.K_RIGHT]:
			self.analog[0].x = 1
		else:
			self.analog[0].x = 0

		if self.keystate[pygame.K_w]:
			self.analog[1].y = -1
		elif self.keystate[pygame.K_s]:
			self.analog[1].y = 1
		else:
			self.analog[1].y = 0

		if self.keystate[pygame.K_a]:
			self.analog[1].x = -1
		elif self.keystate[pygame.K_d]:
			self.analog[1].x = 1
		else:
			self.analog[1].x = 0



	def get_analog(self, i):
		return self.analog[i].x,self.analog[i].y
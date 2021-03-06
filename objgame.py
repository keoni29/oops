import pygame
from pygame.locals import *
import math
from loader import *
from control import *
from spritemgr import *

# TODO do not use constants for frame-rate

class App:
	def __init__(self):
		self._running = True
		self._display_surf = None
		self.size = self.weight, self.height = 640, 480

	def on_init(self):
		# Initialize pygame and subsystems
		pygame.mixer.pre_init(44100, -16, 2, 512)
		pygame.init()

		pygame.init()
		self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
		self._running = True

		# Create a virtual joystick
		self.joy = vJoystick()

		loadActorAssets()
		loadProjectileAssets()

		# Load the first room
		# Create a sprite manager and give it the groups
		# we just loaded.
		self.room_loader = RoomLoader()
		groups = self.room_loader.load()
		self.sprite_manager = SpriteManager(self._display_surf)
		self.sprite_manager.load(groups)

		# Create a clock for limiting the framerate
		self.clk = pygame.time.Clock()

	def on_event(self, event):
		if event.type == pygame.QUIT:
			self._running = False
		elif event.type == pygame.KEYUP or event.type == pygame.KEYDOWN:
			self.joy.update(event.key, event.type)

	def on_loop(self):
		# Read the virtual joystick
		x,y = self.joy.get_analog(0)
		xfire,yfire = self.joy.get_analog(1)
		self.sprite_manager.update(x, y, xfire, yfire)

	def on_render(self):
		self._display_surf.fill(pygame.Color(0,0,0))
		self.sprite_manager.draw()
		pygame.display.flip()
		self.clk.tick(60)
		#print self.clk.get_fps()

	def on_cleanup(self):
		pygame.quit()

	def on_execute(self):
		if self.on_init() == False:
			self._running = False

		while( self._running ):
			for event in pygame.event.get():
				self.on_event(event)
			self.on_loop()
			self.on_render()
		self.on_cleanup()

if __name__ == "__main__" :
	theApp = App()
	theApp.on_execute()

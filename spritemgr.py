import pygame

class SpriteManager:

	def __init__(self, surface):
		self._display_surf = surface
		self.g_terrain = None
		self.g_player = None
		self.g_enemies = None
	def load(self, groups):
		self.g_terrain, self.g_player, self.g_enemies = groups

	def update(self, x, y):

		# Control and update the player character
		p1 = self.g_player.sprites()[0]
		p1.fx, p1.fy = x ,y
		p1.update()

		self.g_enemies.update()

		# Collision checking between player and enemies
		col = pygame.sprite.groupcollide(self.g_player, self.g_enemies, False, False)
		for spr1,spr2 in col.iteritems():
			# Player gets damaged when touching an enemy
			spr1.hit()

		# Collision checking between actors and terrain
		col = pygame.sprite.groupcollide(self.g_player, self.g_enemies, False, False)
	
	def draw(self):
		self.g_player.draw(self._display_surf)
		self.g_enemies.draw(self._display_surf)
		self.g_terrain.draw(self._display_surf)
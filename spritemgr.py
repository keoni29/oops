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
		# Collision checking between player and enemies
		collision = pygame.sprite.groupcollide(self.g_player, self.g_enemies, False, False)
		for player,enemy in collision.iteritems():
			# Player gets damaged when touching an enemy
			player.hit()

		# Control and update the player character
		#TODO update enemies
		#self.g_enemies.update()

		# Move in one axis at a time, then do colision checks for both axis
		for dx,dy in [(x,0),(0,y)]:
			for player in self.g_player.sprites():
				player.move_1d(dx, dy)

			collision = pygame.sprite.groupcollide(self.g_player, self.g_terrain, False, False)
			for player,terrain in collision.iteritems():
				for t in terrain:
					if t.solid:
						if dx > 0: # Moving right; Hit the left side of the wall
							player.rect.right = t.rect.left
						if dx < 0: # Moving left; Hit the right side of the wall
							player.rect.left = t.rect.right
						if dy > 0: # Moving down; Hit the top side of the wall
							player.rect.bottom = t.rect.top
						if dy < 0: # Moving up; Hit the bottom side of the wall
							player.rect.top = t.rect.bottom
					else:
						# Pass straight through non-solid terrain for now
						pass
				if t.damage:
					player.hit()

		# Update all player characters
		for player in self.g_player.sprites():
			player.update()

	def draw(self):
		self.g_terrain.draw(self._display_surf)
		self.g_enemies.draw(self._display_surf)
		self.g_player.draw(self._display_surf)
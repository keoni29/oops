import pygame

class SpriteManager:

	def __init__(self, surface):
		self._display_surf = surface
		self.g_terrain = None
		self.g_players = None
		self.g_enemies = None
		self.g_projectiles = None
	def load(self, groups):
		self.g_terrain, self.g_players, self.g_enemies = groups
		self.g_actors = pygame.sprite.Group(self.g_players.sprites() + self.g_enemies.sprites())
		self.g_projectiles = pygame.sprite.Group()
	def update(self, x, y, fire):
		# Todo use interface for allowing sprites to register new sprites with sprite manager
		# Update all player characters
		for player in self.g_players.sprites():
			player.control(x, y)

			if fire:
				p = player.shoot(x)
				if p:
					self.g_projectiles.add(p)
		
		###
		# Update game objects
		self.g_actors.update()
		self.g_projectiles.update()

		###
		# Actors <> Terrain
		# Move in one axis at a time, then do colision checks for both axis
		for dx,dy in [(0,1),(1,0)]:

			for actor in self.g_actors.sprites():
				actor.move_1d(dx,dy)

			collision = pygame.sprite.groupcollide(self.g_actors, self.g_terrain, False, False)
			for actor,terrain in collision.iteritems():
				for t in terrain:
					if t.solid:
						if actor.dx > 0: # Moving right; Hit the left side of the wall
							actor.rect.right = t.rect.left
							actor.vx = 0
						if actor.dx < 0: # Moving left; Hit the right side of the wall
							actor.rect.left = t.rect.right
							actor.vx = 0
						if actor.dy > 0: # Moving down; Hit the top side of the wall
							actor.rect.bottom = t.rect.top
							actor.vy = 0
						if actor.dy < 0: # Moving up; Hit the bottom side of the wall
							actor.rect.top = t.rect.bottom
							actor.vy = 0
					#else:
					#	# Pass straight through non-solid terrain for now
					#	pass
				if t.damage:
					player.hit()

		###
		# Players <> Enemies
		collision = pygame.sprite.groupcollide(self.g_players, self.g_enemies, False, False)
		for player,enemy in collision.iteritems():
			# Player gets damaged when touching an enemy
			player.hit()

		###
		# Projectiles <> Terrain
		# Projectile gets destroyed when touching solid terrain
		collision = pygame.sprite.groupcollide(self.g_projectiles, self.g_terrain, False, False)
		for projectile,terrain in collision.iteritems():
			for t in terrain:
				if t.solid:
					projectile.kill()
					projectile = None
					break
				#else:
				#	# Pass straight through non-solid terrain
				#	pass

		###
		# Projectiles <> Enemies
		# Destroy projectile when touching an enemy
		collision = pygame.sprite.groupcollide(self.g_enemies, self.g_projectiles, False, True)
		for enemy, projectiles in collision.iteritems():
			# Enemy gets damaged when hit by a projectile
			for p in projectiles:
				enemy.hit()


	def draw(self):
		self.g_terrain.draw(self._display_surf)
		self.g_enemies.draw(self._display_surf)
		self.g_players.draw(self._display_surf)
		self.g_projectiles.draw(self._display_surf)
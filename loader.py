import pygame

from actors import *
from terrain import *

class RoomLoader:
	# Holds the level layout in a list of strings.
	level = [
	"WWWWWWWWWWWWWWWWWWWW",
	"W E                W",
	"W         WWWWWW   W",
	"W   WWWW       W   W",
	"W   W        WWWW  W",
	"W WWW  WWWW        W",
	"W   W     W W  E   W",
	"W   W     W   WWW WW",
	"W   WWW WWW   W W  W",
	"W     W   W P W W  W",
	"WWW   W   WWWWW W  W",
	"W W      WW        W",
	"W W   WWWW   WWW   W",
	"W     W        W   W",
	"WWWWWWWWWWWWWWWWWWWW",
	]

	def load(self):
		g_terrain = pygame.sprite.Group()
		g_player = pygame.sprite.Group()
		g_enemies = pygame.sprite.Group()
		# Parse the level string above. W = wall, E = exit
		x = y = 0
		for row in self.level:
			for col in row:
				if col == "W":
					g_terrain.add(Wall(x, y))
				if col == "E":
					g_enemies.add(Enemy(x, y))
				if col == "P":
					g_player.add(Player(x, y))
				x += 32
			y += 32
			x = 0
		return (g_terrain, g_player, g_enemies)
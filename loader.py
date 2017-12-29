import pygame

from actors import *
from projectile import *
from terrain import *

class RoomLoader:
	# Holds the level layout in a list of strings.
	level2 = [
	"WWWWWWWWWWWWWWWWWWWW",
	"W E                W",
	"W         SSSSSW   W",
	"W   WWWW       W   W",
	"W   W        WWWW  W",
	"W WWW  WWWW        W",
	"W   W  S  W W  E   W",
	"W   W     W   WWW WW",
	"W   WWW WWW   W W  W",
	"W     W   W P W W  W",
	"WWW   W   WWWWW W  W",
	"W W      WW        W",
	"W W   WWWW   WWW   W",
	"W     W        W   W",
	"WWWWWWWWWWWWWWWWWWWW",
	]

	level = [
	"WWWWWWWWWWWWWWWWWWWW",
	"WW               W W",
	"W   E             WW",
	"W   WWWW    WWWW   W",
	"W                  W",
	"W                  W",
	"W                  W",
	"W         P        W",
	"W                  W",
	"W     WW           W",
	"W     WW     E     W",
	"W   WWWW           W",
	"WW         E       W",
	"W W               WW",
	"WWWWWWWWWWWWWWWWWWWW",
	]

	# level = [
	# "WWWWWWWWWWWWWWWWWWWW",
	# "WPEPPPPPPPPPPPPPPPPW",
	# "WPPPPPPPPPSSSSSWPPPW",
	# "WPPPWWWWPPPPPPPWPPPW",
	# "WPPPWPPPPPPPPWWWWPPW",
	# "WPWWWPPWWWWPPPPPPPPW",
	# "WPPPWPPSPPWPWPPEPPPW",
	# "WPPPWPPPPPWPPPWWWPWW",
	# "WPPPWWWPWWWPPPWPWPPW",
	# "WPPPPPWPPPWPPPWPWPPW",
	# "WWWPPPWPPPWWWWWPWPPW",
	# "WPWPPPPPPWWPPPPPPPPW",
	# "WPWPPPWWWWPPPWWWPPPW",
	# "WPPPPPWPPPPPPPPWPPPW",
	# "WWWWWWWWWWWWWWWWWWWW",
	# ]

	def load(self):
		g_terrain = pygame.sprite.Group()
		g_players = pygame.sprite.Group()
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
					g_players.add(Player(x, y))
				if col == "S":
					g_terrain.add(Spikes(x, y))
				x += 32
			y += 32
			x = 0
		return (g_terrain, g_players, g_enemies)
import items, enemies

class MapTile:
	def __init__(self, x, y, directions):
		self.x = x
		self.y = y
		self.directions = directions

	def room_text(self):
		raise NotImplementedError()

	def modify_player(self):
		raise NotImplementedError()

class StartingRoom(MapTile):
	def __init__(self, x, y, directions):
		super().__init__(x, y, directions)

	def room_text(self):
		return """
		You step into the dungeon.
		You head the enterence close behind you, no turning back now

		There are you can {}.
		""".format(self.directions)

	def modify_player(self):
		#This room does not affect the player
		pass

class GoldRoom
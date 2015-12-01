class Enemy:
	def __init__(self, name, hp, damage):
		self.name = name
		self.hp = hp
		self.damage = damage

	def is_alive(self):
		return self.hp > 0

class Goblin(Enemy):
	def __init__(self):
		super().__init__(name='Goblin', hp=10, damage=2)

class GiantSpider(Enemy):
	def __init__(self):
		super().__init__(name='Giant Spider', hp=20, damage=2)

#Some code borrowed from http://letstalkdata.com/2014/08/how-to-write-a-text-adventure-in-python/

class Item:
	def __init__(self, name, description, value):
		self.name = name
		self.description = description
		self.value = value

	def __str__(self):
		return '\n======\n{}\n{}\nValue: {}\n'.format(self.name, self.description, self.value)

class Gold(Item):
	def __init__(self, amt):
		self.amt = amt
		super().__init__(name='Gold',
						 description='A coin with a {} written on it'.format(self.amt),
						 value=self.amt)


class Weapon(Item):
	def __init__(self, name, description, value, damage):
		self.damage = damage
		super().__init__(name=name, description=description, value=value)

	def __str__(self):
		return '\n======\n{}\n{}\nValue: {}\nDamage: {}\n'.format(self.name, self.description, self.value, self.damage)

class Knife(Weapon):
	def __init__(self):
		super().__init__(name='Knife',
						 description='Just a simple kife',
						 value=5,
						 damage=1)

class Sword(Weapon):
	def __init__(self):
		super().__init__(name='Sword',
						 description='A basic sword',
						 value=10,
						 damage=3)


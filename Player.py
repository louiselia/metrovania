class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.friction = -2
		self.accseleration = .5
		self.velocity = 0

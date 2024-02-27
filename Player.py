import pygame.math


class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.RIGHT_KEY = False
		self.LEFT_KEY = False
		self.facingleft = False
		self.isjumping = False
		self.onground = False
		self.gravity = 2.
		self.friction = -2
		self.position = pygame.math.Vector2(0,0)
		self.velocity = pygame.math.Vector2(0, 0)
		self.accseleration = pygame.math.Vector2(0, self.gravity)


	def horizontalmove(self):
		pass


	def verticalmove(self):
		pass


	def update(self):
		self.horizontalmove()
		self.verticalmove()
import pygame.math


class Player:
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.
		self.
		self.
		self.isjumping = False
		self.onground = False
		self.gravity = 2.
		self.friction = -2
		self.position = pygame.math.Vector2(0,0)
		self.accseleration = .5
		self.velocity = 0

	def horizontalmove(self):
		pass


	def verticalmove(self):
		pass


	def update(self):
		self.horizontalmove()
		self.verticalmove()
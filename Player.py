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
		self.acceleration = pygame.math.Vector2(0, self.gravity)


	def horizontalmove(self, dt):
		self.acceleration.x = 0
		if self.LEFT_KEY:
			self.acceleration.x -= 0.3
		elif self.RIGHT_KEY:
			self.acceleration.x += 0.3
		self.acceleration += self.velocity * self.friction
		self.velocity = self.acceleration * dt

		self.position.x = self.velocity.x * dt + (self.acceleration * 0.5) * (dt * dt)
		self.x = self.position.x

	def verticalmove(self):
		pass


	def update(self):
		self.horizontalmove()
		self.verticalmove()
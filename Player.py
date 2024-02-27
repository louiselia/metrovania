import pygame


class Player():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.RIGHT_KEY = False
		self.LEFT_KEY = False
		self.facingleft = False
		self.isjumping = False
		self.onground = False
		self.gravity = 0.35
		self.friction = -0.12
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

		self.position.x = self.velocity.x * dt + (self.acceleration.x * 0.5) * (dt * dt)
		self.x = self.position.x

	def verticalmove(self, dt):
		pass


	def update(self, dt):
		self.horizontalmove(dt)
		self.verticalmove(dt)


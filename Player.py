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
		self.friction = 0.59
		self.position = pygame.math.Vector2(0, 0)
		self.velocity = pygame.math.Vector2(0, 0)
		self.acceleration = pygame.math.Vector2(0, self.gravity)

	def horizontalmove(self, dt):
		self.acceleration.x = 0

		if self.LEFT_KEY:

			self.acceleration.x -= 0.3

		elif self.RIGHT_KEY:

			self.acceleration.x += 0.3
		elif True:
			self.velocity.x = 0

		self.acceleration.x += self.acceleration.x * self.friction
		self.velocity.x += self.acceleration.x * dt

		if abs(self.velocity.x) < 0.1:
			self.velocity.x = 0

		self.position.x += self.velocity.x * dt / 2 + (self.velocity.x * 0.5 * dt**2)
		self.x = self.position.x


	def verticalmove(self, dt):
		pass


	def update(self, dt):
		self.horizontalmove(dt)
		self.verticalmove(dt)

'''		if self.RIGHT_KEY == False and self.LEFT_KEY:
			if abs(self.velocity.x) > 0:
				self.velocity.x /= 0.5
				if abs(self.velocity.x) < 0.1:
					self.velocity.x = 0'''

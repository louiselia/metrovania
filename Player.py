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
		self.friction = 0.39
		self.position = pygame.math.Vector2(0, 0)
		self.velocity = pygame.math.Vector2(0, 0)
		self.acceleration = pygame.math.Vector2(0, self.gravity)


	def Left(self):

		if self.acceleration.x > 1:
			self.acceleration.x -= 1
		else:
			self.acceleration.x -= 0.8

	def Right(self):

		if self.acceleration.x < -1:
			self.acceleration.x += 1
		else:
			self.acceleration.x += 0.8

	def horizontalmove(self, dt):
		self.acceleration.x = 0
		if self.LEFT_KEY:
			self.Left()

		if self.RIGHT_KEY:
			self.Right()

		if self.LEFT_KEY == False and self.RIGHT_KEY == False:
			self.velocity.x /= 10

		self.acceleration.x = self.acceleration.x * self.friction
		self.velocity.x += self.acceleration.x * dt

		if abs(self.velocity.x) < .1:
			self.velocity.x = 0
		if abs(self.acceleration.x) < .1:
			self.acceleration.x = 0

		print(self.velocity.x, self.acceleration.x)

		self.position.x += self.velocity.x * dt + (self.velocity.x * 0.5 * dt**2)
		self.x = self.position.x


	def verticalmove(self, dt):
		pass


	def update(self, dt):
		self.horizontalmove(dt)
		self.verticalmove(dt)

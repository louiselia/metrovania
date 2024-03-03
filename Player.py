import pygame


class Player():
	def __init__(self, x, y):
		self.x = x
		self.y = y
		self.RIGHT_KEY = False
		self.LEFT_KEY = False

		self.facingleft = False
		self.isjumping = False
		self.onground = True

		self.inscreenpos = pygame.math.Vector2(self.x, self.y)

		self.gravity = 0.55
		self.friction = 0.39
		self.position = pygame.math.Vector2(self.x, self.y)
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

		self.position.x += self.velocity.x * dt #+ (self.acceleration.x * 0.5 * dt**2)
		self.x = self.position.x

	def update(self, dt):
		self.horizontalmove(dt)
		self.verticalmove(dt)

	def verticalmove(self, dt):
		self.velocity.y += self.acceleration.y * dt
		if self.velocity.y > 7:
			self.velocity.y = 7
		self.position.y += self.velocity.y * dt + (self.acceleration.y * .5) * (dt * dt)

		if self.position.y > self.inscreenpos.y:
			self.on_ground = True
			self.velocity.y = 0
			self.position.y = self.inscreenpos.y
		self.y = self.position.y

	def jump(self):
		if self.on_ground:
			self.isjumping = True
			self.velocity.y -= 8
			self.on_ground = False


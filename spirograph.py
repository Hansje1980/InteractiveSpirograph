import math
import pygame


class Spirograph:
	def __init__(self, x, y, size, R, r, d):
		self.x = x
		self.y = y
		self.size = size
		self.color = (255, 0, 0)
		self.R = R
		self.r = r
		self.d = d
		self.rotation = 0
		self.rotation_speed = 0.1

	def draw(self, screen):
		x = (self.R - self.r) * math.cos(self.rotation) + self.d * math.cos(
				((self.R - self.r) / self.r) * self.rotation
				) + self.x
		y = (self.R - self.r) * math.sin(self.rotation) - self.d * math.sin(
				((self.R - self.r) / self.r) * self.rotation
				) + self.y
		pygame.draw.circle(screen, self.color, (int(x), int(y)), self.size)

	def update(self):
		self.rotation += self.rotation_speed

	def change_color(self, color):
		self.color = color

	def change_speed(self, speed):
		self.rotation_speed = speed

	def change_size(self, size):
		self.size

	def collidepoint(self, pos):
		rect = pygame.Rect(self.x - self.size, self.y - self.size, self.size * 2, self.size * 2)
		return rect.collidepoint(pos)
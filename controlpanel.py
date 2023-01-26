import pygame


class ControlPanel:
	def __init__(self, x, y, width, height):
		self.x = x
		self.y = y
		self.width = width
		self.height = height
		self.color = (255, 255, 255)
		self.spirographs = []

	def draw(self, screen):
		pygame.draw.rect(screen, self.color, (self.x, self.y, self.width, self.height))

	def add_spirograph(self, spirograph):
		self.spirographs.append(spirograph)

	def update(self):
		for spirograph in self.spirographs:
			spirograph.update()

	def handle_events(self, events):
		for event in events:
			if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
				for spirograph in self.spirographs:
					if spirograph.collidepoint(event.pos):
						spirograph.change_color()
			elif event.type == pygame.MOUSEBUTTONDOWN and event.button == 3:
				for spirograph in self.spirographs:
					if spirograph.collidepoint(event.pos):
						spirograph.change_speed()
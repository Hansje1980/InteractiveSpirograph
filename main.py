import py
import pygame

# Create screen variable
screen = None


def check_resolution():
	# Get the current screen resolution
	info = pygame.display.Info()
	width, height = info.current_w, info.current_h
	global screen
	screen = pygame.display.set_mode((width, height), pygame.FULLSCREEN)


# Initialize Pygame
pygame.init()

# Check the resolution and update the size of the window
check_resolution()

# Set the caption of the main window
pygame.display.set_caption("Spirograph Drawing Application")

# Set the background color of the main window
screen.fill((255, 255, 255))

# Create a start button
start_button = pygame.Rect(50, 50, 100, 50)

# Update the display
pygame.display.flip()


def main_loop():
	running = True
	drawing = False
	while running:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				running = False
			# Add a button for start drawing
			elif event.type == py
				if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
					if start_button.collidepoint(event.pos):
						drawing = True
				elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
					drawing = False
			if drawing:
				start_drawing()
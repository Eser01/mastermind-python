import pygame
from pygame.locals import *

SCREENRECT = Rect(0, 0, 640, 480)

# Initialize pygame
if pygame.get_sdl_version()[0] == 2:
    pygame.mixer.pre_init(44100, 32, 2, 1024)
pygame.init()
if pygame.mixer and not pygame.mixer.get_init():
    print("Warning, no sound")
    pygame.mixer = None

# Set the display mode
winstyle = 0  # |FULLSCREEN
bestdepth = pygame.display.mode_ok(SCREENRECT.size, winstyle, 32)
screen = pygame.display.set_mode(SCREENRECT.size, winstyle, bestdepth)

clock = pygame.time.Clock()

flag = True
while flag:
	for event in pygame.event.get():
		print(event)
		if event.type == 12:
			flag = False
		elif event.type == 3 and event.key == 27:
			flag = False
	clock.tick(40)

pygame.time.wait(100)
pygame.quit()
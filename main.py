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
		if event.type == pygame.QUIT:
			flag = False
		elif event.type == pygame.KEYUP and event.key == 27:
			flag = False
	clock.tick(40)

# QUIT None
# ACTIVEEVENT gain, state
# KEYDOWN unicode, key, mod
# KEYUP key, mod
# MOUSEMOTION pos, rel, buttons
# MOUSEBUTTONUP pos, button
# MOUSEBUTTONDOWN pos, button
# JOYAXISMOTION joy, axis, value
# JOYBALLMOTION joy, ball, rel
# JOYHATMOTION joy, hat, value
# JOYBUTTONUP joy, button
# JOYBUTTONDOWN joy, button
# VIDEORESIZE size, w, h
# VIDEOEXPOSE None
# USEREVENT Code

pygame.time.wait(100)
pygame.quit()
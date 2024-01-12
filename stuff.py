import pygame
import sys
	


WIDTH, HEIGHT = 1536, 960
BG = (50, 50, 50)

#level
lvl_map = ('background.png', (1000, 900))#second half is map size

#settings
playerspeed = 1


def exit_proc():
	pygame.quit()
	quit()

class mkpos():
	x = 0
	y = 0
	def __init__(self, xi, yi):
		x = xi
		y = yi

class player():
	def __init__(self, x, y):
		self.pos = mkpos(x, y)
	


#main

pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')


# Set up the sprite
sprite = pygame.sprite.Sprite()
sprite.image = pygame.image.load('test.png')
sprite.rect = sprite.image.get_rect()
sprite.rect.center = (WIDTH / 2, HEIGHT / 2)


#Background
background = pygame.sprite.Sprite()
background.image = pygame.image.load(lvl_map[0]).convert_alpha()
background.rect = background.image.get_rect()
background.rect.center = (WIDTH / 2, HEIGHT / 2)

running = True
while running:

	#update background
	screen.fill(BG)
	screen.blit(background.image, background.rect)

	#show player image
	screen.blit(sprite.image, sprite.rect)

	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			running = False

	# Update the display
	pygame.display.update()

    # Keyboard input
	keys = pygame.key.get_pressed()

	if keys[pygame.K_a]: # Left arrow key
		background.rect.x += playerspeed
	if keys[pygame.K_d]: # Right arrow key
		background.rect.x -= playerspeed
	if keys[pygame.K_w]: # Up arrow key
		background.rect.y += playerspeed
	if keys[pygame.K_s]: # Down arrow key
		background.rect.y -= playerspeed


exit_proc()
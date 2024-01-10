import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 1536, 960
BG = (50, 50, 50)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)

class SpriteSheet():
	def __init__(self, image):
		self.sheet = image

	def get_image(self, frame, width, height, scale, colour):
		image = pygame.Surface((width, height))
		image.blit(self.sheet, (0, 0), ((frame * width), 0, width, height))
		image = pygame.transform.scale(image, (width * scale, height * scale))
		image.set_colorkey(colour)

		return image

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spritesheets')

sprite_image = pygame.image.load('test.png')
sprite_sheet = SpriteSheet(sprite_image)
sprite = pygame.sprite.Sprite()
sprite.image = sprite_image
# Set up the sprite's position
sprite.rect = sprite.image.get_rect()
sprite.rect.center = (WIDTH / 2, HEIGHT / 2)



background_image = pygame.image.load('background.png').convert_alpha()
background = pygame.sprite.Sprite()
background.image = background_image
background.rect = sprite.image.get_rect()
background.rect.center = (0, 0)


frame_0 = sprite_sheet.get_image(0, 24, 24, 3, BLACK)


run = True
while run:

	#update background
	screen.fill(BG)
	screen.blit(background.image, background.rect)

	#show frame image
	screen.blit(frame_0, (sprite.rect.x, sprite.rect.y))
	#event handler
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False

	# Update the display
	pygame.display.update()

    # Keyboard input
	keys = pygame.key.get_pressed()

	if keys[pygame.K_a]: # Left arrow key
		background.rect.x += 1
	if keys[pygame.K_d]: # Right arrow key
		background.rect.x -= 1
	if keys[pygame.K_w]: # Up arrow key
		background.rect.y += 1
	if keys[pygame.K_s]: # Down arrow key
		background.rect.y -= 1

    # Keep the sprite within the screen
	sprite.rect.x = max(sprite.rect.x, 0)
	sprite.rect.x = min(sprite.rect.x, WIDTH - sprite.rect.width)
	sprite.rect.y = max(sprite.rect.y, 0)
	sprite.rect.y = min(sprite.rect.y, HEIGHT - sprite.rect.height)

pygame.quit()
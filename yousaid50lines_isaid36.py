import pygame
import sys
pygame.init()
WIDTH, HEIGHT = 1536, 960
BG = (50, 50, 50)
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Spritesheets')
sprite_image = pygame.image.load('test.png')
sprite = pygame.sprite.Sprite()
sprite.image = sprite_image
sprite.rect = sprite.image.get_rect()
sprite.rect.center = (WIDTH / 2, HEIGHT / 2)
background_image = pygame.image.load('background.png').convert_alpha()
background = pygame.sprite.Sprite()
background.image = background_image
background.rect = sprite.image.get_rect()
background.rect.center = (0, 0)
run = True
while run:
	screen.fill(BG)
	screen.blit(background.image, background.rect)
	screen.blit(sprite_image, (sprite.rect.x, sprite.rect.y))
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			run = False
	pygame.display.update()
	keys = pygame.key.get_pressed()
	if keys[pygame.K_a]: # Left arrow key
		background.rect.x += 1
	if keys[pygame.K_d]: # Right arrow key
		background.rect.x -= 1
	if keys[pygame.K_w]: # Up arrow key
		background.rect.y += 1
	if keys[pygame.K_s]: # Down arrow key
		background.rect.y -= 1
pygame.quit()
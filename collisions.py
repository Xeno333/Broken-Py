#janky collisions now added with a enemy

import pygame
import sys

WIDTH, HEIGHT = 1700, 960
BG = (50, 50, 50)
center_area_size = 50
playerspeed = 1
running = True

#level
lvl_map = ('background.png', (1000, 900))#second half is map size

#settings
def exit_proc():
	pygame.quit()
	quit()

#main
pygame.init()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Game')

# Set up the sprite
sprite = pygame.sprite.Sprite()
sprite.image = pygame.image.load('test.png')
sprite.rect = sprite.image.get_rect()
sprite.rect.center = (WIDTH / 2, HEIGHT / 2)

#collisionblock
collide = pygame.sprite.Sprite()
collide.image = pygame.image.load('enemy.png')
collide.rect = collide.image.get_rect()
collide.rect.center = (WIDTH / 3, HEIGHT / 3)

#Background
background = pygame.sprite.Sprite()
background.image = pygame.image.load(lvl_map[0]).convert_alpha()
background.rect = background.image.get_rect()
background.rect.center = (WIDTH / 2, HEIGHT / 2)

while running:
	
	#update background
    screen.fill(BG)
    screen.blit(background.image, background.rect)
    screen.blit(collide.image, collide.rect)
	
	#show player image
    screen.blit(sprite.image, sprite.rect)

    if collide.rect.colliderect(sprite.rect):
         pygame.quit()
	
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
        collide.rect.x += playerspeed
    if keys[pygame.K_d]: # Right arrow key
        background.rect.x -= playerspeed
        collide.rect.x -= playerspeed
    if keys[pygame.K_w]: # Up arrow key
        background.rect.y += playerspeed
        collide.rect.y += playerspeed
    if keys[pygame.K_s]: # Down arrow key
        background.rect.y -= playerspeed
        collide.rect.y -= playerspeed

pygame.quit()
       

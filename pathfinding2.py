import pygame
import sys
import math
import random

playerspeed = 5

# Initialize Pygame
pygame.init()

# Set up display
width, height = 2000, 1000
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Direct Path")

# Colors
black = (0, 0, 0)
red = (255, 0, 0)

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move_towards(self, target, speed):
        angle = math.atan2(target.rect.centery - self.rect.centery, target.rect.centerx - self.rect.centerx)
        speed = speed
        self.rect.x += speed * math.cos(angle)
        self.rect.y += speed * math.sin(angle)

# Create sprites
sprite1 = Sprite(100, 100, black)
sprite2 = Sprite(700, 500, red)
sprite3 = Sprite(random.randint(1, 500), random.randint(1, 500), black)

background = pygame.sprite.Sprite()
background.image = pygame.image.load('background2.png')
background.rect = background.image.get_rect()
background.rect.center = (0, 0)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2, sprite3)

# Main loop
clock = pygame.time.Clock()

running = True
while running:

    screen.blit(background.image, background.rect)

    if sprite1.rect.colliderect(sprite2.rect):
         pygame.quit()

    if sprite3.rect.colliderect(sprite2.rect):
         pygame.quit()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move sprite1 towards sprite2
    sprite1.move_towards(sprite2, 3)
    sprite3.move_towards(sprite2, 4)

    # Draw
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: # Left arrow key
        sprite2.rect.x -= playerspeed    
    if keys[pygame.K_d]: # Right arrow key
        sprite2.rect.x += playerspeed 
    if keys[pygame.K_w]: # Up arrow key
        sprite2.rect.y -= playerspeed
    if keys[pygame.K_s]: # Down arrow key
        sprite2.rect.y += playerspeed

    sprite2.rect.x = max(sprite2.rect.x, 0)
    sprite2.rect.x = min(sprite2.rect.x, width - sprite2.rect.width)
    sprite2.rect.y = max(sprite2.rect.y, 0)
    sprite2.rect.y = min(sprite2.rect.y, height - sprite2.rect.height)

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

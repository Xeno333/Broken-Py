import pygame
import sys
import math
import random
import time

playerspeed = 5

# Initialize Pygame
pygame.init()

# Set up display
width, height = 1500, 960
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Direct Path")

# Colors
black = (0, 0, 0)
red = (255, 0, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.alive = True

    def move_towards(self, target, speed):
        if self.alive == True:
            angle = math.atan2(target.rect.centery - self.rect.centery, target.rect.centerx - self.rect.centerx)
            self.rect.x += speed * math.cos(angle)
            self.rect.y += speed * math.sin(angle)

# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, color, target_position):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.target_position = target_position

    def move_towards(self, speed):
        angle = math.atan2(-90, 0)
        self.rect.x += speed * math.cos(angle)
        self.rect.y += speed * math.sin(angle)

# Create sprites
sprite1 = Sprite(100, 100, black)
sprite2 = Sprite(700, 500, red)
sprite3 = Sprite(480, 940, yellow)

projectiles = pygame.sprite.Group()

background = pygame.sprite.Sprite()
background.image = pygame.image.load('background2.png')
background.rect = background.image.get_rect()
background.rect.center = (0, 0)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2, sprite3, projectiles)

# Main loop
clock = pygame.time.Clock()

running = True
last_shot_time = pygame.time.get_ticks()

while running:

    keys = pygame.key.get_pressed()
    screen.blit(background.image, background.rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    if sprite1.alive == True:
        if sprite3.rect.colliderect(sprite1.rect):
         sprite1.alive = False

    if sprite1.alive == True:
     if sprite3.rect.colliderect(sprite2.rect):
          sprite2.alive = False

    if sprite1.alive and sprite2.alive == True:
        sprite1.move_towards(sprite3, 3)
        sprite2.move_towards(sprite1, 3)


    if keys[pygame.K_w]:
        projectile_initial_position = (sprite3.rect.centerx, sprite3.rect.centery)
        projectile = Projectile(*projectile_initial_position, blue, (sprite2.rect.centerx, sprite2.rect.centery))
        projectiles.add(projectile)
    # Move projectiles towards their initial target position
    for projectile in projectiles:
        projectile.move_towards(5)

    # Check if projectiles have reached their target positions
    for projectile in projectiles:
        distance_to_target = math.hypot(projectile.target_position[0] - projectile.rect.centerx,
                                        projectile.target_position[1] - projectile.rect.centery)
        if distance_to_target < 5:  # Adjust this threshold as needed
            projectiles.remove(projectile)

    # Check for collision between projectiles and sprite2
    if sprite1.alive == True:
      if pygame.sprite.spritecollide(sprite2, projectiles, True):
          sprite2.remove(all_sprites)


    if sprite1.alive == True:
     if pygame.sprite.spritecollide(sprite1, projectiles, True):
         sprite1.remove(all_sprites)
    # Draw
    all_sprites.draw(screen)
    projectiles.draw(screen)

    # Update display
    pygame.display.flip()

    if keys[pygame.K_a]:  # Left arrow key
        sprite3.rect.x -= playerspeed
    if keys[pygame.K_d]:  # Right arrow key
        sprite3.rect.x += playerspeed

    sprite2.rect.x = max(sprite2.rect.x, 0)
    sprite2.rect.x = min(sprite2.rect.x, width - sprite2.rect.width)
    sprite2.rect.y = max(sprite2.rect.y, 0)
    sprite2.rect.y = min(sprite2.rect.y, height - sprite2.rect.height)

    sprite1.rect.x = max(sprite1.rect.x, 0)
    sprite1.rect.x = min(sprite1.rect.x, width - sprite1.rect.width)
    sprite1.rect.y = max(sprite1.rect.y, 0)
    sprite1.rect.y = min(sprite1.rect.y, height - sprite1.rect.height)

    sprite3.rect.x = max(sprite3.rect.x, 0)
    sprite3.rect.x = min(sprite3.rect.x, width - sprite3.rect.width)
    sprite3.rect.y = max(sprite3.rect.y, 0)
    sprite3.rect.y = min(sprite3.rect.y, height - sprite3.rect.height)

    # Cap the frame rate
    clock.tick(60)
# Quit Pygame
pygame.quit()
sys.exit()
#add a timer and if the player is still alive at the end they win
#the longer the spend in the center the higher the score they got
#
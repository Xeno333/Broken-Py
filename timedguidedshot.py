import pygame
import sys
import math
import random

playerspeed = 5
projectile_duration = 5000  # 5 seconds in milliseconds
spawn_interval = 1000  # 2 seconds in milliseconds

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

    def move_towards(self, target, speed):
        angle = math.atan2(target.rect.centery - self.rect.centery, target.rect.centerx - self.rect.centerx)
        self.rect.x += speed * math.cos(angle)
        self.rect.y += speed * math.sin(angle)

# Projectile class
class Projectile(pygame.sprite.Sprite):
    def __init__(self, x, y, color, target):
        super().__init__()
        self.image = pygame.Surface((10, 10))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.target = target
        self.creation_time = pygame.time.get_ticks()  # Store the creation time

    def move_towards(self, speed):
        angle = math.atan2(self.target.rect.centery - self.rect.centery, self.target.rect.centerx - self.rect.centerx)
        self.rect.x += speed * math.cos(angle)
        self.rect.y += speed * math.sin(angle)

# Create sprites
sprite1 = Sprite(100, 100, black)
sprite2 = Sprite(700, 500, red)
sprite3 = Sprite(random.randint(1, 500), random.randint(1, 500), yellow)

background = pygame.sprite.Sprite()
background.image = pygame.image.load('background2.png')
background.rect = background.image.get_rect()
background.rect.center = (0, 0)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2, sprite3)

# Main loop
clock = pygame.time.Clock()
running = True
projectile_spawn_timer = pygame.time.get_ticks()  # Initialize projectile spawn timer

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
    sprite3.move_towards(sprite2, 1)

    # Spawn new projectile every 2 seconds
    current_time = pygame.time.get_ticks()
    if current_time - projectile_spawn_timer > spawn_interval:
        projectile = Projectile(sprite3.rect.centerx, sprite3.rect.centery, blue, sprite2)
        all_sprites.add(projectile)
        projectile_spawn_timer = current_time  # Reset the projectile spawn timer

    # Move all projectiles towards sprite2
    for projectile in all_sprites.sprites():
        if isinstance(projectile, Projectile):
            projectile.move_towards(5)

            # Check for collision between projectile and sprite2
            if projectile.rect.colliderect(sprite2.rect):
                pygame.quit()

    # Check if projectile duration has elapsed
    for projectile in all_sprites.sprites():
        if isinstance(projectile, Projectile):
            if current_time - projectile.creation_time > projectile_duration:
                # Remove the projectile
                all_sprites.remove(projectile)

    # Draw
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]:  # Left arrow key
        sprite2.rect.x -= playerspeed
    if keys[pygame.K_d]:  # Right arrow key
        sprite2.rect.x += playerspeed
    if keys[pygame.K_w]:  # Up arrow key
        sprite2.rect.y -= playerspeed
    if keys[pygame.K_s]:  # Down arrow key
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

#to add a goal coins could randomly spawn and when player collides with them a counter goes up if they reach x num they win
#could also add another player who is controlled by arrow keys and has its own counter so first to 10 or last to die wins
#
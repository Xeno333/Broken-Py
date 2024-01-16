#to do list:
#make emeny # increase  every round

import pygame
import sys
import math
import random

# some variables
playerspeed = 5
score = 0

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

# Initialize time variables for projectile rate limiting
projectile_cooldown = 500  # 1000 milliseconds (1 second)
last_shot_time = pygame.time.get_ticks()

# new wave class
def spawn_new_wave():
    global sprite1, sprite2, score
    sprite1.alive = True
    sprite2.alive = True
    sprite1 = Sprite(random.randint(1, 135) * 10, 100, black)
    sprite2 = Sprite(random.randint(1, 135) * 10, 500, red)
    all_sprites.add(sprite1, sprite2)
    score += 50

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)
        self.alive = True
        self.direction = 1  # Initial direction (1 for right, -1 for left)

    def move_invasion_pattern(self, speed, screen_width):
        if self.alive:
            self.rect.x += speed * self.direction

            # Check if the sprite has hit the edge of the screen
            if self.rect.right > screen_width or self.rect.left < 0:
                self.rect.y += 60  # Move down by 30 pixels
                self.direction *= -1  # Change direction

            self.rect.x += speed * self.direction

    # ... (your existing code)

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
sprite1 = Sprite(random.randint(1, 15) * 10, 100, black)
sprite2 = Sprite(random.randint(1, 15) * 10, 500, red)
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

while running:
    keys = pygame.key.get_pressed()
    screen.blit(background.image, background.rect)

    # event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # collisions
    if sprite1.alive == True:
        if sprite3.rect.colliderect(sprite1.rect):
            sprite3.alive = False
            sprite3.remove(all_sprites)
            playerspeed = 0
    if sprite2.alive == True:
        if sprite3.rect.colliderect(sprite2.rect):
            sprite3.alive = False
            sprite3.remove(all_sprites)
            playerspeed = 0

    # kill command
    if sprite1.alive == True:
        sprite1.move_invasion_pattern(3, width)
    if sprite2.alive == True:
        sprite2.move_invasion_pattern(3, width)

    # shoot projectiles with rate limit
    if sprite3.alive == True and keys[pygame.K_w]:
        current_time = pygame.time.get_ticks()
        if current_time - last_shot_time >= projectile_cooldown:
            projectile_initial_position = (sprite3.rect.centerx, sprite3.rect.centery)
            projectile = Projectile(*projectile_initial_position, blue, (sprite2.rect.centerx, sprite2.rect.centery))
            projectiles.add(projectile)
            last_shot_time = current_time

    # Move projectiles towards their initial target position
    for projectile in projectiles:
        projectile.move_towards(5)

    # Check if projectiles have reached their target position (don't think this is necessary)
    for projectile in projectiles:
        distance_to_target = math.hypot(projectile.target_position[0] - projectile.rect.centerx,
                                        projectile.target_position[1] - projectile.rect.centery)
        if distance_to_target < 5:  # Adjust this threshold as needed
            projectiles.remove(projectile)

    # Check for collision between projectiles and sprites
    if sprite2.alive == True:
        if pygame.sprite.spritecollide(sprite2, projectiles, True):
            sprite2.alive = False
            sprite2.remove(all_sprites)
            score += 10  # Increase score by 10 when an enemy is killed
    if sprite1.alive == True:
        if pygame.sprite.spritecollide(sprite1, projectiles, True):
            sprite1.alive = False
            sprite1.remove(all_sprites)
            score += 10  # Increase score by 10 when an enemy is killed

    # starts a new wave of enemies
    if not sprite1.alive and not sprite2.alive:
        # Spawn a new wave of enemies
        spawn_new_wave()

    # Draws sprites to the screen
    all_sprites.draw(screen)
    projectiles.draw(screen)

    # Displays score
    font = pygame.font.Font(None, 36)
    score_text = font.render(f"Score: {score}", True, red)
    screen.blit(score_text, (10, 10))

    # Updates the display
    pygame.display.flip()

    # Move the player
    if keys[pygame.K_a]:
        sprite3.rect.x -= playerspeed
    if keys[pygame.K_d]:
        sprite3.rect.x += playerspeed

    # keeps player on the screen
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

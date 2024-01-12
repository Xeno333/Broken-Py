import pygame
import sys
import math

# Initialize Pygame
pygame.init()

# Set up display
width, height = 800, 600
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sprite Direct Path")

# Colors
white = (255, 255, 255)
red = (255, 0, 0)

# Sprite class
class Sprite(pygame.sprite.Sprite):
    def __init__(self, x, y, color):
        super().__init__()
        self.image = pygame.Surface((50, 50))
        self.image.fill(color)
        self.rect = self.image.get_rect()
        self.rect.center = (x, y)

    def move_towards(self, target):
        angle = math.atan2(target.rect.centery - self.rect.centery, target.rect.centerx - self.rect.centerx)
        speed = 5
        self.rect.x += speed * math.cos(angle)
        self.rect.y += speed * math.sin(angle)

# Create sprites
sprite1 = Sprite(100, 100, white)
sprite2 = Sprite(700, 500, red)

all_sprites = pygame.sprite.Group()
all_sprites.add(sprite1, sprite2)

# Main loop
clock = pygame.time.Clock()

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Move sprite1 towards sprite2
    sprite1.move_towards(sprite2)

    # Draw
    screen.fill((0, 0, 0))
    all_sprites.draw(screen)

    # Update display
    pygame.display.flip()

    # Cap the frame rate
    clock.tick(60)

# Quit Pygame
pygame.quit()
sys.exit()

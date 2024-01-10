import pygame
import sys

# Initialize pygame
pygame.init()

# Set up some constants
WIDTH, HEIGHT = 640, 480
WHITE = (255, 255, 255)
RED = (255, 0, 0)

# Set up the display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption('Red Dot')

# Load an image and create a sprite
sprite_image = pygame.image.load('doux.png')
sprite = pygame.sprite.Sprite()
sprite.image = sprite_image

# Set up the sprite's position
sprite.rect = sprite.image.get_rect()
sprite.rect.center = (WIDTH / 2, HEIGHT / 2)

# Game loop
while True:
    # Fill the screen with white
    screen.fill(WHITE)

    # Draw the sprite
    screen.blit(sprite.image, sprite.rect)

    # Update the display
    pygame.display.flip()

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    # Keyboard input
    keys = pygame.key.get_pressed()
    if keys[pygame.K_a]: # Left arrow key
        sprite.rect.x -= 10
    if keys[pygame.K_d]: # Right arrow key
        sprite.rect.x += 10
    if keys[pygame.K_w]: # Up arrow key
        sprite.rect.y -= 10
    if keys[pygame.K_s]: # Down arrow key
        sprite.rect.y += 10

    # Keep the sprite within the screen
    sprite.rect.x = max(sprite.rect.x, 0)
    sprite.rect.x = min(sprite.rect.x, WIDTH - sprite.rect.width)
    sprite.rect.y = max(sprite.rect.y, 0)
    sprite.rect.y = min(sprite.rect.y, HEIGHT - sprite.rect.height)
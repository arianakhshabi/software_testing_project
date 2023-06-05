import pygame
import os

# Construct the image path
color = 'white'
name = 'pawn'
image_path = os.path.join(f'F:/software_testing/img/{color} {name}.png')

# Initialize Pygame
pygame.init()

# Set the video mode
screen_width = 400
screen_height = 400
screen = pygame.display.set_mode((screen_width, screen_height))

# Create a Pygame surface
surface = pygame.Surface((100, 100))

# Load and convert the image
img = pygame.image.load(image_path).convert()

# Scale the image to the desired size
img = pygame.transform.scale(img, (80, 80))

# Blit the image onto the surface
surface.blit(img, (10, 10))

# Blit the surface onto the screen
screen.blit(surface, (0, 0))

# Update the display
pygame.display.update()

# Wait for a few seconds to observe the image
pygame.time.wait(3000)

# Quit Pygame
pygame.quit()

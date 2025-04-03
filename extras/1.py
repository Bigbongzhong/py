import pygame
import sys
import random
from pygame.locals import *

# Initialize pygame
pygame.init()

# Screen dimensions
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("3D Python Roaming Simulation")

# Colors
WHITE = (255, 255, 255)
GREEN = (0, 128, 0)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

# Load background image
background_image = pygame.image.load("extras/wal.jpg")
background_image = pygame.transform.scale(background_image, (WIDTH, HEIGHT))

# Snake properties
snake_pos = [WIDTH // 2, HEIGHT // 2]
snake_segments = [[WIDTH // 2, HEIGHT // 2]]
snake_size = 20
snake_speed = 5
snake_length = 5

# Obstacles
obstacles = [[random.randint(0, WIDTH - snake_size), random.randint(0, HEIGHT - snake_size)] for _ in range(10)]

# Food properties
food_pos = [random.randint(0, (WIDTH - snake_size) // snake_size) * snake_size,
            random.randint(0, (HEIGHT - snake_size) // snake_size) * snake_size]
food_spawned = True

# Main loop
clock = pygame.time.Clock()
running = True

while running:
    for event in pygame.event.get():
        if event.type == QUIT:
            running = False

    # Movement keys
    keys = pygame.key.get_pressed()
    if keys[K_UP]:
        snake_pos[1] -= snake_speed
    if keys[K_DOWN]:
        snake_pos[1] += snake_speed
    if keys[K_LEFT]:
        snake_pos[0] -= snake_speed
    if keys[K_RIGHT]:
        snake_pos[0] += snake_speed

    # Update snake segments
    snake_segments.insert(0, list(snake_pos))
    if len(snake_segments) > snake_length:
        snake_segments.pop()

    # Check if snake eats food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        snake_length += 1
        food_spawned = False

    # Spawn new food if eaten
    if not food_spawned:
        food_pos = [random.randint(0, (WIDTH - snake_size) // snake_size) * snake_size,
                    random.randint(0, (HEIGHT - snake_size) // snake_size) * snake_size]
        food_spawned = True

    # Draw background
    screen.blit(background_image, (0, 0))

    # Draw food
    pygame.draw.rect(screen, GREEN, (*food_pos, snake_size, snake_size))

    # Draw obstacles
    for obs in obstacles:
        pygame.draw.rect(screen, RED, (*obs, snake_size, snake_size))

    # Draw snake with circular segments
    for i, segment in enumerate(snake_segments):
        color = (0, 255 - i * 10, 0)  # Gradient effect
        pygame.draw.circle(screen, color, (segment[0] + snake_size // 2, segment[1] + snake_size // 2), snake_size // 2)

        # Dynamic shadow
        shadow_offset = 10 + i * 2
        pygame.draw.circle(screen, BLACK, (segment[0] + snake_size // 2 + shadow_offset, segment[1] + snake_size // 2 + shadow_offset), snake_size // 2, 1)

    pygame.display.flip()
    clock.tick(30)

pygame.quit()
sys.exit()

import pygame
import numpy as np
import random
from moviepy.video.io.ImageSequenceClip import ImageSequenceClip

# Initialize Pygame
pygame.init()

# Video settings
WIDTH, HEIGHT = 800, 600  # 4:3 aspect ratio
FPS = 60  # Frames per second
DURATION = 120  # Duration in seconds (reduced for testing)
NUM_FRAMES = DURATION * FPS

# Set up display (off-screen rendering)
screen = pygame.Surface((WIDTH, HEIGHT))

# Load image
input_image = input("Enter the image file name: ")
logo = pygame.image.load(input_image)  # Replace with your image file

# Resize the image while maintaining its aspect ratio
SIZE = 150  # Max size for width or height
aspect_ratio = logo.get_width() / logo.get_height()  # Original aspect ratio

if aspect_ratio > 1:
    new_width = SIZE
    new_height = int(SIZE / aspect_ratio)
else:
    new_height = SIZE
    new_width = int(SIZE * aspect_ratio)

logo = pygame.transform.scale(logo, (new_width, new_height))
logo_rect = logo.get_rect()

# Speed settings
BASE_SPEED = 2  # Base speed
SPEED_VARIATION = 0.5  # Speed variation range (+/- this value)
speed = [
    BASE_SPEED + random.uniform(-SPEED_VARIATION, SPEED_VARIATION),
    BASE_SPEED + random.uniform(-SPEED_VARIATION, SPEED_VARIATION),
]

# Store frames
frames = []

for _ in range(NUM_FRAMES):
    screen.fill((0, 0, 0))  # Black background
    screen.blit(logo, logo_rect)

    # Move Logo
    logo_rect.x += speed[0]
    logo_rect.y += speed[1]

    # Bounce off walls with random speed and direction variation
    if logo_rect.left <= 0 or logo_rect.right >= WIDTH:
        speed[0] = -speed[0] * random.uniform(0.8, 1.2)  # Random speed and direction variation
    if logo_rect.top <= 0 or logo_rect.bottom >= HEIGHT:
        speed[1] = -speed[1] * random.uniform(0.8, 1.2)  # Random speed and direction variation

    # Save frame as NumPy array
    frame = pygame.surfarray.array3d(screen)
    frame = np.transpose(frame, (1, 0, 2))  # Transpose to match MoviePy's expected format
    frames.append(frame)

# Convert frames to video using ImageSequenceClip
clip = ImageSequenceClip(frames, fps=FPS)
output_file = input_image.split(".")[0] + ".mp4"
clip.write_videofile(output_file, codec="libx264", fps=FPS)

pygame.quit()
print("Video saved as:", output_file)
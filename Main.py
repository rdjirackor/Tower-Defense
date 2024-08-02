import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up the display
width, height = 800, 600
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Road in Field")

# Colors
green = (34, 139, 34)  # Field color
gray = (105, 105, 105) # Road color

# Main drawing function
def draw_scene():
    # Fill the background with the field color
    window.fill(green)

    # Define road points for a curved road
    road_points = [
        (200, height),
        (250, 400),
        (350, 300),
        (450, 200),
        (400, 0)
    ]

    # Draw the road
    pygame.draw.lines(window, gray, False, road_points, 80)

    # Update the display
    pygame.display.flip()

# Main loop
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    draw_scene()

# Quit Pygame
pygame.quit()
sys.exit()

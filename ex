import pygame
import sys

pygame.init()
size = (640, 480)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pygame Example")

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    screen.fill((30, 144, 255))  # Dodger Blue background
    pygame.display.flip()

pygame.quit()
sys.exit()

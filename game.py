import pygame
import random
import sys

# Initialize pygame
pygame.init()

# Screen settings
WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pygame Shooter")

# Clock
clock = pygame.time.Clock()
FPS = 60

# Colors
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)

# Player
player_width = 50
player_height = 40
player_x = WIDTH // 2 - player_width // 2
player_y = HEIGHT - player_height - 10
player_speed = 6

# Bullets
bullets = []
bullet_speed = 8

# Enemies
enemies = []
enemy_speed = 3
spawn_delay = 30
spawn_timer = 0

# Score
score = 0
font = pygame.font.SysFont(None, 36)

# Game state
game_over = False


def draw_text(text, x, y, color=WHITE):
    img = font.render(text, True, color)
    screen.blit(img, (x, y))


def reset_game():
    global bullets, enemies, score, game_over, player_x
    bullets = []
    enemies = []
    score = 0
    game_over = False
    player_x = WIDTH // 2 - player_width // 2


# Main loop
running = True
while running:
    clock.tick(FPS)
    screen.fill(BLACK)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullets.append(
                    pygame.Rect(player_x + player_width // 2 - 3, player_y, 6, 10)
                )
            if event.key == pygame.K_r and game_over:
                reset_game()

    keys = pygame.key.get_pressed()

    if not game_over:
        # Player movement
        if keys[pygame.K_LEFT] and player_x > 0:
            player_x -= player_speed
        if keys[pygame.K_RIGHT] and player_x < WIDTH - player_width:
            player_x += player_speed

        # Spawn enemies
        spawn_timer += 1
        if spawn_timer >= spawn_delay:
            spawn_timer = 0
            enemies.append(
                pygame.Rect(
                    random.randint(0, WIDTH - 40),
                    -40,
                    40,
                    40
                )
            )

        # Move bullets
        for bullet in bullets[:]:
            bullet.y -= bullet_speed
            if bullet.y < 0:
                bullets.remove(bullet)

        # Move enemies
        for enemy in enemies[:]:
            enemy.y += enemy_speed
            if enemy.y > HEIGHT:
                game_over = True

        # Collisions
        for enemy in enemies[:]:
            for bullet in bullets[:]:
                if enemy.colliderect(bullet):
                    enemies.remove(enemy)
                    bullets.remove(bullet)
                    score += 1
                    break

    # Draw player
    pygame.draw.rect(
        screen,
        GREEN,
        (player_x, player_y, player_width, player_height)
    )

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, WHITE, bullet)

    # Draw enemies
    for enemy in enemies:
        pygame.draw.rect(screen, RED, enemy)

    # UI
    draw_text(f"Score: {score}", 10, 10)

    if game_over:
        draw_text("GAME OVER", WIDTH // 2 - 100, HEIGHT // 2 - 20, RED)
        draw_text("Press R to Restart", WIDTH // 2 - 120, HEIGHT // 2 + 20)

    pygame.display.flip()

pygame.quit()
sys.exit()


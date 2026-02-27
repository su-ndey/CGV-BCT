import pygame
import random
import sys
import numpy as np

pygame.mixer.pre_init(44100, -16, 2, 512)
pygame.init()
pygame.mixer.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Ultimate Shooter PRO")

clock = pygame.time.Clock()
FPS = 60
font = pygame.font.SysFont(None, 36)

# 🔊 REAL SOUND GENERATOR
def generate_sound(frequency, duration=0.2, volume=0.5):
    sample_rate = 44100
    t = np.linspace(0, duration, int(sample_rate * duration), False)
    wave = np.sin(frequency * t * 2 * np.pi)
    audio = wave * (2**15 - 1) * volume
    audio = audio.astype(np.int16)
    stereo_audio = np.column_stack((audio, audio))
    return pygame.sndarray.make_sound(stereo_audio)

# ✅ Initialize sounds
shoot_sound = generate_sound(880, duration=0.1, volume=0.3)
explosion_sound = generate_sound(220, duration=0.3, volume=0.5)

# 🔹 Load sprites using absolute paths
def load_sprite_absolute(path, size=(50,50)):
    img = pygame.image.load(path).convert_alpha()
    return pygame.transform.scale(img, size)

# Replace these paths with the actual absolute paths on your PC
player_img = load_sprite_absolute(r"C:\Users\ASUS\OneDrive\Desktop\CGV-BCT\Darshil(HCE081BCT009)\project\player.jpg")
ufo_img = load_sprite_absolute(r"C:\Users\ASUS\OneDrive\Desktop\CGV-BCT\Darshil(HCE081BCT009)\project\ufo.jpg")
background_img = load_sprite_absolute(r"C:\Users\ASUS\OneDrive\Desktop\CGV-BCT\Darshil(HCE081BCT009)\project\background.jpg", size=(WIDTH, HEIGHT))

def reset_game():
    player = pygame.Rect(375, 520, 50, 50)
    bullets = []
    enemies = []
    particles = []
    score = 0
    lives = 3
    game_over = False
    shake = 0
    flash = 0
    return player, bullets, enemies, particles, score, lives, game_over, shake, flash

player, bullets, enemies, particles, score, lives, game_over, shake, flash = reset_game()

player_speed = 7
enemy_spawn_delay = 1000
last_spawn = pygame.time.get_ticks()

running = True

while running:
    clock.tick(FPS)
    offset_x = random.randint(-shake, shake)
    offset_y = random.randint(-shake, shake)

    # Draw background or flash
    if flash > 0:
        screen.fill((255, 100, 0))
        flash -= 1
    else:
        screen.blit(background_img, (0, 0))

    # Event handling
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not game_over:
                bullets.append(pygame.Rect(player.centerx - 3, player.top, 6, 18))
                shoot_sound.play()
            if event.key == pygame.K_r and game_over:
                player, bullets, enemies, particles, score, lives, game_over, shake, flash = reset_game()
                last_spawn = pygame.time.get_ticks()
                enemy_spawn_delay = 1000

    keys = pygame.key.get_pressed()
    if not game_over:
        if keys[pygame.K_LEFT] and player.left > 0:
            player.x -= player_speed
        if keys[pygame.K_RIGHT] and player.right < WIDTH:
            player.x += player_speed

    if pygame.time.get_ticks() - last_spawn > enemy_spawn_delay and not game_over:
        enemies.append(pygame.Rect(random.randint(0, WIDTH - 50), -50, 50, 50))
        last_spawn = pygame.time.get_ticks()

    # Move bullets
    for bullet in bullets[:]:
        bullet.y -= 12
        if bullet.bottom < 0:
            bullets.remove(bullet)

    # Move enemies
    for enemy in enemies[:]:
        enemy.y += 4
        if enemy.top > HEIGHT:
            enemies.remove(enemy)
            lives -= 1
            shake = 10
        elif enemy.colliderect(player):
            enemies.remove(enemy)
            lives -= 1
            shake = 20
            flash = 5

    # Bullet collision
    for bullet in bullets[:]:
        for enemy in enemies[:]:
            if bullet.colliderect(enemy):
                explosion_sound.play()
                shake = 25
                flash = 6

                for _ in range(40):
                    if len(particles) < 200:
                        particles.append({
                            "x": enemy.centerx,
                            "y": enemy.centery,
                            "dx": random.uniform(-6, 6),
                            "dy": random.uniform(-6, 6),
                            "life": random.randint(20, 40),
                            "color": random.choice([
                                (255,0,0), (255,165,0), (255,255,0), (255,255,255)
                            ])
                        })

                bullets.remove(bullet)
                enemies.remove(enemy)
                score += 10
                if enemy_spawn_delay > 200:
                    enemy_spawn_delay -= 5
                break

    # Update particles
    for p in particles[:]:
        p["x"] += p["dx"]
        p["y"] += p["dy"]
        p["life"] -= 1
        p["dx"] *= 0.95
        p["dy"] *= 0.95
        if p["life"] <= 0:
            particles.remove(p)

    if shake > 0:
        shake -= 1
    if lives <= 0:
        game_over = True

    # Draw player sprite
    screen.blit(player_img, (player.x + offset_x, player.y + offset_y))

    # Draw bullets
    for bullet in bullets:
        pygame.draw.rect(screen, (255, 255, 255), bullet.move(offset_x, offset_y))

    # Draw UFO enemies
    for enemy in enemies:
        screen.blit(ufo_img, (enemy.x + offset_x, enemy.y + offset_y))

    # Draw particles
    for p in particles:
        pygame.draw.circle(screen, p["color"], (int(p["x"]+offset_x), int(p["y"]+offset_y)), 4)

    # HUD
    score_text = font.render("Score: " + str(score), True, (255,255,255))
    lives_text = font.render("Lives: " + str(lives), True, (255,255,255))
    screen.blit(score_text, (10, 10))
    screen.blit(lives_text, (650, 10))

    if game_over:
        over_text = font.render("GAME OVER", True, (255,0,0))
        restart_text = font.render("Press R to Restart", True, (255,255,255))
        screen.blit(over_text, (300, 260))
        screen.blit(restart_text, (270, 300))

    pygame.display.flip()

pygame.quit()
sys.exit()
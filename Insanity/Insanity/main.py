import pygame
import random
from Player import Player

pygame.init()
window = pygame.display.set_mode((600, 600))
clock = pygame.time.Clock()

running = True

# player variables
p = Player()

sprite_group = pygame.sprite.Group()
sprite_group.add(p)
p.rect.y = 550
score = 0

right = False
left = False
game_over = False

# texts and fonts
font = pygame.font.SysFont("bold", 30)
game_over_font = pygame.font.SysFont("bold", 60)

# object variables
speed = 2
object_ = pygame.Rect(30, 30, 30, 30)
object_blue = pygame.Rect(30, 30, 30, 30)

grass = pygame.Rect(30, 30, 600, 30)
grass.x = 0.5
grass.y = 580

chaos = False
pygame.mixer.music.load("sounds/Doom music.wav")


while running:
    if score > 300:
        chaos = True
    if score == 300:
        speed += 7
        object_.width += 10
        pygame.mixer.music.play()

    elif score == 600:
        speed += 3
        object_.width += 20
        score += 200
    elif score == 700:
        speed += 8
        object_.width += 80
    elif score == 900:
        speed += 4
        object_.width += 100
    elif score == 1500:
        speed += 6
        object_.width += 150

    if p.rect.x <= -2:
        p.rect.x = 600
    elif p.rect.x >= 600:
        p.rect.x = 1

    if game_over is True:
        window.fill("red")
        score = 0
        game_over_label = game_over_font.render(f"Game Over :(", False, (0, 0, 0))
        window.blit(game_over_label, (150, 30))
        object_.width = 30
        speed = 0
        chaos = False
        pygame.mixer.music.pause()

    if game_over is False:
        score_label = font.render(f"Score: {score}", False, (0, 0, 0))
        score += 1

    if object_.colliderect(p):
        game_over = True

    if right is True:
        p.rect.x += 5
    if left is True:
        p.rect.x -= 5

    if object_.y > 600:
        object_.x = random.randint(1, 550)
        object_.y = 1

    object_.y += 3 + speed

    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            quit()

        if events.type == pygame.KEYDOWN:
            if events.key == pygame.K_d:
                right = True
            if events.key == pygame.K_LEFT:
                left = True
            if events.key == pygame.K_RIGHT:
                right = True
            if events.key == pygame.K_a:
                left = True
            if events.key == pygame.K_SPACE and game_over is True:
                game_over = False

        if events.type == pygame.KEYUP:
            if events.key == pygame.K_d:
                right = False
            if events.key == pygame.K_a:
                left = False
            if events.key == pygame.K_LEFT:
                left = False
            if events.key == pygame.K_RIGHT:
                right = False

    pygame.display.update()
    if chaos is False:
        window.fill("white")
    if chaos is True:
        pygame.mixer.music.unpause()
        window.fill("red")

    window.blit(score_label, (30, 30))
    pygame.draw.rect(window, "dark red", object_)
    pygame.draw.rect(window, "green", grass)
    sprite_group.draw(window)
    clock.tick(60)

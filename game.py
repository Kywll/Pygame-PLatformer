import pygame
import sys

pygame.init()


window_height = 500
window_width = 600

screen = pygame.display.set_mode((window_width, window_height))

clock = pygame.time.Clock()

sample_block = pygame.Surface((2500, 500))
character = pygame.Surface((((50, 50))))

character_x = 250
character_y = 300

speed = 4


x_velocity = [False, False]
y_velocity = [False, False]

player_rect = character.get_rect(topleft = (character_x, character_y))
sample_rect = sample_block.get_rect(topleft = (0, 350))


run = True

while run:
    screen.fill((0, 255, 255))
    screen.blit(sample_block, sample_rect)
    screen.blit(character, player_rect)
    
    
    sample_block.fill(('Red'))

    
    player_rect.x += (x_velocity[0] - x_velocity[1]) * speed
    player_rect.y += (y_velocity[1] - y_velocity[0]) * speed
    
    if player_rect.x < 0:
        player_rect.x = 549
    if player_rect.x > 550:
        player_rect.x = 1

    
    if player_rect.bottom == sample_rect.top:
        if player_rect.colliderect(sample_rect):
            y_velocity[1] = 0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run == False
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            
            if event.key == pygame.K_RIGHT:
                x_velocity[0] = True
            if event.key == pygame.K_LEFT:
                x_velocity[1] = True
            if event.key == pygame.K_UP:
                y_velocity[0] = True
            if event.key == pygame.K_DOWN:
                y_velocity[1] = True
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_RIGHT:
                x_velocity[0] = False
            if event.key == pygame.K_LEFT:
                x_velocity[1] = False
            if event.key == pygame.K_UP:
                y_velocity[0] = False
            if event.key == pygame.K_DOWN:
                y_velocity[1] = False

    pygame.display.update()
    clock.tick(60)

pygame.quit()


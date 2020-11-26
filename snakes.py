import pygame
import random

pygame.init()

white = (255, 255, 255)
red = (255, 0, 0)
black = (0, 0, 0)

screen_width = 800
screen_height = 500
gameWindow = pygame.display.set_mode((screen_width, screen_height))

pygame.display.set_caption("Snakes")
pygame.display.update()

exit_game = False
game_over = False
snake_x = 45
snake_y = 55
snake_size = 10
fps = 30
velocity_x = 0
velocity_y = 0

clock = pygame.time.Clock()

while not exit_game:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit_game = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                velocity_x = 10
                velocity_y = 0

            if event.key == pygame.K_LEFT:
                velocity_x = -10
                velocity_y = 0

            if event.key == pygame.K_UP:
                velocity_x = 0
                velocity_y = -10

            if event.key == pygame.K_DOWN:
                velocity_x = 0
                velocity_y = 10

            if event.key == pygame.K_SPACE:
                snake_size = 20

    snake_x = snake_x + velocity_x
    snake_y = snake_y + velocity_y

    gameWindow.fill(white)
    pygame.display.update()

    gameWindow.fill(white)
    pygame.draw.rect(gameWindow, black, [snake_x, snake_y, snake_size, snake_size])
    pygame.display.update()
    clock.tick(fps)

pygame.quit()
quit()

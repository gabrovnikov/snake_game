#start settings

import pygame
import random 

pygame.init()

pygame.display.set_caption("Snake Game")
width, height = 1200, 700
display = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

#defining colors in RGB

black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 156, 76)
blue = (0, 0, 255)
background_color = (204, 204, 255)
background_color2 = (160, 160, 160)
snake_color = (255, 102, 102)

#snake parameters

square_size = 20
game_speed = 15

#food

def food_generate(): 
    food_x = round(random.randrange(0, width - square_size) / 20.0) * 20.0
    food_y = round(random.randrange(0, height - square_size) / 20.0) * 20.0
    return food_x, food_y

def food_draw(size, food_x, food_y):
    pygame.draw.rect(display, green, [food_x, food_y, size, size])

def snake_draw(size, pixels):
    for pixel in pixels:
        pygame.draw.rect(display, snake_color, [pixel[0], pixel[1], size, size])

def points_draw(points):
    font = pygame.font.SysFont("Helvetica", 30)
    text = font.render(f"Pontos: {points}", True, white)
    display.blit(text, [1, 1])

def select_speed(key):
    if key == pygame.K_DOWN:
        speed_x = 0
        speed_y = square_size
    elif key == pygame.K_UP:
        speed_x = 0
        speed_y = -square_size
    elif key == pygame.K_RIGHT:
        speed_x = square_size
        speed_y = 0
    elif key == pygame.K_LEFT:
        speed_x = -square_size
        speed_y = 0
    return speed_x, speed_y

#game loop

def game():
    end_game = False

    x = width / 2
    y = height / 2

    speed_x = 0
    speed_y = 0

    snake_length = 1
    pixels = []

    food_x , food_y = food_generate()

    while not end_game:
        display.fill(background_color2)

        for event in pygame.event.get():
            if event.type == pygame.QUIT: 
                end_game = True
            elif event.type == pygame.KEYDOWN:
                speed_x, speed_y = select_speed(event.key)    

        # adding the food into the display
        food_draw(square_size, food_x, food_y)

        # rounding the coordinates of the head of the snake
        x = round(x, 1)
        y = round(y, 1)

        # refreshing the snake position
        if x < 0 or x >= width or y < 0 or y >= height:
            end_game = True

        x += speed_x
        y += speed_y

        # drawing the snake
        pixels.append([x, y])
        if len(pixels) > snake_length:
            del pixels[0]

        # if the snake has hit itself
        for pixel in pixels[:-1]:
            if pixel == [x,y]:
                end_game = True

        snake_draw(square_size, pixels)        
        points_draw(snake_length - 1)    

        pygame.display.update()

        if round(x) == food_x and round(y) == food_y:
            snake_length += 1 
            food_x, food_y = food_generate()

        clock.tick(game_speed)

game()

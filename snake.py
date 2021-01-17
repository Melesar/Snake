import pygame
import random

screen_width = 800
screen_height = 600

food_size = 10

grid_cell_size = 20
grid_width = int(screen_width / grid_cell_size)
grid_height = int(screen_height / grid_cell_size)
grid_color = (0, 0, 0)
grid_line_width = 1

snake_head_color = (230, 15, 68)
snake_body_color = (0, 0, 0)
food_color = (0, 255, 0)
background_color = (255, 255, 255)

default_move_interval = 0.5
min_move_interval = 0.05
speed_increase_interval = 10
speed_increase_amount = 0.1

def main():
    pygame.init()
    screen = pygame.display.set_mode((screen_width, screen_height))

    snake = [(grid_width / 2, grid_height / 2)]
    snake_segment = pygame.Surface((grid_cell_size, grid_cell_size))
    food = pygame.Surface((food_size, food_size))
    food.fill(food_color)

    food_position = randomize_food_position(snake)
    move_direction = (0, -1)

    is_playing = True
    clock = pygame.time.Clock()
    deltaTime = 0.0
    move_interval = default_move_interval
    move_timer = move_interval
    while is_playing:
        screen.fill(background_color)
        draw_snake(screen, snake_segment, snake)
        draw_food(screen, food, food_position)

        pygame.display.update()

        move_timer -= deltaTime
        if move_timer <= 0:
            move_snake(snake, move_direction)
            # ============= TASK #5 =================
            # Consume food. We need to check if we have reached the food and consume it if so. 
            # As a result, the snake should get bigger. To achieve this, add an element to the end of 
            # the snake list. It will make it one segment bigger

        if move_interval > min_move_interval:
            # Difficulty growth
            pass

        if check_game_over(snake):
            snake = [(grid_width / 2, grid_height / 2)]
            move_interval = default_move_interval
            food_position = randomize_food_position(snake)
            move_direction = (0, -1)

        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                is_playing = False
            if event.type == pygame.KEYDOWN:
                key = pygame.key.name(event.key)
                # ================== TASK # 3 =====================
                # Make the snake react to the WASD input.
                # The goal here is to set move_direction variable according to the keyboard input.
                # key variable holds the name of the key that was pressed, for example 'w', 'a', 's' or 'd'.
                # So if 'w' is pressed, the move_direction should be (0, -1), if a then (-1, 0) and so on

        deltaTime = clock.tick() / 1000
    

def draw_snake(screen, segment, snake):
    is_head = True
    for p in snake:
        if is_head:
            segment.fill(snake_head_color)
            is_head = False
        else:
            segment.fill(snake_body_color)
        screen.blit(segment, (p[0] * grid_cell_size, p[1] * grid_cell_size))

def draw_food(screen, food, position):
    size_delta = 0.5 * (grid_cell_size - food_size)
    screen.blit(food, (position[0] * grid_cell_size + size_delta, position[1] * grid_cell_size + size_delta))

def draw_grid(screen):
    for y in range(grid_height):
        row = y * grid_cell_size
        pygame.draw.line(screen, grid_color, (0, row), (screen_width, row), grid_line_width)
    for x in range(grid_width):
        column = x * grid_cell_size
        pygame.draw.line(screen, grid_color, (column, 0), (column, screen_height), grid_line_width) 
            

def move_snake(snake, move_direction):
    # =============== TASK # 1 ===================
    # Make snake move in the given direction
    # move_direction variable is a tuple (x, y) which holds the number of cells that we need to move
    # along each axis. For example if move_direction is equals to (0, -1), it means that the snake
    # needs to move one cell up and 0 cells to the side
    pass

def randomize_food_position(snake):
    # ============== TASK # 4 ====================
    # Spawn the food in the random position. This function needs to return a tuple (x, y) that
    # will show the position of the food on the grid.
    # Right now it always returns the same position, but we need to make it pick a random position where 
    # there is no snake
    return (grid_width / 2, grid_height / 6)

def check_game_over(snake):
    # ============= TASK #2 ======================
    # Check if the snake collided with the screen border. If it did, return True. If didn't return False
    return False

if __name__ == "__main__":
    main()

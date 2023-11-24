import pygame
import random

# Initialize Pygame
pygame.init()

# Game Settings
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (213, 50, 80)
GREEN = (0, 255, 0)
BLUE = (50, 153, 213)
GRAY = (150, 150, 150)
DIS_WIDTH = 600
DIS_HEIGHT = 400
SNAKE_BLOCK = 20
SNAKE_SPEED = 10
FONT_STYLE = pygame.font.SysFont("Minecraft", 50)
SCORE_FONT = pygame.font.SysFont("Minecraft", 24)

# Game Display
dis = pygame.display.set_mode((DIS_WIDTH, DIS_HEIGHT))
pygame.display.set_caption("Snake Game")
clock = pygame.time.Clock()


def draw_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, GREEN, [x[0], x[1], snake_block, snake_block])


def draw_score(score):
    value = SCORE_FONT.render("Your Score: " + str(score), True, BLACK)
    dis.blit(value, [0, 0])


def draw_message(msg, color, position):
    mesg = FONT_STYLE.render(msg, True, color)
    dis.blit(mesg, position)


def check_collision(x1, y1, x2, y2, block_size):
    return x1 >= x2 and x1 < x2 + block_size and y1 >= y2 and y1 < y2 + block_size


def game_loop():
    game_over = False
    game_close = False

    x1, y1 = DIS_WIDTH / 2, DIS_HEIGHT / 2
    x1_change, y1_change = 0, 0

    snake_list = []
    length_of_snake = 1

    foodx = (
        round(random.randrange(10, (DIS_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK))
        * SNAKE_BLOCK
    )
    foody = (
        round(random.randrange(10, (DIS_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK))
        * SNAKE_BLOCK
    )

    while not game_over:
        while game_close:
            dis.fill(BLACK)
            draw_message("GAME OVER!", WHITE, (140, 75))
            draw_message("Press 'Q' to Quit", WHITE, (110, 150))
            draw_message("or", WHITE, (270, 200))
            draw_message("'C' to Play Again", WHITE, (110, 250))
            draw_score(length_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        game_loop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = SNAKE_BLOCK
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -SNAKE_BLOCK
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = SNAKE_BLOCK
                    x1_change = 0

        x1 += x1_change
        y1 += y1_change

        # Check for collision with the barrier
        if (
            x1 >= (DIS_WIDTH - SNAKE_BLOCK)
            or x1 < SNAKE_BLOCK
            or y1 >= (DIS_HEIGHT - SNAKE_BLOCK)
            or y1 < SNAKE_BLOCK
        ):
            game_close = True

        # Do not proceed with rendering if the game is about to close
        if game_close:
            continue

        dis.fill(BLACK)
        pygame.draw.rect(dis, GRAY, [0, 0, DIS_WIDTH, DIS_HEIGHT], SNAKE_BLOCK)
        pygame.draw.rect(dis, RED, [foodx, foody, SNAKE_BLOCK, SNAKE_BLOCK])
        snake_head = [x1, y1]
        snake_list.append(snake_head)

        if len(snake_list) > length_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        draw_snake(SNAKE_BLOCK, snake_list)
        draw_score(length_of_snake - 1)

        pygame.display.update()

        if check_collision(x1, y1, foodx, foody, SNAKE_BLOCK):
            foodx = (
                round(random.randrange(10, (DIS_WIDTH - SNAKE_BLOCK) / SNAKE_BLOCK))
                * SNAKE_BLOCK
            )
            foody = (
                round(random.randrange(10, (DIS_HEIGHT - SNAKE_BLOCK) / SNAKE_BLOCK))
                * SNAKE_BLOCK
            )
            length_of_snake += 1

        clock.tick(SNAKE_SPEED)

    pygame.quit()
    quit()


game_loop()

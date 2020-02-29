import pygame
import random
pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
green = (50, 153, 213)

dis_width = 800
dis_height = 600
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('SUPER Snake Game')

clock = pygame.time.Clock()
snake_block = 10
snake_speed = 30

font_style = pygame.font.SysFont("comicsansms", 30)
score_font = pygame.font.SysFont("comicsansms", 35)


def your_score(score):
    value = score_font.render("Your score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, red, [x[0], x[1], snake_block, snake_block])


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width/6, dis_height/3])


def gameloop():

    pygame.mixer_music.load("COPSTEP - Motherfucking Snakes.mp3")
    pygame.mixer_music.play(-1)

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_list = []
    lenght_of_snake = 1

    foodx = round(random.randrange(10, dis_width - snake_block) / 20.0) * 20.0
    foody = round(random.randrange(10, dis_height - snake_block) / 20.0) * 20.0

    direction = None

    while not game_over:
        while game_close:
            dis.fill(blue)
            message("You lose! Press Q=Quit or C=Play Again", red)
            your_score(lenght_of_snake - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameloop()
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if (event.key == pygame.K_LEFT or event.key == pygame.K_a) and direction != "right":
                    x1_change = -snake_block
                    y1_change = 0
                    direction = "left"
                elif (event.key == pygame.K_RIGHT or event.key == pygame.K_d) and direction != "left":
                    x1_change = snake_block
                    y1_change = 0
                    direction = "right"
                elif (event.key == pygame.K_UP or event.key == pygame.K_w) and direction != "down":
                    x1_change = 0
                    y1_change = -snake_block
                    direction = "up"
                elif (event.key == pygame.K_DOWN or event.key == pygame.K_s) and direction != "up":
                    x1_change = 0
                    y1_change = snake_block
                    direction = "down"

        # warunek zakończenia gry przy uderzeniu w ścianę
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(black)
        pygame.draw.rect(dis, white, [foodx, foody, snake_block, snake_block])
        snake_head = []
        snake_head.append(x1)
        snake_head.append(y1)
        snake_list.append(snake_head)
        if len(snake_list) > lenght_of_snake:
            del snake_list[0]

        for x in snake_list[:-1]:
            if x == snake_head:
                game_close = True

        our_snake(snake_block, snake_list)
        your_score(lenght_of_snake - 1)

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(10, dis_width - snake_block) / 20.0) * 20.0
            foody = round(random.randrange(10, dis_height - snake_block) / 20.0) * 20.0
            lenght_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()


if __name__ == '__main__':
    gameloop()
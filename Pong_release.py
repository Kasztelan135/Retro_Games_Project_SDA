import pygame
import random


pygame.init()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)

# Inicjalizacja okienka do gry
size = (800, 600)
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Pong Game")


# Rysuje rakietkę oraz określa jej granice pomiędzy
# krawędziami ekranu
def drawrect(screen, x, y):
    if x <= 0:
        x = 0
    if x >= 699:
        x = 699
    pygame.draw.rect(screen, RED, [x, y, 100, 20])


def random_color():
    return random.randint(0, 255), random.randint(0, 255), random.randint(0, 255)


def distorted(value, should_distort):
    return value if not should_distort else value + random.randint(-1, 1) * random.randint(1, 2)


def distorted_array(array, should_distort):
    return [distorted(a, should_distort) for a in array]


# Logika gry
def gameloop():
    pygame.mixer_music.load("PONG_music.mp3")
    pygame.mixer_music.play(-1)

    # Początkowe współrzędne rakietki do odbijania piłeczki
    rect_x = 400
    rect_y = 580

    # Prędkość początkowa rakietki
    rect_change_x = 0
    rect_change_y = 0

    # Pozycja początkowa piłeczki
    ball_x = 50
    ball_y = 50

    # Prędkość piłeczki
    ball_change_x = 5
    ball_change_y = 5

    score = 0
    max_score = 0

    done = False
    clock = pygame.time.Clock()
    while not done:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    rect_change_x = -6
                elif event.key == pygame.K_RIGHT:
                    rect_change_x = 6
            elif event.type == pygame.KEYUP:
                if event.key == pygame.K_LEFT or event.key == pygame.K_RIGHT:
                    rect_change_x = 0
                elif event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                    rect_change_y = 0
        screen.fill(BLACK)
        rect_x += rect_change_x
        rect_y += rect_change_y

        ball_x += ball_change_x
        ball_y += ball_change_y

        # Obsługa ruchu piłeczki
        if ball_x < 0:
            ball_x = 0
            ball_change_x = ball_change_x * -1
        elif ball_x > 785:
            ball_x = 785
            ball_change_x = ball_change_x * -1
        elif ball_y < 0:
            ball_y = 0
            ball_change_y = ball_change_y * -1
        elif ball_x > rect_x and ball_x <rect_x + 100 and ball_y == 565:
            ball_change_y = ball_change_y * -1
            score = score + 1
            if score > max_score:
                max_score = score
        elif ball_y > 600:
            ball_change_y = ball_change_y * -1
            if rect_x < ball_x < rect_x + 100:
                score = score + 3
                if score > max_score:
                    max_score = score
            else:
                score = 0
        pygame.draw.rect(screen, WHITE, [ball_x, ball_y, 15, 15])

        drawrect(screen, rect_x, rect_y)
        at_max = score == max_score and score > 0
        # Tablica wyników
        font = pygame.font.SysFont('Calibri', 20, False, False)
        score_text = font.render("Wynik:", True, WHITE)
        max_text = font.render("Najlepsiejszy:", True, WHITE)
        score_value_text = font.render(str(score), True, random_color() if at_max else WHITE)
        max_value_text = font.render(str(max_score), True, random_color() if at_max else WHITE)
        screen.blit(score_text, [600, 100])
        screen.blit(max_text, [600, 120])
        screen.blit(score_value_text, distorted_array([700, 100], at_max))
        screen.blit(max_value_text, distorted_array([730, 120], at_max))

        pygame.display.flip()
        clock.tick(60)

    pygame.quit()

if __name__ == "__main__":
    gameloop()
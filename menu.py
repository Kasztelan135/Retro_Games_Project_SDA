import pygame
import pygame_gui
from Pizza_Panic import main
import Pong_release as pong
from Snake_Game import gameloop
from Astrocrash3 import main1

pygame.init()

pygame.mixer_music.load("MENU_music.mp3")
pygame.mixer_music.play(-1)

pygame.display.set_caption('Quick Start')
window_surface = pygame.display.set_mode((800, 600))

background = pygame.Surface((800, 600))
background.fill(pygame.Color('#000000'))

# white = (255, 255, 255)
# green = (0, 255, 0)
# blue = (0, 0, 128)
# font = pygame.font.Font('freesansbold.ttf', 32)
# text = font.render('Cudowny projekt Rafała i Dawida', True, green, blue)
# textRect = text.get_rect()
bacgkroundImage = pygame.image.load('tlo.jpg')
manager = pygame_gui.UIManager((800, 600))
pygame_gui.elements.UIImage(image_surface=bacgkroundImage, manager=manager, relative_rect=pygame.Rect((0, 0), (800, 600)))
title_label = pygame_gui.elements.UILabel(text='RETRO GAMES BY RAFAŁ AND DAWID', relative_rect=pygame.Rect((275, 100), (250, 50)), manager=manager)

title_label.bg_colour.a = 0
title_label.text_colour = (255, 0, 0)
title_label.text_font = ('freesansbold.ttf', 32)
title_label.rebuild()


pizza_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((275, 225), (250, 50)),
                                            text='MAMMA MIA, ODPALAMY',
                                            manager=manager)

astro_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((275, 275), (250, 50)),
                                            text='SPAAAAAAAAAACE',
                                            manager=manager)


snake_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((275, 325), (250, 50)),
                                            text='SNEK IZ HUNGRY',
                                            manager=manager)

pong_button = pygame_gui.elements.UIButton(relative_rect=pygame.Rect((275, 375), (250, 50)),
                                            text='PONG ME!',
                                            manager=manager)


clock = pygame.time.Clock()
is_running = True

while is_running:
    time_delta = clock.tick(60) / 1000.0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            is_running = False

        if event.type == pygame.USEREVENT:
            if event.user_type == 'ui_button_pressed':
                if event.ui_element == pizza_button:
                    main()

        if event.type == pygame.USEREVENT:
            if event.user_type == 'ui_button_pressed':
                if event.ui_element == astro_button:
                   main1()

        if event.type == pygame.USEREVENT:
            if event.user_type == 'ui_button_pressed':
                if event.ui_element == snake_button:
                    gameloop()

        if event.type == pygame.USEREVENT:
            if event.user_type == 'ui_button_pressed':
                if event.ui_element == pong_button:
                    pong.gameloop()

        manager.process_events(event)

    manager.update(time_delta)

    window_surface.blit(background, (0, 0))
    manager.draw_ui(window_surface)

    pygame.display.update()

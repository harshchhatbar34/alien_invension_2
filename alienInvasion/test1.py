import sys

import pygame

def run_game():
    #initilaisation the game and creat the object screen
    pygame.init()
    screen = pygame.display.set_mode((1400,900))
    pygame.display.set_caption('my world')
    color = (000,000,255)
    #screen.fill(color)
    # pygame.display.flip

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
               sys.exit()
        screen.fill(color)
        pygame.display.flip()

run_game()

    #start main loop of the game
    #while true:


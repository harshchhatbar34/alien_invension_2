import sys

import pygame

from pygame.sprite import Group

from settings import Settings

from game_states import  GameStats

from scoreboard import Scoreboard

from button import Button

from ship import Ship

import game_function as gf

def run_game():
    # Initialize game and create a screen object.
    pygame.init()
    ai_settings = Settings()
    screen = pygame.display.set_mode(
        (ai_settings.screen_width, ai_settings.screen_height))
    pygame.display.set_caption("Alien Invasion")
    # Make the Play button.
    play_button = Button(ai_settings, screen, "Play")

    # Create an instance to store game statistics and creat a scoreboard.
    stats = GameStats(ai_settings)
    sb = Scoreboard(ai_settings,screen,stats)

    # make a ship.
    ship =Ship(ai_settings, screen)
    #make a group to store  bullets in
    bullets = Group()
    # Make a alien.
    aliens = Group()
    ships = Group()
    gf.create_fleet(ai_settings, screen, ship, aliens)
    gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)


    # Start the main loop for the game.
    while True:
        gf.check_events(ai_settings, screen, stats, sb, play_button, ship, aliens, bullets)

        if stats.game_active:
            ship.update()
            #pdb.set_trace()
            gf.update_bullets(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_aliens(ai_settings, screen, stats, sb, ship, aliens, bullets)
            gf.update_screen(ai_settings, screen, stats, sb, ship, aliens, bullets, play_button)

run_game()

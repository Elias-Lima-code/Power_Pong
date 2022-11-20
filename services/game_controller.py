import pygame
from time import sleep
import sys
from pygame.locals import *
from utility.constants import colors
import datetime
from random import randint
from utility.math import between
from content.models.game_object import GameObject


playing = False


def handle_events(game):
    """Iterates through each event and call it's appropriate function.

    Args:
        game (Game): The currently running game.
    """
    for event in pygame.event.get():

        match event.type:
            case pygame.QUIT:
                quit_app()

            case pygame.KEYDOWN:
                handle_keydown(event.key, game)


            case pygame.KEYUP:
                handle_keyup(event.key, game)

def handle_keydown(key, game):
    """Decides what to do with the key pressed by the user.

        Args:
            key (int): The pygame keycode of the key.
            game (Game): The currently running game.
    """
    match key:
        case pygame.K_r:
            restart(game)

    if key not in game.pressed_keys:
        game.pressed_keys.append(key)



def handle_keyup(key, game):
    """Decides what to do with the key released by the user.

    Args:
        key (int): The pygame keycode of the key.
        game (Game): The currently running game.
    """
    if key in game.pressed_keys:
        game.pressed_keys.remove(key)
    
def restart(game):
    """Restarts the game from the beginning.
    """
    game.start()
    game.drawer.clear()
    
def quit_app():
    """Stops the game and closes application.
    """
    pygame.display.quit()
    pygame.quit()
    sys.exit()

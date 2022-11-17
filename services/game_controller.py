import pygame
import sys
from pygame.locals import *
from shapely.geometry import Polygon
import datetime
from random import randint
from utility.math import clamp, between

playing = False


def handle_events(game):
    for event in pygame.event.get():

        match event.type:
            case pygame.QUIT:
                quit_app()

            case pygame.KEYDOWN:
                handle_keydown(event.key, game)


            case pygame.KEYUP:
                handle_keyup(event.key, game)


def quit_app():
    """Stops the game and closes application.
    """
    pygame.display.quit()
    pygame.quit()
    sys.exit()

def restart(game):
    game.start()
    game.drawer.clear()

def handle_keydown(key, game):

    match key:
        case pygame.K_r:
            restart(game)

    if key not in game.pressed_keys:
        game.pressed_keys.append(key)



def handle_keyup(key, game):

    if key in game.pressed_keys:
        game.pressed_keys.remove(key)


def read_input(game):

    def contains_key(key):
        return key in game.pressed_keys

    #def in_bounds(player):
     #   return player.pos.y >= 0 #and player.pos.y + player.size[1] #<= game.drawer.height_arena 

    def can_move(key, player):
        return contains_key(key) #wand in_bounds(player) 

    if can_move(K_w, game.p1):
        game.p1.pos.y = clamp(game.p1.pos.y-game.p1.speed,
                              0, game.drawer.height_arena - game.p1.size[1])

    if can_move(K_s, game.p1):
        game.p1.pos.y = clamp(game.p1.pos.y+game.p1.speed,
                              0, game.drawer.height_arena - game.p1.size[1])

    if can_move(K_UP, game.p2):
        game.p2.pos.y = clamp(game.p2.pos.y-game.p2.speed,
                              0, game.drawer.height_arena - game.p2.size[1])

    if can_move(K_DOWN, game.p2):
        game.p2.pos.y = clamp(game.p2.pos.y+game.p2.speed,
                              0, game.drawer.height_arena - game.p2.size[1])


def ball_movemt(game):

    game.ball.pos.x += game.ball.xspeed * game.ball.direction.x
    game.ball.pos.y += game.ball.yspeed * game.ball.direction.y

    for o in game.ball_targets:
        if collides(game.ball.get_polygon(), o.get_polygon()):
            if o.reflection_dir[0] == 1 :
                game.ball.direction.x *= -1 
            if o.reflection_dir[1] == 1 :
                game.ball.direction.y *= -1 


def collides(polygon1, polygon2):

    return polygon1.intersects(polygon2)
    
    

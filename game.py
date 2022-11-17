import pygame, datetime
from pygame.locals import *
from random import randint

from services.draw_screen import Drawer
from services import game_controller
from utility.constants import colors
from content.models.paddle import Paddle
from content.models.ball import Ball
from content.models.coord import Coord 
from content.models.game_object import GameObject 



class Game():
    def __init__(self):
        
        self.clock = pygame.time.Clock()
        self.drawer = None
        self.screen = None
        self.pressed_keys = []
        self.monitor_size = (0, 0)
        self.p1 = None
        self.p2 = None
        self.ball = Ball()
        self.ball_targets = []
        

    def start(self):
        print("play")
        pygame.init()
        
        if self.monitor_size == (0,0):
            self.monitor_size = (pygame.display.Info().current_w - 50, pygame.display.Info().current_h -50 )


        game_controller.playing = True
        self.screen = pygame.display.set_mode(self.monitor_size)
        
        

        self.drawer = Drawer(self)

        _player_size = (20, self.drawer.height_arena * 0.18) 
        self.p1 = Paddle(
                        pos=Coord((40,(self.drawer.height_arena - _player_size[1]) / 2)), 
                        size = _player_size,
                        speed = 8,
                        color = colors.WHITE,
                        reflection_dir = (1,0)
                        )

        self.p2 = Paddle(
                        pos=Coord((self.drawer.width_arena - 40 - _player_size[0],(self.drawer.height_arena - _player_size[1]) / 2)),
                        size = _player_size,
                        speed = 8,
                        color = colors.WHITE,
                        reflection_dir = (1,0)
                        )

        self.ball = Ball(
                        pos=Coord((self.drawer.width_arena / 2 - 8,self.drawer.height_arena / 2 - 8)),
                        size = (16,16),
                        xspeed = 5,
                        yspeed = 5,
                        color = colors.RED,
                        direction = Coord((-1 if randint(0,1) == 0 else 1,-1 if randint(0,1) == 0 else 1))
                        )
                        
        _wall_top = GameObject(pos= Coord((self.drawer.top_wall)), color=colors.RED, size = self.drawer.top_wall_size,reflection_dir= (0,1))
        _wall_bottom = GameObject(pos= Coord((self.drawer.bottom_wall)), color=colors.RED, size = self.drawer.bottom_wall_size,reflection_dir= (0,1))
        self.ball_targets = [self.p1, self.p2,_wall_top,_wall_bottom]


        self.game_loop()
        
        game_controller.resize_window(self)
        
           
                   

    def game_loop(self):

        while game_controller.playing:
            self.clock.tick(60)


            game_controller.handle_events(self)
            game_controller.read_input(self)
            game_controller.ball_movemt(self)

            self.screen.fill(colors.BLACK)

            self.drawer.draw_arena()
            self.drawer.draw_objects()
            

            
            

          

            pygame.display.update()



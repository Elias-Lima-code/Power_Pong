import pygame, time
from pygame.locals import *
from random import randint

from services.drawer import Drawer
from services import game_controller
from utility.constants import colors
from utility.constants.enums import *
from content.models.paddle import Paddle
from content.models.ball import Ball
from content.models.game_object import GameObject 
from content.models.player import Player
from utility.math import infix_sum_tuple as t, infix_clamp as clamp

class Game():
    def __init__(self):
        
        #pygame clock to control FPS
        self.clock = pygame.time.Clock()
        #class to display the game on screen
        self.drawer = None
        #main surface to hold all drawings
        self.screen = None
        #the list of currently pressed keys of keyboard
        self.pressed_keys = []
        #the size of user monitor
        self.monitor_size = (0, 0)
        #player one paddle
        self.p1 = None
        #player two paddle
        self.p2 = None
        #the game ball
        self.ball = None
        #the last time the loop executed
        self.last_time = None
        #the game time delta
        self.dt = None
        

    def start(self):
        """Start the game and create the objects
        """
        pygame.init()
        self.last_time = time.time()
        if self.monitor_size == (0,0):
            self.monitor_size = (pygame.display.Info().current_w - 50, pygame.display.Info().current_h -50 )


        self.screen = pygame.display.set_mode(self.monitor_size)
        
        self.drawer = Drawer()
        self.drawer.setup(self.screen)

        _player_size = (20, self.drawer.height_arena * 0.18) 
        
        p1_paddle = Paddle(self.drawer.group,
                        pos=(40,(self.drawer.height_arena - _player_size[1]) / 2), 
                        size = _player_size,
                        speed = 30,
                        color = colors.WHITE,
                        name="Player 1 Paddle"
                        )

        p2_paddle = Paddle(self.drawer.group,
                        pos=(self.drawer.width_arena - 40 - _player_size[0],(self.drawer.height_arena - _player_size[1]) / 2),
                        size = _player_size,
                        speed = 30,
                        color = colors.WHITE,
                        name="Player 2 Paddle"
                        )
        
        _arena_size = (self.drawer.width_arena, self.drawer.height_arena)
        _paddle_size = (10, _arena_size[1] * 0.18)
        
        self.p1 = Player(paddle = p1_paddle, 
                         top_beam = GameObject(self.drawer.group, pos=(0, 0), size=_paddle_size, color=colors.WHITE, name="P1_Top_Beam"),
                         bottom_beam = GameObject(self.drawer.group, pos=(0, _arena_size[1]-_paddle_size[1]),size = _paddle_size, color = colors.WHITE, name = "P1_Bottom_Beam")
                         )
        
        self.p2 = Player(paddle = p2_paddle, 
                        top_beam = GameObject(self.drawer.group, pos=(_arena_size[0] - _paddle_size[0], 0), size=_paddle_size, color=colors.WHITE, name="P2_Top_Beam"),
                        bottom_beam = GameObject(self.drawer.group, pos=(_arena_size[0] - _paddle_size[0], _arena_size[1] - _paddle_size[1]), size = _paddle_size, color = colors.WHITE, name = "P2_Bottom_Beam")
                        )

        self.ball = Ball(self.drawer.group,
                        pos=(self.drawer.width_arena / 2 - 8,self.drawer.height_arena / 2 - 8),
                        size = (16,16),
                        xspeed = 32,
                        yspeed = 32,
                        color = colors.YELLOW,
                        direction = (-1 if randint(0,1) == 0 else 1,-1 if randint(0,1) == 0 else 1),
                        name="Ball"
                        )
        
        game_controller.playing = True
        self.game_loop()
        
    
    
    
    def ball_movement(self):
        """Makes the movement of the ball.

        Args:
            game (Game): The currently running game.
        """
        self.ball.last_rect = self.ball.rect.copy()

        self.ball.pos = self.ball.pos |t| (self.ball.xspeed * 10 * self.ball.direction[0] * self.dt, 0)
        self.ball.rect[0] = round(self.ball.pos[0])
        self.handle_ball_collision(Orientation.HORIZONTAL)
        self.ball.pos = self.ball.pos |t| (0, self.ball.yspeed * 10 * self.ball.direction[1] * self.dt)
        self.ball.rect[1] = round(self.ball.pos[1])
        self.handle_ball_collision(Orientation.VERTICAL)

    def handle_ball_collision(self, direction):
        """Handles the collision of the ball to obstacle game objects.

        Args:
            game (Game): The currently running game.
            direction (str): The direction to detect collision.
        """
        collision_objs = pygame.sprite.spritecollide(self.ball, self.drawer.group, False)
        
        if not collision_objs:
            return
        
        for o in collision_objs:
            match direction:
                case Orientation.HORIZONTAL:
                    # collision on the right
                    if self.ball.rect.right >= o.rect.left and self.ball.last_rect.right <= o.last_rect.left:
                        self.ball.rect.right = o.rect.left
                        self.ball.pos = (self.ball.rect[0], self.ball.rect[1])
                        self.ball.direction = (-1, self.ball.direction[1])
                        
                    # collision on the left
                    elif self.ball.rect.left <= o.rect.right and self.ball.last_rect.left >= o.last_rect.right:
                        self.ball.rect.left = o.rect.right
                        self.ball.pos = (self.ball.rect[0], self.ball.rect[1])
                        self.ball.direction = (1, self.ball.direction[1])
            
                case Orientation.VERTICAL:
                    # collision on the bottom
                    if self.ball.rect.bottom >= o.rect.top and self.ball.last_rect.bottom <= o.last_rect.top:
                        self.ball.rect.bottom = o.rect.top
                        self.ball.pos = (self.ball.rect[0], self.ball.rect[1])
                        self.ball.direction = (self.ball.direction[0], -1)
                        
                    # collision on the top
                    elif self.ball.rect.top >= o.rect.top and self.ball.last_rect.top >= o.last_rect.bottom:
                        self.ball.rect.top = o.rect.bottom
                        self.ball.pos = (self.ball.rect[0], self.ball.rect[1])
                        self.ball.direction = (self.ball.direction[0], 1)
        
        
    
    def read_input(self):
        """Checks the currently pressed keys and handle what to do.

        Args:
            game (Game): The currently running game.
        """
        _offset = self.drawer.wall_top.size[1]
        
        def contains_key(key):
            return key in self.pressed_keys

        if contains_key(pygame.K_w):
            self.move_player(self.p1.paddle, Direction.UP, _offset)
            
        if contains_key(pygame.K_s):
            self.move_player(self.p1.paddle, Direction.DOWN, _offset)

        if contains_key(pygame.K_UP):
            self.move_player(self.p2.paddle, Direction.UP, _offset)

        if contains_key(pygame.K_DOWN):
            self.move_player(self.p2.paddle, Direction.DOWN, _offset)
    
    def move_player(self, player, direction: Direction, offset):
        """Moves the chosen player paddle to the specified direction.

        Args:
            player (Paddle): The player paddle to move.
            direction (Direction): The direction to move the paddle.
            offset (int): The distance in px from the arena borders to stop the paddle (frame width).
        """
        player.last_rect = player.rect.copy()
        match direction:
            case Direction.UP:
                player.pos = (player.pos[0], player.pos[1] - (player.speed *10* self.dt) |clamp| [offset, self.drawer.height_arena - offset])
            case Direction.DOWN:
                player.pos = (player.pos[0], player.pos[1] + (player.speed * 10 * self.dt) |clamp| [offset, self.drawer.height_arena - offset - player.size[1]])
        player.rect[1] = round(player.pos[1])
        
         
    def game_loop(self):
        """The game's main loop.
        """
        while game_controller.playing:
            self.clock.tick(60)
            self.dt = time.time() - self.last_time
            self.last_time = time.time()
            


            game_controller.handle_events(self)
            self.read_input()
            self.ball_movement()

            self.screen.fill(colors.BLACK)

            self.drawer.draw_arena(self.screen, self.p1, self.p2)
            self.drawer.draw_objects(self.screen, [self.p1.paddle, self.p2.paddle, self.ball])
            
            pygame.display.update()



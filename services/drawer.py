import pygame
from utility.constants import colors
from content.models.game_object import GameObject
from content.models.player import Player
from content.models.ball import Ball

class Drawer:

    def __init__(self):
        #the width of the game arena
        self.width_arena = 0
        #the height of the game arena
        self.height_arena = 0
        #the width and height of the arena frame
        self.frame_size= (0,0)
        #top frame
        self.wall_top = None
        #bottom frame
        self.wall_bottom = None
        #Group of sprites that the ball can collide with
        self.group_ball_obstacles = None
        #Group of sprites that the ball will score when colliding
        self.group_score_zones = None

    def setup(self, screen: pygame.surface):
        """sets the initial values.
           Args:
            screen (pygame.surface): The screen to draw on.
        """
        self.width_arena = int(screen.get_size()[0])
        self.height_arena = int(screen.get_size()[1])
        self.frame_size= (self.width_arena,10)
        self.group_ball_obstacles = pygame.sprite.Group()
        self.group_score_zones = pygame.sprite.Group()
    
        self.wall_top = GameObject(self.group_ball_obstacles, pos= (0,0), color=colors.LIGHT_GRAY, size = self.frame_size, name="TOP")
        self.wall_bottom = GameObject(self.group_ball_obstacles, pos= (0,self.height_arena - self.frame_size[1]), color=colors.LIGHT_GRAY, size = self.frame_size, name="BOTTOM")
    
    def draw_arena(self, screen: pygame.surface, p1: Player, p2: Player):
        """Draws arena objects.
           Args:
               screen (pygame.surface): The screen to draw on.
               p1 (Player): The player one.
               p2 (Player): The player two.
        """
    
        #player 1 goalposts
        pygame.draw.rect(screen, p1.top_beam.color, p1.top_beam.rect)
        pygame.draw.rect(screen, p1.bottom_beam.color, p1.bottom_beam.rect)
        
        #player 2 goalposts
        pygame.draw.rect(screen, p2.top_beam.color, p2.top_beam.rect)
        pygame.draw.rect(screen, p2.bottom_beam.color, p2.bottom_beam.rect)

        #top and bottom frames
        pygame.draw.rect(screen, self.wall_top.color, self.wall_top.rect)
        pygame.draw.rect(screen, self.wall_bottom.color, self.wall_bottom.rect)
   
    def draw_objects(self, screen: pygame.surface, objects: list[GameObject]):
        """Draws game objects.
           Args:
               screen (pygame.surface): The screen to draw on.
               objects (list[GameObject]): The list of objects to draw.
        """
        for obj in objects:
            obj.draw(screen)
            
            
            
            
            
    def draw_text(self, text, pos, size = 30, color = colors.WHITE, font = 'Arial'):
        """Custom function to write text on the screen

            Args:
                text (any): The text to be drawn.
                pos (Tuple[int,int]): The top left position the text will be drawn.
                color (Tuple[int,int,int,int], optional): The RGB(A) color values for the text. Defaults to colors.WHITE.
                size (int, optional): The size of font . Defaults to 30.
                font (str, optional): The name of the font to render the text. Defaults to 'Arial'.
        """
        text_surface = self.get_text_surface(text, color, size, font)
        self.game.screen.blit(text_surface, pos)
    
    def get_text_surface(self, text, size, color, font):
        """Creates the text with specified values and returns it's surface.

        Args:
            text (any): The text to be drawn.
            size (int, optional): The size of font . Defaults to 30.
            color (Tuple[int,int,int,int], optional): The RGB(A) color values for the text. Defaults to colors.WHITE.
            font (str, optional): The name of the font to render the text. Defaults to 'Arial'.

        Returns:
            _type_: _description_
        """
        text = str(text)
        
        r, g, b, *a = color
        color = (r,g,b)
        _font = None
        
        if type(font) == str:
            _font = pygame.font.SysFont(font, size)
        else:
            _font = font
                
        text_surface = _font.render(text, False, color)
        if len(a) > 0:
            text_surface.set_alpha(a[0])
        return text_surface
        
    def draw_ui(self, screen: pygame.surface, p1: Player,p2: Player):
        """draw user's interface

        Args:
            screen (pygame.surface): The screen to draw on.
            p1 (Player): The name and score of the player 1 to be drawn
            p2 (Player): The name and score of the player 2 to be drawn
        """
        _x_margin = 50
        _y_margin = 30
        p1_name = self.get_text_surface("Player 1", 30, colors.GREEN, font='Arial')
        p2_name = self.get_text_surface("Player 2", 30, colors.GREEN, font='Arial')
        
        score_board = self.get_text_surface(f"{p1.score} x {p2.score}", 30, colors.GREEN, font='Arial')
        
        screen.blit(p1_name, (p1.top_beam.size[0] + _x_margin, _y_margin))
        screen.blit(p2_name, (self.width_arena - p2.top_beam.size[0] - p2_name.get_size()[0] - _x_margin, _y_margin))
        screen.blit(score_board, (self.width_arena/2 - (score_board.get_size()[0]/2), _y_margin))
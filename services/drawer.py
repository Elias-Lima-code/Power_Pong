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
        #Sprites groups
        self.group = None

    def setup(self, screen: pygame.surface):
        """sets the initial values.
           Args:
            screen (pygame.surface): The screen to draw on.
        """
        self.width_arena = int(screen.get_size()[0])
        self.height_arena = int(screen.get_size()[1])
        self.frame_size= (self.width_arena,10)
        self.group = pygame.sprite.Group()
    
        self.wall_top = GameObject(self.group, pos= (0,0), color=colors.LIGHT_GRAY, size = self.frame_size, name="TOP")
        self.wall_bottom = GameObject(self.group, pos= (0,self.height_arena - self.frame_size[1]), color=colors.LIGHT_GRAY, size = self.frame_size, name="BOTTOM")
    
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
        

    def draw_text(self,screen: pygame.surface, text, pos, color = colors.WHITE, size = 30, font = 'Arial'):
        """Custom function to write text on the screen

        Args:
            text (any): The text to be drawn.
            pos (Tuple[int,int]): The top left position the text will be drawn.
            color (Tuple[int,int,int,int], optional): The RGB(A) color values for the text. Defaults to colors.WHITE.
            size (int, optional): The size of font . Defaults to 30.
            font (str, optional): The name of the font to render the text. Defaults to 'Arial'.
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
        screen.blit(text_surface, pos)
        
        
    
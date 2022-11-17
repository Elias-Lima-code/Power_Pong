import pygame
from shapely.geometry import Polygon
from utility.constants import colors
from content.models.coord import Coord 

class GameObject:
    def __init__(self, **kwargs):
        self.pos = kwargs.pop("pos", Coord((0,0)))
        self.size = kwargs.pop("size", (0,0))
        self.color = kwargs.pop("color", colors.WHITE)
        self.reflection_dir = kwargs.pop("reflection_dir", (0,1,2,3))


    def draw(self,screen):
        pygame.draw.rect(screen, self.color ,((self.pos.x,self.pos.y),self.size))

    def get_polygon(self):
        return Polygon([(self.pos.x,self.pos.y), (self.pos.x + self.size[0],self.pos.y),(self.pos.x + self.size[0],self.pos.y + self.size[1]),(self.pos.x,self.pos.y + self.size[1])])
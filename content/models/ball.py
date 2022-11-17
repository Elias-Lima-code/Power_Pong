import pygame
from utility.constants import colors
from content.models.game_object import GameObject
from content.models.coord import Coord 

class Ball(GameObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.xspeed = kwargs.pop("xspeed", 0)
        self.yspeed = kwargs.pop("yspeed", 0)
        self.direction = kwargs.pop("direction",Coord((1,1)))
    
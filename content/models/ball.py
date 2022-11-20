import pygame
from utility.constants import colors
from content.models.game_object import GameObject

class Ball(GameObject):
    def __init__(self, group, **kwargs):
        super().__init__(group, **kwargs)
        #the horizontal speed of the ball
        self.xspeed = kwargs.pop("xspeed", 0)
        #the vertical speed of the ball
        self.yspeed = kwargs.pop("yspeed", 0)
        #the horizontal and vertical direction that the ball is moving to
        self.direction = kwargs.pop("direction",(1,1))
    
from content.models.game_object import GameObject
from content.models.paddle import Paddle


class Player():
    def __init__(self, **kwargs):
        #The paddle of this player
        self.paddle: Paddle = kwargs.pop("paddle", None)
        #The rect of the top goalpost
        self.top_beam: GameObject = kwargs.pop("top_beam", None)
        #The rect of the bottom goalpost
        self.bottom_beam: GameObject = kwargs.pop("bottom_beam", None)
   

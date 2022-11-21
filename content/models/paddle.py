from content.models.game_object import GameObject


class Paddle(GameObject):
    def __init__(self, group, **kwargs):
        super().__init__(group, **kwargs)
        #the vertical movement speed of the paddle
        self.speed = kwargs.pop("speed", 0)
        #The default force that the player will rebound the ball when moving, changing it's angle
        self.rebound_force = kwargs.pop("rebound_force", 0.6)


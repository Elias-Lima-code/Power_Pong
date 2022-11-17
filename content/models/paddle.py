from content.models.game_object import GameObject


class Paddle(GameObject):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        self.speed = kwargs.pop("speed", 0)


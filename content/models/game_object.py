import pygame
from utility.constants import colors


class GameObject(pygame.sprite.Sprite):
    def __init__(self, group, **kwargs):
        super().__init__(group)
        #the topleft position of this object
        self.pos = kwargs.pop("pos", (0,0))
        #the rect size of this object
        self.size = kwargs.pop("size", (0,0))
        #the color of this object
        self.color = kwargs.pop("color", colors.WHITE)
        #the name of this object (manly for debugging)
        self.name = kwargs.pop("name", "")
        #the surface of this object
        self.image = pygame.Surface(self.size)
        #the rect of this object
        self.rect = self.image.get_rect(topleft = self.pos)
        #the rect of this object in the last frame
        self.last_rect = self.rect.copy() 
        #if this object should be rendered
        self.is_alive = kwargs.pop("is_alive", True)       

    def draw(self,screen):
        """Draws this object.
           Args:
               screen (pygame.surface): The screen to draw on.
        """
        if not self.is_alive:
            return
        pygame.draw.rect(screen, self.color ,(self.pos, self.size))


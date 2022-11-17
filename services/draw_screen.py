import pygame
from utility.constants import colors


class Drawer:

    def __init__(self, game):
        self.game = game
        self.width_arena = 0
        self.height_arena = 0
        self.size_arena = 0
        self.goalpost_size = 0
        self.goalpost_offset = 0
        self.beam_width = 0
        self.top_wall = 0
        self.top_wall_size = 0
        self.bottom_wall = 0
        self.bottom_wall_size = 0
        self.setup()

    def setup(self):
        self.width_arena = int(self.game.screen.get_size()[0])
        self.height_arena = int(self.game.screen.get_size()[1])
        self.size_arena = (self.width_arena, self.height_arena)
        self.goalpost_size = self.height_arena * 0.65
        self.goalpost_offset = 0
        self.beam_width = 10
        self.top_wall = (self.beam_width, 5)
        self.top_wall_size = (self.width_arena - (2*self.beam_width), 5)
        self.bottom_wall = (self.beam_width, self.height_arena - (self.beam_width - 5))
        self.bottom_wall_size = (self.width_arena - (2*self.beam_width), 5)

    def draw_arena(self):
        self.goalpost_offset = (self.height_arena - self.goalpost_size) / 2
        _goalpost_inferior_pos = self.goalpost_offset + self.goalpost_size
        _beam_color = colors.WHITE

        def draw_beam(color, start_pos, width):
            pygame.draw.rect(self.game.screen, color, (start_pos,
                             (width, start_pos[1] + self.goalpost_offset)))

        draw_beam(_beam_color, (0, 0), self.beam_width)
        draw_beam(_beam_color, (0, _goalpost_inferior_pos), self.beam_width)
        draw_beam(_beam_color, (self.width_arena -
                  self.beam_width, 0), self.beam_width)
        draw_beam(_beam_color, (self.width_arena - self.beam_width,
                  _goalpost_inferior_pos), self.beam_width)

        pygame.draw.rect(self.game.screen, colors.RED,
                         (self.top_wall, self.top_wall_size))
        pygame.draw.rect(self.game.screen, colors.RED,
                         (self.bottom_wall, self.bottom_wall_size))

    def draw_objects(self):
        self.game.ball.draw(self.game.screen)
        self.game.p1.draw(self.game.screen)
        self.game.p2.draw(self.game.screen)

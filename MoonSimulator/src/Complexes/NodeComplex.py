import pygame

from .Complex import Complex


class NodeComplex(Complex):

    def __init__(self, name, position)-> None:
        super().__init__(name, position, 1)

    def OnRender(self, surface: pygame.Surface)-> None:
        pass

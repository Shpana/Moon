import pygame


class Input(object):

    @staticmethod
    def GetMouseX()-> int:
        """ Returns the x coordinate of the mouse.
        |
        """
        return pygame.mouse.get_pos()[0]

    @staticmethod
    def GetMouseY()-> int:
        """ Returns the y coordinate of the mouse.
        |
        """
        return pygame.mouse.get_pos()[1]

    @staticmethod
    def GetMousePosition()-> tuple:
        """ Returns the coordinates of the mouse.
        |
        """
        return pygame.mouse.get_pos()

    @staticmethod
    def IsKeyPressed(key: int)-> bool:
        """ Returns whether a key is pressed.
        |
        |-If this key is pressed returns True, else returns False.
        """
        return pygame.key.get_pressed()[key]

    @staticmethod
    def IsMouseButtonPressed(button: int)-> bool:
        """ Returns whether a mouse button is pressed.
        |
        |-If this mouse button is pressed returns True, else returns False.
        """
        return pygame.mouse.get_pressed()[button]

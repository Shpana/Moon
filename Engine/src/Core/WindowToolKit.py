import pygame


class WindowToolKit(object):

    @staticmethod
    def IsWindowMinimized()-> bool:
        return not (pygame.key.get_focused() or pygame.mouse.get_focused())

    @staticmethod
    def GetWindowTitle()-> str:
        return pygame.display.get_caption()

    @staticmethod
    def GetWindowSurface()-> pygame.Surface:
        return pygame.display.get_surface()

    @staticmethod
    def GetWindowSurfaceSize()-> tuple:
        return pygame.display.get_surface().get_size()

    @staticmethod
    def GetDriver()-> str:
        return pygame.display.get_driver()

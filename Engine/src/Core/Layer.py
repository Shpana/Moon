import pygame
import pygame_gui
import Engine


class Layer(object):

    def __init__(self, name: str = "Layer")-> None:
        self.m_DebugName = name

    def OnAttach(self)-> None:
        pass

    def OnGuiAttach(self, manager: pygame_gui.UIManager)-> None:
        pass

    def OnDetach(self)-> None:
        pass

    def OnUpdate(self, dt: float)-> None:
        pass

    def OnGuiRender(self, manager: pygame_gui.UIManager)-> None:
        pass

    def OnEvent(self, event: pygame.event.Event)-> None:
        pass

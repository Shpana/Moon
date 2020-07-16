import pygame
import Engine


class WindowProps(object):

    def __init__(self, title: str = "Application", width: int = 900, height: int = 600, modes: int = 0) -> None:
        self.Title = title
        self.Width = width
        self.Height = height
        self.Modes = modes
        self.EventCallback = None


class Window(object):

    def __init__(self, props: WindowProps)-> None:
        self.m_Props = props

        self.m_NativeWindow = pygame.display.set_mode((props.Width, props.Height), props.Modes)

        pygame.display.set_caption(props.Title)

    def OnUpdate_(self)-> None:
        for event in pygame.event.get():
            self.m_Props.EventCallback(event)

        pygame.display.update()

    def SetTitle(self, title: str)-> None:
        self.m_Props.Title = title
        pygame.display.set_caption(props.Title)

    def SetSize(self, width: int, height: int)-> None:
        self.m_Props.Width, self.m_Props.Height = width, height
        self.m_NativeWindow = pygame.display.set_mode((width, height), self.m_Props.Modes)

    def SetModes(self, modes: int)-> None:
        self.m_Props.Modes = modes
        self.m_NativeWindow = pygame.display.set_mode((self.m_Props.Width, self.m_Props.Height), modes)

    def SetEventCallback(self, callback)-> None:
        self.m_Props.EventCallback = callback

    def GetNativeWindow(self)-> pygame.Surface:
        return self.m_NativeWindow

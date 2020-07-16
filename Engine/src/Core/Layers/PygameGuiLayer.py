import pygame
import pygame_gui
import Engine


class PygameGuiLayer(Engine.Layer):

    def __init__(self)-> None:
        super().__init__("PygameGuiLayer")

    def OnAttach(self)-> None:
        self.m_Manager = pygame_gui.UIManager(Engine.WindowToolKit.GetWindowSurfaceSize())
        Engine.Log.Assert(self.m_Manager, "Failed to create UIManager!")

        Engine.Log.Info("PygameGui was successfully initialized.")

    def OnUpdate(self, dt: float)-> None:
        self.m_Manager.update(dt)

    def OnEvent(self, event: pygame.event.Event)-> None:
        self.m_Manager.process_events(event)

    def GetManager(self)-> pygame_gui.UIManager:
        return self.m_Manager

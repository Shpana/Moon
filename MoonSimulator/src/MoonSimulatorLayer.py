import sys
sys.path.append("../../")
import pygame
import pygame_gui
import Engine

from GlobalClock import GlobalClock


class MoonSimulatorLayer(Engine.Layer):

    s_Paused: bool = False

    def OnAttach(self)-> None:
        self.m_SimulationSurfacePosition = (0, 0)
        self.m_Color = (35, 45, 51)

        self.m_SimulationSurface = pygame.Surface((1000, 700))
        self.m_SimulationSurface.fill(self.m_Color)

    def OnUpdate(self, dt: float)-> None:
        windowSurface = Engine.WindowToolKit.GetWindowSurface()

        if (not MoonSimulatorLayer.s_Paused):
            GlobalClock.Tick()

        windowSurface.blit(self.m_SimulationSurface, self.m_SimulationSurfacePosition)

    @staticmethod
    def ResumeSimulation()-> None:
        MoonSimulatorLayer.s_Paused = False

    @staticmethod
    def PauseSimulation()-> None:
        MoonSimulatorLayer.s_Paused = True

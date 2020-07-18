import sys
import time
sys.path.append("../../")
import pygame
import pygame_gui
import Engine

from Time import Time

from ResourcesData import ResourcesData

from Time import GlobalClock

from DataLogger import DataLogger

from Navigation.Map import Map

from Navigation.MapNavigator import MapNavigator

from Cosmonauts.Cosmonaut import Cosmonaut


class MoonSimulatorLayer(Engine.Layer):

    s_Paused: bool = False

    s_SimulationSpeed: float = 1 / 10000

    def OnAttach(self)-> None:
        self.m_SimulationSurfacePosition = (0, 0)
        self.m_Color = (35, 45, 51)

        DataLogger.Init("testMap.log", "TestLog")
        DataLogger.DisableLogging()

        self.m_Map = Map()
        self.m_Map.LoadMapFromJson("Data/maps/TestMap.json")

        MapNavigator.Init(self.m_Map)

        self.m_Consmonaut = Cosmonaut("ResidentialComplex", Time("0.00.00"), Time("0.12.00"))

        self.m_SimulationSurface = pygame.Surface((1000, 700))

    def OnUpdate(self, dt: float)-> None:
        windowSurface = Engine.WindowToolKit.GetWindowSurface()

        if (not MoonSimulatorLayer.s_Paused):
            self.m_SimulationSurface.fill(self.m_Color)

            self.m_Consmonaut.OnUpdate(dt)
            self.m_Consmonaut.OnRender(self.m_SimulationSurface)

            self.m_Map.OnUpdate(dt)
            self.m_Map.OnRender(self.m_SimulationSurface)

            GlobalClock.Tick()

        time.sleep(MoonSimulatorLayer.s_SimulationSpeed)

        windowSurface.blit(self.m_SimulationSurface, self.m_SimulationSurfacePosition)

    def OnEvent(self, event: pygame.event.Event)-> None:
        self.m_Map.OnEvent(event)

    @staticmethod
    def SetSimulationSpeed(speed: float)-> None:
        MoonSimulatorLayer.s_SimulationSpeed = 1 / speed

    @staticmethod
    def ResumeSimulation()-> None:
        MoonSimulatorLayer.s_Paused = False

    @staticmethod
    def PauseSimulation()-> None:
        MoonSimulatorLayer.s_Paused = True

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

from Cosmonauts.ControlCenter import ControlCenter


class MoonSimulatorLayer(Engine.Layer):

    s_Paused: bool = False

    s_SimulationSpeed: float = 1 / 10000

    def OnAttach(self)-> None:
        self.m_SimulationSurface = pygame.Surface((1000, 700))
        self.m_SimulationSurfacePosition = (0, 0)
        self.m_Color = (35, 45, 51)
        self.m_TotalFrameTimeSum = 0.0

        DataLogger.Init("testMap.log", "TestLog")
        DataLogger.DisableLogging()

        self.m_Map = Map()
        self.m_Map.LoadMapFromJson("Data/maps/DefaultBaseMap.json")

        MapNavigator.Init(self.m_Map)

        ControlCenter.Init()
        ControlCenter.LoadCommandFromJson("Data/commands/TestCommand.json")

    def OnUpdate(self, dt: float)-> None:
        windowSurface = Engine.WindowToolKit.GetWindowSurface()
        isNewSimulationFrame = self.m_TotalFrameTimeSum >= MoonSimulatorLayer.s_SimulationSpeed

        if (not MoonSimulatorLayer.s_Paused and isNewSimulationFrame):
            self.m_TotalFrameTimeSum = 0.0
            self.m_SimulationSurface.fill(self.m_Color)

            if (GlobalClock.GetYears() == 1):
                print(ResourcesData.s_HeliumAmount)
                print(ResourcesData.s_TitaniumAmount)
                print(ResourcesData.s_ElectricityAmount)

            ControlCenter.OnUpdate(dt)
            ControlCenter.OnRender(self.m_SimulationSurface)

            self.m_Map.OnUpdate(dt)
            self.m_Map.OnRender(self.m_SimulationSurface)

            GlobalClock.Tick()

        self.m_TotalFrameTimeSum += dt

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

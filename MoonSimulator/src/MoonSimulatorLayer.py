import sys
sys.path.append("../../")
import pygame
import pygame_gui
import Engine

from GlobalClock import GlobalClock

from DataLogger import DataLogger

from Navigation.Map import Map

from Navigation.MapNavigator import MapNavigator


class MoonSimulatorLayer(Engine.Layer):

    s_Paused: bool = False

    def OnAttach(self)-> None:
        DataLogger.Init("testMap.log", "TestLog")
        self.m_SimulationSurfacePosition = (0, 0)
        self.m_Color = (35, 45, 51)

        self.m_Map = Map()
        self.m_Map.LoadMapFromJson("Data/maps/TestMap.json")

        MapNavigator.Init(self.m_Map)
        print(MapNavigator.FindPath(MapNavigator.FindNodeByName("ResidentialComplex"), MapNavigator.FindNodeByName("TitaniumComplex2")))

        self.m_SimulationSurface = pygame.Surface((1000, 700))

    def OnUpdate(self, dt: float)-> None:
        windowSurface = Engine.WindowToolKit.GetWindowSurface()

        if (not MoonSimulatorLayer.s_Paused):
            GlobalClock.Tick()

            self.m_SimulationSurface.fill(self.m_Color)
            self.m_Map.OnUpdate(dt)
            self.m_Map.OnRender(self.m_SimulationSurface)

        windowSurface.blit(self.m_SimulationSurface, self.m_SimulationSurfacePosition)

    def OnEvent(self, event: pygame.event.Event)-> None:
        self.m_Map.OnEvent(event)

    @staticmethod
    def ResumeSimulation()-> None:
        MoonSimulatorLayer.s_Paused = False

    @staticmethod
    def PauseSimulation()-> None:
        MoonSimulatorLayer.s_Paused = True

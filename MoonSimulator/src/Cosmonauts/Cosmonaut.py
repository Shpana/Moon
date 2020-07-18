import pygame

from Time import Time

from Settings import Settings

from .States.State import State

from .States.StateContext import StateContext

from .States.CosmonautStates import *

from Navigation.MapNavigator import MapNavigator

from Navigation.NavigationNode import NavigationNode


class Cosmonaut(object):

    def __init__(self, location: str, startShift: Time, endShift: Time)-> None:
        self.m_Position = pygame.math.Vector2(MapNavigator.FindNodeByName(location).GetPosition())
        self.m_Size = 6
        self.m_Color = (255, 255, 255)
        self.m_CurrentLocation = location
        self.m_Speed = Settings.GetKilometersInUint() * 1 * Settings.GetTickTimeInHours()

        self.m_StartShift = startShift
        self.m_EndShift = endShift

        self.m_CurrentTarget: NavigationNode = MapNavigator.FindNodeByName("TitaniumComplex2")

        self.m_Context = StateContext(self)
        self.m_CurrentState: State = self.m_Context.Create(RelaxState)

    def OnUpdate(self, dt: float)-> None:
        self.m_CurrentState.OnBehaivour()

    def OnRender(self, surface: pygame.Surface)-> None:
        pygame.draw.rect(surface, self.m_Color, (
            *(self.m_Position - pygame.math.Vector2(self.m_Size / 2)), self.m_Size, self.m_Size))

    def OnEvent(self, event: pygame.event.Event)-> None:
        pass

    def SetCurrentTarget(self, target: NavigationNode)-> None:
        self.m_CurrentTarget = target

    def SetCurrentLocation(self, location: str)-> None:
        self.m_CurrentLocation = location

    def SetCurrentState(self, state: State, *params)-> None:
        self.m_CurrentState = self.m_Context.Create(state, *params)

    def GetSpeed(self)-> float:
        return self.m_Speed

    def GetPosition(self)-> pygame.math.Vector2:
        return self.m_Position

    def GetCurrentTarget(self)-> NavigationNode:
        return self.m_CurrentTarget

    def GetCurrentLocation(self)-> str:
        return self.m_CurrentLocation

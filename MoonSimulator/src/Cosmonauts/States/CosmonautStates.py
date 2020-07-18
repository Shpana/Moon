import pygame

from .State import State

from Time import GlobalClock

from Time import Time

from Navigation.NodeStack import NodeStack

from Navigation.MapNavigator import MapNavigator


class TravelState(State):

    def __init__(self, master, to: str)-> None:
        super().__init__(master)

        self.m_NodeStack = NodeStack(master.GetCurrentLocation(), to)

        self.m_CurrentTarget =  self.m_NodeStack.GetNextPoint()

    def OnBehaivour(self)-> None:
        interpolationRatio = self.m_Master.GetSpeed() / self.m_Master.GetPosition().distance_to(self.m_CurrentTarget.GetPosition())

        if (interpolationRatio >= 1):
            self.m_Master.m_Position = pygame.math.Vector2(self.m_CurrentTarget.GetPosition())
            self.m_Master.SetCurrentLocation(self.m_CurrentTarget.GetName())

            self.m_CurrentTarget = self.m_NodeStack.GetNextPoint()

            if (self.m_CurrentTarget == None):
                self.m_Master.SetCurrentState(RelaxState)

        else:
            self.m_Master.m_Position = self.m_Master.m_Position.lerp(self.m_CurrentTarget.GetPosition(), interpolationRatio)

class RelaxState(State):

    def OnBehaivour(self)-> None:
        if (Time.IsWorkTime(self.m_Master.m_StartShift, self.m_Master.m_EndShift)
                and self.m_Master.GetCurrentLocation() == self.m_Master.GetCurrentTarget().GetName()):
            self.m_Master.SetCurrentState(WorkState)

        else:
            if (GlobalClock.GetHours() == self.m_Master.m_StartShift.GetHours() and GlobalClock.GetMinutes() == self.m_Master.m_StartShift.GetMinutes()
                    and self.m_Master.GetCurrentLocation() != self.m_Master.GetCurrentTarget().GetName()):
                self.m_Master.SetCurrentState(TravelState, self.m_Master.GetCurrentTarget().GetName())


class WorkState(State):

    def OnBehaivour(self)-> None:
        if (GlobalClock.GetHours() == self.m_Master.m_EndShift.GetHours() and GlobalClock.GetMinutes() == self.m_Master.m_EndShift.GetMinutes()
                and self.m_Master.GetCurrentLocation() != "ResidentialComplex"):
            self.m_Master.SetCurrentState(TravelState, "ResidentialComplex")

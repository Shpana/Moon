import pygame

from Navigation.NavigationNode import NavigationNode

from .Behaivour.NoBehaivours import *

class Complex(NavigationNode):

    def __init__(self, name: str, position: tuple, size: int = 10)-> None:
        super().__init__(name, position, size)

        self.m_ComplexBehaivour = NoComplexBehaivour()
        self.m_PorductionBehaivour = NoPorductionBehaivour()
        self.m_ExpensesBehaivour = NoExpensesBehaivour()
        self.m_DurabilityBehaivour = NoDurabilityBehaivour()

    def OnUpdate(self, dt: float)-> None:
        if (self.IsActive()):
            self.m_ComplexBehaivour.OnBehaivour()
            self.m_PorductionBehaivour.OnBehaivour()
            self.m_ExpensesBehaivour.OnBehaivour()
            self.m_DurabilityBehaivour.OnBehaivour()

    def OnEvent(self, event: pygame.event.Event)-> None:
        pass

    def IsBroken(self)-> bool:
        return self.m_DurabilityBehaivour.IsBroken()

    def GetPorduction(self)-> float:
        return self.m_PorductionBehaivour.GetPorduction()

    def GetDurability(self)-> float:
        return self.m_DurabilityBehaivour.GetDurability()

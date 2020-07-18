import pygame

from Navigation.NavigationNode import NavigationNode

from .Behaivour.NoBehaivours import *

from .ComplexContext import ComplexContext


class Complex(NavigationNode):

    def __init__(self, name: str, position: tuple, size: int = 10)-> None:
        super().__init__(name, position, size)
        self.m_Active = True

        self.m_Context = ComplexContext(self)

        self.m_ComplexBehaivour = self.m_Context.Create(NoComplexBehaivour)
        self.m_PorductionBehaivour = self.m_Context.Create(NoPorductionBehaivour)
        self.m_ExpensesBehaivour = self.m_Context.Create(NoExpensesBehaivour)
        self.m_DurabilityBehaivour = self.m_Context.Create(NoDurabilityBehaivour)

    def OnUpdate(self, dt: float)-> None:
        if (self.IsActive()):
            self.m_ComplexBehaivour.OnBehaivour()
            self.m_PorductionBehaivour.OnBehaivour()
            self.m_ExpensesBehaivour.OnBehaivour()
            self.m_DurabilityBehaivour.OnBehaivour()

    def OnEvent(self, event: pygame.event.Event)-> None:
        pass

    def IsActive(self)-> bool:
        return self.m_Active

    def Activate(self)-> None:
        self.m_Active = True

    def Diactivete(self)-> None:
        self.m_Active = False

    def IsBroken(self)-> bool:
        return self.m_DurabilityBehaivour.IsBroken()

    def GetPorduction(self)-> float:
        return self.m_PorductionBehaivour.GetPorduction()

    def GetDurability(self)-> float:
        return self.m_DurabilityBehaivour.GetDurability()

import abc
import pygame

from Navigation.NavigationNode import NavigationNode

from .Behaivour.NoBehaivours import *

from .ComplexContext import ComplexContext


class Complex(NavigationNode):

    def __init__(self, name: str, position: tuple, size: int)-> None:
        super().__init__(name, position, size)
        self.m_Active = True

        self.m_Context = ComplexContext(self)

        self.m_ComplexBehaivour = self.m_Context.Create(NoComplexBehaivour)
        self.m_PorductionBehaivour = self.m_Context.Create(NoPorductionBehaivour)
        self.m_ExpensesBehaivour = self.m_Context.Create(NoExpensesBehaivour)
        self.m_DurabilityBehaivour = self.m_Context.Create(NoDurabilityBehaivour)

    def OnWork(self)-> None:
        self.m_DurabilityBehaivour.AddDurability()

    def OnUpdate(self, dt: float)-> None:
        if (self.IsActive()):
            print(self.GetDurability())
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
        self.m_Color = (150, 150, 150)
        self.m_Active = False

    def IsBroken(self)-> bool:
        return self.m_DurabilityBehaivour.IsBroken()

    def GetDurability(self)-> float:
        return self.m_DurabilityBehaivour.GetDurability()

    @abc.abstractstaticmethod
    def GetStaticType()-> str:
        pass

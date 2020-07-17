import pygame


class Complex(object):

    def __init__(self, position: tuple)-> None:
        self.m_Radius = 10
        self.m_Position = position
        self.m_Active = True

        self.m_ComplexBehaivour = None
        self.m_PorductionBehaivour = None
        self.m_ExpensesBehaivour = None
        self.m_DurabilityBehaivour = None

    def OnUpdate(self, dt: float)-> None:
        pass

    def OnRender(self, surface: pygame.Surface)-> None:
        pass

    def OnEvent(self, event: pygame.event.Event)-> None:
        pass

    def OnBehaivour(self)-> None:
        if (self.IsActive()):
            self.m_ComplexBehaivour.OnBehaivour()
            self.m_PorductionBehaivour.OnBehaivour()
            self.m_ExpensesBehaivour.OnBehaivour()
            self.m_DurabilityBehaivour.OnBehaivour()

    def IsActive(self)-> bool:
        return self.m_Active

    def IsBroken(self)-> bool:
        return self.m_DurabilityBehaivour.IsBroken()

    def GetPorduction(self)-> float:
        return self.m_PorductionBehaivour.GetPorduction()

    def GetDurability(self)-> float:
        return self.m_DurabilityBehaivour.GetDurability()

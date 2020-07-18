from .Complex import Complex

from .Behaivour.HeliumBehaivours import *


class HeliumComplex(Complex):

    def __init__(self, name: str, position: tuple)-> None:
        super().__init__(name, position, 10)
        self.m_Color = (255, 203, 107)

        self.m_ComplexBehaivour = self.m_Context.Create(HeliumComplexBehaivour)
        self.m_PorductionBehaivour = self.m_Context.Create(HeliumPorductionBehaivour)
        self.m_ExpensesBehaivour = self.m_Context.Create(HeliumExpensesBehaivour)
        self.m_DurabilityBehaivour = self.m_Context.Create(HeliumDurabilityBehaivour)

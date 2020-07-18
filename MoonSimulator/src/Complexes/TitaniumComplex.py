from .Complex import Complex

from .Behaivour.TitaniumBehaivours import *


class TitaniumComplex(Complex):

    def __init__(self, name: str, position: tuple)-> None:
        super().__init__(name, position, 10)
        self.m_Color = (130, 158, 204)

        self.m_ComplexBehaivour = self.m_Context.Create(TitaniumComplexBehaivour)
        self.m_PorductionBehaivour = self.m_Context.Create(TitaniumPorductionBehaivour)
        self.m_ExpensesBehaivour = self.m_Context.Create(TitaniumExpensesBehaivour)
        self.m_DurabilityBehaivour = self.m_Context.Create(TitaniumDurabilityBehaivour)

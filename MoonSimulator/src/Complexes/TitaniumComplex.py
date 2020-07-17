from .Complex import Complex

from .Behaivour.TitaniumBehaivours import *


class TitaniumComplex(Complex):

    def __init__(self, name: str, position: tuple)-> None:
        super().__init__(name, position, 10)
        self.m_Color = (130, 158, 204)

        self.m_ComplexBehaivour = TitaniumComplexBehaivour()
        self.m_PorductionBehaivour = TitaniumPorductionBehaivour()
        self.m_ExpensesBehaivour = TitaniumExpensesBehaivour()
        self.m_DurabilityBehaivour = TitaniumDurabilityBehaivour()

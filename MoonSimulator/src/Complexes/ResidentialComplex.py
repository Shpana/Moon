from .Complex import Complex

from .Behaivour.ResidentialBehaivours import *


class ResidentialComplex(Complex):

    def __init__(self, name, position)-> None:
        super().__init__(name, position, 15)
        self.m_Color = (195, 232, 141)

        self.m_ComplexBehaivour = ResidentialComplexBehaivour()
        self.m_PorductionBehaivour = ResidentialPorductionBehaivour()
        self.m_ExpensesBehaivour = ResidentialExpensesBehaivour()
        self.m_DurabilityBehaivour = ResidentialDurabilityBehaivour()

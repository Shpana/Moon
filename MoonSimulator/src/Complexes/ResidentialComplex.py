from .Complex import Complex

from .Behaivour.ResidentialBehaivours import *


class ResidentialComplex(Complex):

    def __init__(self, name, position)-> None:
        super().__init__(name, position, 15)
        self.m_Color = (195, 232, 141)

        self.m_ComplexBehaivour = self.m_Context.Create(ResidentialComplexBehaivour)
        self.m_PorductionBehaivour = self.m_Context.Create(ResidentialPorductionBehaivour)
        self.m_ExpensesBehaivour = self.m_Context.Create(ResidentialExpensesBehaivour)
        self.m_DurabilityBehaivour = self.m_Context.Create(ResidentialDurabilityBehaivour)

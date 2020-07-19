from .Complex import Complex

from .Behaivour.ElectricityBehaivours import *


class ElectricityComplex(Complex):

    def __init__(self, name: str, position: tuple)-> None:
        super().__init__(name, position, 10)
        self.m_Color = (189, 146, 205)

        self.m_ComplexBehaivour = self.m_Context.Create(ElectricityComplexBehaivour)
        self.m_PorductionBehaivour = self.m_Context.Create(ElectricityPorductionBehaivour)
        self.m_ExpensesBehaivour = self.m_Context.Create(ElectricityExpensesBehaivour)
        self.m_DurabilityBehaivour = self.m_Context.Create(ElectricityDurabilityBehaivour)

    @staticmethod
    def GetStaticType()-> str:
        return "ElectricityComplex"

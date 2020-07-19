from .IComplexBehaivour import IComplexBehaivour
from .IDurabilityBehaivour import IDurabilityBehaivour
from .IExpensesBehaivour import IExpensesBehaivour
from .IPorductionBehaivour import IPorductionBehaivour

from ResourcesData import ResourcesData


class ElectricityComplexBehaivour(IComplexBehaivour):

    def OnBehaivour(self)-> None:
        pass


class ElectricityDurabilityBehaivour(IDurabilityBehaivour):

    def OnBehaivour(self)-> None:
        super().OnBehaivour()

        if (self.m_Durability <= 0.0):
            self.m_Master.Diactivete()


class ElectricityExpensesBehaivour(IExpensesBehaivour):

    def OnBehaivour(self)-> None:
        pass


class ElectricityPorductionBehaivour(IPorductionBehaivour):

    def OnBehaivour(self)-> None:
        pass

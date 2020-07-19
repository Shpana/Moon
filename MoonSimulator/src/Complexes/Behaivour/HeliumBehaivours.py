from .IComplexBehaivour import IComplexBehaivour
from .IDurabilityBehaivour import IDurabilityBehaivour
from .IExpensesBehaivour import IExpensesBehaivour
from .IPorductionBehaivour import IPorductionBehaivour

from ResourcesData import ResourcesData


class HeliumComplexBehaivour(IComplexBehaivour):

    def OnBehaivour(self)-> None:
        pass


class HeliumDurabilityBehaivour(IDurabilityBehaivour):

    def OnBehaivour(self)-> None:
        super().OnBehaivour()

        if (self.m_Durability <= 0.0):
            self.m_Master.Diactivete()


class HeliumExpensesBehaivour(IExpensesBehaivour):

    def OnBehaivour(self)-> None:
        pass


class HeliumPorductionBehaivour(IPorductionBehaivour):

    def OnBehaivour(self)-> None:
        pass

from .IComplexBehaivour import IComplexBehaivour
from .IDurabilityBehaivour import IDurabilityBehaivour
from .IExpensesBehaivour import IExpensesBehaivour
from .IPorductionBehaivour import IPorductionBehaivour

from ResourcesData import ResourcesData


class TitaniumComplexBehaivour(IComplexBehaivour):

    def OnBehaivour(self)-> None:
        pass


class TitaniumDurabilityBehaivour(IDurabilityBehaivour):

    def OnBehaivour(self)-> None:
        super().OnBehaivour()

        if (self.m_Durability <= 0.0):
            self.m_Master.Diactivete()


class TitaniumExpensesBehaivour(IExpensesBehaivour):

    def OnBehaivour(self)-> None:
        pass


class TitaniumPorductionBehaivour(IPorductionBehaivour):

    def OnBehaivour(self)-> None:
        pass

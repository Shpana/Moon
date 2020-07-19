from .IComplexBehaivour import IComplexBehaivour
from .IDurabilityBehaivour import IDurabilityBehaivour
from .IExpensesBehaivour import IExpensesBehaivour
from .IPorductionBehaivour import IPorductionBehaivour


class NoComplexBehaivour(IComplexBehaivour):

    def OnBehaivour(self)-> None:
        pass


class NoDurabilityBehaivour(IDurabilityBehaivour):

    def OnBehaivour(self)-> None:
        if (self.m_Durability <= 0.0):
            self.m_Master.Diactivete()


class NoExpensesBehaivour(IExpensesBehaivour):

    def OnBehaivour(self)-> None:
        pass


class NoPorductionBehaivour(IPorductionBehaivour):

    def OnBehaivour(self)-> None:
        pass

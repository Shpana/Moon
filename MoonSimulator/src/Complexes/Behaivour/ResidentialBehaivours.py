from .IComplexBehaivour import IComplexBehaivour
from .IDurabilityBehaivour import IDurabilityBehaivour
from .IExpensesBehaivour import IExpensesBehaivour
from .IPorductionBehaivour import IPorductionBehaivour

from ResourcesData import ResourcesData


class ResidentialComplexBehaivour(IComplexBehaivour):

    def OnBehaivour(self)-> None:
        pass


class ResidentialDurabilityBehaivour(IDurabilityBehaivour):

    def OnBehaivour(self)-> None:
        pass


class ResidentialExpensesBehaivour(IExpensesBehaivour):

    def OnBehaivour(self)-> None:
        if (ResourcesData.CanAddElectricity()):
            ResourcesData.AddElectricity(-1.7, "Затраты на обслуживание жилого комплеса")
        else:
            pass

class ResidentialPorductionBehaivour(IPorductionBehaivour):

    def OnBehaivour(self)-> None:
        pass

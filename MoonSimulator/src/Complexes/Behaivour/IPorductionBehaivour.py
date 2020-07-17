import abc


class IPorductionBehaivour(abc.ABC):

    def __init__(self, production: float)-> None:
        self.m_Porduction = production

    @abc.abstractmethod
    def OnBehaivour(self)-> None:
        pass

    def GetPorduction(self)-> float:
        return self.m_Porduction

import abc


class IDurabilityBehaivour(abc.ABC):

    def __init__(self, durability: float)-> None:
        self.m_MaxDurability = durability

    @abc.abstractmethod
    def OnBehaivour(self)-> None:
        pass

    def IsBroken(self)-> bool:
        return self.m_MaxDurability < 0

    def GetDurability(self)-> float:
        return self.m_MaxDurability

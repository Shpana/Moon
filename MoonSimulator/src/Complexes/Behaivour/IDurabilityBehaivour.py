import abc

from Settings import Settings

class IDurabilityBehaivour(abc.ABC):

    def __init__(self, master)-> None:
        self.m_Master = master

        self.m_Durability = 100
        self.m_MaxDurability = 100

    @abc.abstractmethod
    def OnBehaivour(self)-> None:
        self.m_Durability -= 0.01 * Settings.GetTickTimeInHours()

    def AddDurability(self)-> None:
        self.m_Durability = min(self.m_Durability + 0.1 * Settings.GetTickTimeInHours(), self.m_MaxDurability)

    def GetDurability(self)-> float:
        return self.m_Durability

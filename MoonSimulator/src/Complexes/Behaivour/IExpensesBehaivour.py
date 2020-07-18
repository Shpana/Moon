import abc


class IExpensesBehaivour(abc.ABC):

    def __init__(self, master)-> None:
        self.m_Master = master

    @abc.abstractmethod
    def OnBehaivour(self)-> None:
        pass

import abc


class IExpensesBehaivour(abc.ABC):

    @abc.abstractmethod
    def OnBehaivour(self)-> None:
        pass

import abc


class IExpensesBehaivour(abc.ABC):

    def __init__(self, expenses: float)-> None:
        self.m_Expenses = expenses

    @abc.abstractmethod
    def OnBehaivour(self)-> None:
        pass

    def GetExpenses(self)-> float:
        return self.m_Expenses

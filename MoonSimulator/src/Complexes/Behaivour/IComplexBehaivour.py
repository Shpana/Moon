import abc


class IComplexBehaivour(abc.ABC):

    @abc.abstractmethod
    def OnBehaivour(self)-> None:
        pass

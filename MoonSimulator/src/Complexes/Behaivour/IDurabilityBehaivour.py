import abc


class IDurabilityBehaivour(abc.ABC):

    @abc.abstractmethod
    def OnBehaivour(self)-> None:
        pass

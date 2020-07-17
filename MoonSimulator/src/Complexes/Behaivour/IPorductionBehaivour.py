import abc


class IPorductionBehaivour(abc.ABC):

    @abc.abstractmethod
    def OnBehaivour(self)-> None:
        pass

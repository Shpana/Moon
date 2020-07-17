from DataLogger import DataLogger


class ResourcesData(object):

    s_HeliumAmount: float = 0.0

    s_ElectricityAmount: float = 0.0

    s_TitaniumAmount: float = 0.0

    @staticmethod
    def CanAddHelium()-> bool:
        return ResourcesData.s_HeliumAmount > 0.0

    @staticmethod
    def AddHelium(amount: float, message: str)-> None:
        ResourcesData.s_HeliumAmount += amount
        DataLogger.Log(f"{message}({abs(amount)}).")

    @staticmethod
    def CanAddElectricity()->bool:
        return ResourcesData.s_ElectricityAmount > 0.0

    @staticmethod
    def AddElectricity(amount: float, message: str)-> None:
        ResourcesData.s_ElectricityAmount += amount
        DataLogger.Log(f"{message}({abs(amount)}).")

    @staticmethod
    def CanAddTitnium()-> bool:
        return ResourcesData.s_TitaniumAmount > 0.0

    @staticmethod
    def AddTitnium(amount: float, message: str)-> None:
        ResourcesData.s_TitaniumAmount += amount
        DataLogger.Log(f"{message}({abs(amount)}).")

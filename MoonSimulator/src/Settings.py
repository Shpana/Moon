class Settings(object):

    s_TickTimeInMinutes = 30

    s_TickTimeInHours = s_TickTimeInMinutes / 60

    s_KilometersInUint = 50

    s_UnitToKilometers = 1 / s_KilometersInUint

    @staticmethod
    def GetTickTimeInMinutes()-> int:
        return Settings.s_TickTimeInMinutes

    @staticmethod
    def GetTickTimeInHours()-> float:
        return Settings.s_TickTimeInHours

    @staticmethod
    def GetKilometersInUint()-> int:
        return Settings.s_KilometersInUint

    @staticmethod
    def GetUnitToKilometers()-> float:
        return Settings.s_UnitToKilometers

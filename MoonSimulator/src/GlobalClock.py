class GlobalClock(object):

    s_Hours: int = 0

    @staticmethod
    def Tick()-> None:
        GlobalClock.s_Hours += 1

    @staticmethod
    def GetDate()-> str:
        return f"D:{GlobalClock.s_Hours // 24}, T:{GlobalClock.s_Hours % 24}.00"

    @staticmethod
    def GetMinutes()-> int:
        return GlobalClock.s_Hours * 60

    @staticmethod
    def GetHours()-> int:
        return GlobalClock.s_Hours

    @staticmethod
    def GetDays()-> int:
        return GlobalClock.s_Hours // 24

    @staticmethod
    def GetYears()-> int:
        return GlobalClock.GetDays() // 365

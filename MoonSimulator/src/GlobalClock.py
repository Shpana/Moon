class GlobalClock(object):

    s_Time: int = 0

    @staticmethod
    def Tick()-> None:
        GlobalClock.s_Time += 1

    @staticmethod
    def GetDate()-> str:
        return f"D:{GlobalClock.GetDays()}, T:{GlobalClock.GetHours() % 24}.{GlobalClock.GetMinutes() % 60}"

    @staticmethod
    def GetMinutes()-> int:
        return GlobalClock.s_Time * 30

    @staticmethod
    def GetHours()-> int:
        return GlobalClock.s_Time // 2

    @staticmethod
    def GetDays()-> int:
        return GlobalClock.GetHours() // 24

    @staticmethod
    def GetYears()-> int:
        return GlobalClock.GetDays() // 365

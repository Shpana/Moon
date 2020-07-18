class Time : pass

class GlobalClock(object):

    s_Time: int = 0

    @staticmethod
    def Tick()-> None:
        GlobalClock.s_Time += 1

    @staticmethod
    def GetCurrentTime()-> Time:
        return Time(f"00.{GlobalClock.GetHours() % 24}.{GlobalClock.GetMinutes() % 60}")

    @staticmethod
    def GetDate()-> str:
        return f"D:{GlobalClock.GetDays()}, T:{GlobalClock.GetHours() % 24}.{GlobalClock.GetMinutes() % 60}"

    @staticmethod
    def GetMinutes()-> int:
        return (GlobalClock.s_Time * 30) % 60

    @staticmethod
    def GetHours()-> int:
        return (GlobalClock.s_Time // 2) % 24

    @staticmethod
    def GetDays()-> int:
        return (GlobalClock.s_Time // 2) // 24

    @staticmethod
    def GetYears()-> int:
        return GlobalClock.GetDays() // 365

class Time(object):

    def __init__(self, time: str)-> None:
        self.m_Time = time

        self.m_Days, self.m_Hours, self.m_Minutes = map(int, time.split("."))

    def __lt__(self, other: Time)-> bool:
        return (self.GetDays() < other.GetDays() and self.GetHours() < other.GetHours() and self.GetMinutes() < other.GetMinutes())

    def __gt__(self, other: Time)-> bool:
        return (self.GetDays() > ther.GetDays() and self.GetHours() > other.GetHours() and self.GetMinutes() > other.GetMinutes())

    def __le__(self, other: Time)-> bool:
        return (self.GetDays() <= other.GetDays() and self.GetHours() <= other.GetHours() and self.GetMinutes() <= other.GetMinutes())

    def __ge__(self, other: Time)-> bool:
        return  (self.GetDays() >= other.GetDays() and self.GetHours() >= other.GetHours() and self.GetMinutes() >= other.GetMinutes())

    @staticmethod
    def IsWorkTime(startShift: Time, endShift: Time)-> bool:
        time = GlobalClock.GetCurrentTime()

        return startShift <= time <= endShift

    def GetDays(self)-> int:
        return self.m_Days

    def GetHours(self)-> int:
        return self.m_Hours

    def GetMinutes(self)-> int:
        return self.m_Minutes

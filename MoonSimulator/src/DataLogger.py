import logging

from Time import GlobalClock


class DataLogger(object):

    s_LogPath = "Data/logs/"

    s_FileFormatter: logging.Formatter = None

    s_Logger: logging.Logger = None

    @staticmethod
    def Init(logFileName: str, logName: str)-> None:
        DataLogger.InitFormatters_()
        DataLogger.InitLoggers_(logFileName)

        DataLogger.Log(f"Creation Log({logName}).")

    @staticmethod
    def EnableLogging()-> None:
        DataLogger.s_Logger.setLevel(logging.DEBUG)

    @staticmethod
    def DisableLogging()-> None:
        DataLogger.s_Logger.setLevel(logging.ERROR)

    @staticmethod
    def InitFormatters_()-> None:
        DataLogger.s_FileFormatter = logging.Formatter("%(message)s")

    @staticmethod
    def InitLoggers_(logFileName: str)-> None:
        DataLogger.s_Logger = logging.getLogger("Data")
        DataLogger.s_Logger.setLevel(logging.DEBUG)

        fileHandler = logging.FileHandler(DataLogger.s_LogPath + logFileName)
        fileHandler.setFormatter(DataLogger.s_FileFormatter)
        DataLogger.s_Logger.addHandler(fileHandler)

    @staticmethod
    def Log(message)-> None:
        DataLogger.s_Logger.info(f"[{GlobalClock.GetDate()}]: {message}")

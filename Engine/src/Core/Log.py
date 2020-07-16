import os
import logging


class Log(object):

    s_DefaultStreamFormatter: logging.Formatter = None

    s_CoreLogger: logging.Logger = None

    @staticmethod
    def Init()-> None:
        Log.InitFormatters_()
        Log.s_CoreLogger = Log.CreateLogger_("Sho")

    @staticmethod
    def InitFormatters_()-> None:
        Log.s_DefaultStreamFormatter = logging.Formatter("[%(name)s::%(levelname)s]: %(message)s")

    @staticmethod
    def CreateLogger_(name: str, logLevel: int = logging.DEBUG)-> logging.Logger:
        logger = logging.getLogger(name)
        logger.setLevel(logLevel)
        logger.addHandler(Log.CreateStreamHandler_())
        return logger

    @staticmethod
    def CreateStreamHandler_()-> logging.StreamHandler:
        streamHandler = logging.StreamHandler()
        streamHandler.setFormatter(Log.s_DefaultStreamFormatter)
        return streamHandler

    @staticmethod
    def Debug(message)-> None:
        Log.s_CoreLogger.debug(message)

    @staticmethod
    def Info(message)-> None:
        Log.s_CoreLogger.info(message)

    @staticmethod
    def Warning(message)-> None:
        Log.s_CoreLogger.warn(message)

    @staticmethod
    def Error(message)-> None:
        Log.s_CoreLogger.error(message)

    @staticmethod
    def Critical(message)-> None:
        Log.s_CoreLogger.critical(message)

    @staticmethod
    def Assert(state: bool, message)-> None:
        if (not state):
            Log.Critical(message)
            os.abort()

    @staticmethod
    def PassAssert(state: bool)-> None:
        Log.Assert(state, "Something wrong!")

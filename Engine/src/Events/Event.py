import pygame
import Engine

class Event(object):

    s_Type = None

    s_UserCategory = None

    s_EventName = None

    def GetDiscriptor()-> dict:
        return dict()

    @classmethod
    def GetType(cls)-> int:
        return cls.s_Type

    @classmethod
    def GetUserCategory(cls)-> int:
        return cls.s_UserCategory

    @classmethod
    def GetEventName(cls)-> str:
        return cls.s_EventName

class EventStack(object):

    def PostEvent(self, event: Event)-> None:
        pygame.event.post(pygame.event.Event(event.GetType(), event.GetDiscriptor()))

    def RepeatEvent(self, eventType: int, time: float)-> None:
        pygame.time.set_timer(eventType, time)


class EventDispatcher(object):

    def __init__(self, event: pygame.event.Event)-> None:
        self.m_HandleEvent = event

    def Dispatch(self, eventType: int, callback)-> None:
        if (self.m_HandleEvent.type == eventType):
            callback(self.m_HandleEvent)

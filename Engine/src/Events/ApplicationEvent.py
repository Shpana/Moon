import pygame
import pygame_gui

from Engine.src.Events.Event import Event
from Engine.src.Events.EventCategory import EventCategory
from Engine.src.Events.EventType import EventType


class AppUpdateEvent(Event):

    s_Type = EventType.AppUpdateEvent

    s_UserCategory = EventCategory.AppEventsCategory

    s_EventName = "AppUpdateEvent"

    def __init__(self, time: float)-> None:
        self.m_DeltaTime = time

    def GetDiscriptor(self)-> dict:
        return {
            "eventName":    AppUpdateEvent.GetEventName(),
            "userCategory": AppUpdateEvent.GetUserCategory(),
            "time":         self.m_DeltaTime,
        }


class AppGuiRenderEvent(Event):

    s_Type = EventType.AppGuiRenderEvent

    s_UserCategory = EventCategory.AppEventsCategory

    s_EventName = "AppGuiRenderEvent"

    def __init__(self, manager: pygame_gui.UIManager)-> None:
        self.m_Manager = manager

    def GetDiscriptor(self)-> dict:
        return {
            "eventName":    AppGuiRenderEvent.GetEventName(),
            "userCategory": AppGuiRenderEvent.GetUserCategory(),
            "manager":      self.m_Manager,
        }

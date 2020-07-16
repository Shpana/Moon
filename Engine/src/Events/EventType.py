import enum
import pygame

class EventType(enum.IntEnum):
    Null = 0
    AppUpdateEvent    =  pygame.USEREVENT + 100
    AppGuiRenderEvent =  pygame.USEREVENT + 101

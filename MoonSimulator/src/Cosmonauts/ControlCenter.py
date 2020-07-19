import json
import pygame
import Cosmonauts.Cosmonaut

from Navigation.MapNavigator import MapNavigator

from Navigation.NavigationNode import NavigationNode

from .TodoStack import TodoStack



class ControlCenter(object):

    s_Cosmonauts: list = list()

    s_TodoStack: TodoStack = None

    @staticmethod
    def Init()-> None:

        ControlCenter.s_TodoStack = TodoStack()

    @staticmethod
    def OnUpdate(dt: float)-> None:
        ControlCenter.s_TodoStack.UpdateTodoList()

        for cosmonaut in ControlCenter.s_Cosmonauts:
            cosmonaut.OnUpdate(dt)

    @staticmethod
    def OnRender(surface: pygame.Surface)-> None:
        for cosmonaut in ControlCenter.s_Cosmonauts:
            cosmonaut.OnRender(surface)

    @staticmethod
    def LoadCommandFromJson(filePath: str)-> None:
        file = open(filePath, "r")

        data = json.load(file)

        for key in data.keys():
            currentCosmonautDiscription = data[key]

            startShift = currentCosmonautDiscription["startShift"]
            startLocation = currentCosmonautDiscription["startLocation"]
            endShift = currentCosmonautDiscription["endShift"]

            for index in range(currentCosmonautDiscription["count"]):
                ControlCenter.s_Cosmonauts.append(Cosmonauts.Cosmonaut.Cosmonaut(startLocation, startShift, endShift))

        file.close()

    @staticmethod
    def GetNextTarget()-> NavigationNode:
        return ControlCenter.s_TodoStack.GetNextTarget()

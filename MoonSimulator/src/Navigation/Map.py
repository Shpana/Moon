import math
import pygame
import json

from .NavigationNode import NavigationNode

from Complexes.ComplexType import ComplexType


class Map(object):

    def __init__(self)-> None:
        self.m_Nodes = list()

    def OnUpdate(self, dt: float)-> None:
        for node in self.m_Nodes:
            node.OnUpdate(dt)

    def OnRender(self, surface: pygame.Surface)-> None:
        for node in self.m_Nodes:
            node.OnRenderConnections(surface)

        for node in self.m_Nodes:
            node.OnRender(surface)

    def OnEvent(self, event: pygame.event.Event)-> None:
        for node in self.m_Nodes:
            node.OnEvent(event)

    def LoadMapFromJson(self, filePath: str)-> None:
        file = open(filePath, "r")

        data = json.load(file)

        for key in data.keys():
            self.m_Nodes.append(ComplexType.GetComplexByType(data[key]["type"])(key, data[key]["position"]))

        for key in data.keys():
            currentNode = self.m_Nodes[data[key]["index"]]

            for neighbor in range(len(data[key]["neighbors"])):
                currentNode.AddNeighbor(self.m_Nodes[data[key]["neighbors"][neighbor]])

        file.close()

    def GetNodes(self)-> list:
        return self.m_Nodes

from .MapNavigator import MapNavigator

from .NavigationNode import NavigationNode


class NodeStack(object):

    def __init__(self, start: str, end: str)-> None:
        self.m_IndexPointer = 0

        self.m_Nodes = MapNavigator.FindPath(MapNavigator.FindNodeByName(start), MapNavigator.FindNodeByName(end))

    def GetNextPoint(self)-> NavigationNode:
        self.m_IndexPointer += 1

        if (self.m_IndexPointer >= len(self.m_Nodes)):
            return None

        return self.m_Nodes[self.m_IndexPointer]

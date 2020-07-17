import pygame


class NavigationNode : pass


class NavigationNode(object):

    def __init__(self, name: str, position: tuple, size: float)-> None:
        self.m_Name = name

        self.m_Position = pygame.math.Vector2(position)
        self.m_Size = size
        self.m_Color = (255, 255, 255)

        self.m_Active = True
        self.m_Neighbors = list()

    def OnUpdate(self, dt: float)-> None:
        pass

    def OnBehaivour(self)-> None:
        pass

    def OnRender(self, surface: pygame.Surface)-> None:
        for neighbor in self.m_Neighbors:
            pygame.draw.line(surface, self.m_Color, self.m_Position, neighbor.GetPosition())

        pygame.draw.rect(surface, self.m_Color, (
            *(self.m_Position - pygame.math.Vector2(self.m_Size / 2)), self.m_Size, self.m_Size))

    def OnEvent(self, event: pygame.event.Event)-> None:
        pass

    def AddNeighbor(self, neighbor: NavigationNode)-> None:
        self.m_Neighbors.append(neighbor)

    def IsActive(self)-> bool:
        return self.m_Active

    def GetName(self)-> str:
        return self.m_Name

    def GetNeighbors(self)-> list:
        return self.m_Neighbors

    def GetPosition(self)-> tuple:
        return self.m_Position

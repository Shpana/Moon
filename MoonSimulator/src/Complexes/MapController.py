import math
from collections import defaultdict

from .Map import Map

from .NavigationNode import NavigationNode


class MapController(object):

    s_MapHandle: Map = None

    s_NavigationWeights: list = dict()

    @staticmethod
    def Init(map: Map)-> None:
        MapController.s_MapHandle = map

        MapController.CalculateNavigationHeights_(map)

    @staticmethod
    def CalculateDistance(start: NavigationNode, end: NavigationNode)-> float:
        dx = start.GetPosition().x - end.GetPosition().x
        dy = start.GetPosition().y - end.GetPosition().y

        return math.sqrt(dx**2 + dy**2)

    @staticmethod
    def FindNodeByName(name: str)-> None:
        for node in MapController.s_MapHandle.GetNodes():
            if (node.GetName() == name):
                return node

    @staticmethod
    def FindPath(start: NavigationNode, end: NavigationNode)-> list:
        nodes = MapController.s_MapHandle.GetNodes()
        navigationHeights = MapController.s_NavigationWeights

        nodesToVisit = {start.GetName()}
        visitedNodes = set()
        tentativeParents = dict()

        distanceFromStrart = defaultdict(lambda: float("inf"))
        distanceFromStrart[start.GetName()] = 0

        while (nodesToVisit):
            current = min([(distanceFromStrart[node], node) for node in nodesToVisit])[1]

            if (current == end.GetName()):
                break

            nodesToVisit.discard(current)
            visitedNodes.add(current)

            for key in navigationHeights[current]:
                neighbour = key
                distance = navigationHeights[current][key]

                if neighbour in visitedNodes:
                    continue

                neighbourDistance = distanceFromStrart[current] + distance

                if neighbourDistance < distanceFromStrart[neighbour]:
                    distanceFromStrart[neighbour] = neighbourDistance
                    nodesToVisit.add(neighbour)
                    tentativeParents[neighbour] = current

        return MapController.DeconstructPath_(tentativeParents, end.GetName())

    @staticmethod
    def CalculateNavigationHeights_(map: Map)-> None:
        for node in map.GetNodes():

            MapController.s_NavigationWeights[node.GetName()] = dict()

            for neighbor in node.GetNeighbors():
                distance = MapController.CalculateDistance(node, neighbor)

                MapController.s_NavigationWeights[node.GetName()][neighbor.GetName()] = distance

    @staticmethod
    def DeconstructPath_(tentativeParents: dict, end: str)-> list:
        cursor = end
        path = []
        while cursor:
            path.append(MapController.FindNodeByName(cursor))
            cursor = tentativeParents.get(cursor)

        return list(reversed(path))

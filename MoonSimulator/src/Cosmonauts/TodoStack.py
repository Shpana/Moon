from Navigation.MapNavigator import MapNavigator

from Navigation.NavigationNode import NavigationNode


class TodoStack(object):

    def __init__(self)-> None:
        self.m_TodoList = list()
        self.m_CurrentIndexPointer = 0

        self.InitTodoList()

    def InitTodoList(self)-> None:
        for complex in MapNavigator.GetMapHandle().GetNodes():
            if (complex.GetStaticType() != "NodeComplex" and complex.GetStaticType() != "ResidentialComplex"):
                self.m_TodoList.append(complex)

        self.UpdateTodoList()

    def UpdateTodoList(self)-> None:
        self.m_TodoList.sort(key=lambda x: x.GetDurability())

        self.m_CurrentIndexPointer = 0

    def GetNextTarget(self)-> NavigationNode:
        self.m_CurrentIndexPointer += 1

        if (self.m_CurrentIndexPointer > len(self.m_TodoList)):
            return

        return self.m_TodoList[self.m_CurrentIndexPointer - 1]

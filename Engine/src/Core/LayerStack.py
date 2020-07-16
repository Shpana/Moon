import Engine

class LayerStack(object):

    def __init__(self)-> None:
        self.m_Layers = list()
        self.m_Overlayers = list()

    def AddLayer(self, layer: Engine.Layer)-> None:
        self.m_Layers.append(layer)

    def PopLayer(self, layer: Engine.Layer)-> None:
        if (not layer in self.m_Layers): return

        self.m_Layers.pop(self.m_Layers.index(layer))

    def AddOverlay(self, layer: Engine.Layer)-> None:
        self.m_Overlayers.append(layer)

    def PopOverlay(self, layer: Engine.Layer)-> None:
        if (not layer in self.m_Overlayers): return

        self.m_Overlayers.pop(self.m_Overlayers.index(layer))

    def GetStack(self)-> tuple:
        return (*self.m_Layers, *self.m_Overlayers)

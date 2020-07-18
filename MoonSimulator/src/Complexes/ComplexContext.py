class ComplexContext(object):

    def __init__(self, master)-> None:
        self.m_Master = master

    def Create(self, behaviour):
        return behaviour(self.m_Master)

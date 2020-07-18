from .State import State


class StateContext(object):

    def __init__(self, master)-> None:
        self.m_Master = master

    def Create(self, state: State, *params)-> None:
        return state(self.m_Master, *params)

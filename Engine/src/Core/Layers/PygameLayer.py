import pygame
import Engine


class PygameLayer(Engine.Layer):


    def __init__(self)-> None:
        super().__init__("PygameLayer")

    def OnAttach(self)-> None:
        pygame.init()
        Engine.Log.Assert(pygame.get_init(), "Failid to init pygame!")

        pygame.key.set_repeat(500, 10)

        Engine.Log.Info("Pygame was successfully initialized.")

    def OnDetach(self)-> None:
        pygame.quit()

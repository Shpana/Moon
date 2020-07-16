import sys
sys.path.append("../")
import pygame
import pygame_gui
import Engine


class TestLayer(Engine.Layer):

    def OnGuiAttach(self, manager: pygame_gui.UIManager)-> None:
        self.m_Slider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(30, 30, 200, 25),
            start_value=0,
            value_range=(0, 1000),
            manager=manager,
        )

    def OnGuiRender(self, manager: pygame_gui.UIManager)-> None:
        manager.draw_ui(Engine.WindowToolKit.GetWindowSurface())


app = Engine.ApplicationRegistry.Create(Engine.WindowProps(modes=pygame.RESIZABLE))
app.AddLayer(TestLayer())
app.Run()

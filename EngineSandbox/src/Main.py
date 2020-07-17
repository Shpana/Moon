import sys
sys.path.append("../../")
import pygame
import pygame_gui
import Engine


class TestLayer(Engine.Layer):

    def OnGuiAttach(self, manager: pygame_gui.UIManager)-> None:
        self.m_Panel = pygame_gui.elements.UIPanel(
            relative_rect=pygame.Rect(30, 30, 250, 200),
            starting_layer_height=1,
            manager=manager,
        )

        self.m_Label = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, 0, 200, 20),
            text="Name: ResidentialComplex",
            manager=manager,
            container=self.m_Panel,
        )

    def OnUpdate(self, dt: float)-> None:
        if (Engine.Input.IsKeyPressed(pygame.K_a)):
            self.m_Panel.hide()
        else:
            self.m_Panel.show()

        Engine.WindowToolKit.GetWindowSurface().fill((18, 19, 25))

    def OnGuiRender(self, manager: pygame_gui.UIManager)-> None:
        manager.draw_ui(Engine.WindowToolKit.GetWindowSurface())


app = Engine.ApplicationRegistry.Create(Engine.WindowProps(modes=pygame.RESIZABLE))
app.AddLayer(TestLayer())
app.Run()

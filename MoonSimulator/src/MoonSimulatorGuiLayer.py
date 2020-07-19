import sys
sys.path.append("../../")
import pygame
import pygame_gui
import Engine

from Time import GlobalClock

from MoonSimulatorLayer import MoonSimulatorLayer


class MoonSimulatorGuiLayer(Engine.Layer):

    def OnAttach(self)-> None:
        self.m_LineWidth = 27

        self.m_ElementsCount = 0

    def OnGuiAttach(self, manager: pygame_gui.UIManager)-> None:
        self.m_Window = pygame_gui.elements.UIPanel(
            relative_rect =pygame.Rect(700, 0, 300, 700),
            starting_layer_height=1,
            manager=manager,
        )

        self.m_StatsLabel = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, self.m_LineWidth * self.m_ElementsCount, 300, self.m_LineWidth),
            text="Moon Simulator Stats",
            manager=manager,
            container=self.m_Window,
        )
        self.m_ElementsCount += 2

        self.m_DayLabel = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, self.m_LineWidth * self.m_ElementsCount, 125, self.m_LineWidth),
            text="Day: ",
            manager=manager,
            container=self.m_Window,
        )
        self.m_ElementsCount += 1

        self.m_ResumButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(125, self.m_LineWidth * self.m_ElementsCount, 150, self.m_LineWidth),
            text="Resume",
            manager=manager,
            container=self.m_Window,
        )
        self.m_ElementsCount += 1

        self.m_PauseButton = pygame_gui.elements.UIButton(
            relative_rect=pygame.Rect(125, self.m_LineWidth * self.m_ElementsCount, 150, self.m_LineWidth),
            text="Pause",
            manager=manager,
            container=self.m_Window,
        )
        self.m_ElementsCount += 2

        self.m_SpeedSliderLabel = pygame_gui.elements.UILabel(
            relative_rect=pygame.Rect(0, self.m_LineWidth * self.m_ElementsCount, 125, self.m_LineWidth),
            text="Speed",
            manager=manager,
            container=self.m_Window,
        )

        self.m_SpeedSlider = pygame_gui.elements.UIHorizontalSlider(
            relative_rect=pygame.Rect(125, self.m_LineWidth * self.m_ElementsCount, 150, self.m_LineWidth),
            start_value=10000,
            value_range=(30, 10000),
            manager=manager,
            container=self.m_Window
        )

    def OnUpdate(self, dt: float)-> None:
        MoonSimulatorLayer.SetSimulationSpeed(self.m_SpeedSlider.get_current_value())

        self.m_DayLabel.set_text(f"Days: {GlobalClock.GetDays()}")

    def OnEvent(self, event: pygame.event.Event)-> None:
        if (event.type == pygame.USEREVENT):

            if (event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.m_ResumButton):
                MoonSimulatorLayer.ResumeSimulation()

            if (event.user_type == pygame_gui.UI_BUTTON_PRESSED and event.ui_element == self.m_PauseButton):
                MoonSimulatorLayer.PauseSimulation()

    def OnGuiRender(self, manager: pygame_gui.UIManager)-> None:
        manager.draw_ui(Engine.WindowToolKit.GetWindowSurface())

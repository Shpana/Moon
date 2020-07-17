import time
import pygame
import Engine

from .Layers.PygameLayer    import PygameLayer
from .Layers.PygameGuiLayer import PygameGuiLayer


class Application(object):

    def __init__(self, props: Engine.WindowProps)-> None:
        """ Initializes the application.
        |
        |-Since there must be only one instance of this
        | application in the program, its creation is moved to a separate ApplicationRegistry class
        """
        self.m_LayerStack = Engine.LayerStack()

        # Initializes the pygame module and sets some of its settings
        self.m_PygameLayer = PygameLayer()
        self.AddOverlay(self.m_PygameLayer)

        # Since creating a window requires a
        # previously initialized pygame, it is created after initializing pygame
        self.m_Window = Engine.Window(props)
        # Setting up a function that will handle all events
        self.m_Window.SetEventCallback(self.OnEvent_)

        # Since when UIManager is initialized
        # the window size is used, the window must be initialized first.
        self.m_PygameGuiLayer = PygameGuiLayer()
        self.AddOverlay(self.m_PygameGuiLayer)

        self.m_PreviousFrameTime = time.time()
        self.m_EventStack = Engine.Events.EventStack()
        self.m_Running = True
        self.m_Minimized = False
        
        Engine.Log.Info("Application was created successfully.")

    def __del__(self)-> None:
        """ Deinitializes the application
        |
        |-All layers in LayerStack will have the OnDetach
        | method was called, which is executed when the layer is detached or removed
        """
        for element in self.m_LayerStack.GetStack():
            element.OnDetach()

    def AddLayer(self, layer: Engine.Layer)-> None:
        """ Adds a layer.
        |
        |-Unlike overlay, the layer will be
        | called first and when it is added, the OnGuiAttach method is called
        """
        layer.OnAttach()
        layer.OnGuiAttach(self.m_PygameGuiLayer.GetManager())
        self.m_LayerStack.AddLayer(layer)

    def PopLayer(self, layer: Engine.Layer)-> None:
        """ Pops layer.
        |
        """
        layer.OnDetach()
        self.m_LayerStack.PopLayer(layer)

    def AddOverlay(self, layer: Engine.Layer)-> None:
        """ Adds a layer.
        |
        |-The overlay will update
        | after the layer and the OnGuiRender method will not be called
        """
        layer.OnAttach()
        self.m_LayerStack.AddOverlay(layer)

    def PopOverlay(self, layer: Engine.Layer)-> None:
        """ Pops overlay.
        |
        """
        layer.OnDetach()
        self.m_LayerStack.PopOverlay(layer)

    def Run(self)-> None:
        while (self.m_Running):
            self.m_Minimized = Engine.WindowToolKit.IsWindowMinimized()

            self.m_EventStack.PostEvent(Engine.Events.AppUpdateEvent(time.time() - self.m_PreviousFrameTime))
            self.m_EventStack.PostEvent(Engine.Events.AppGuiRenderEvent(self.m_PygameGuiLayer.GetManager()))

            self.m_PreviousFrameTime = time.time()
            self.m_Window.OnUpdate_()

    def OnEvent_(self, event: pygame.event.Event)-> None:
        dispatcher = Engine.Events.EventDispatcher(event)

        dispatcher.Dispatch(pygame.QUIT, self.OnWindowClose_)
        dispatcher.Dispatch(pygame.VIDEORESIZE, self.OnWindowResize_)

        for element in self.m_LayerStack.GetStack():
            element.OnEvent(event)

            if (event.type == Engine.Events.AppUpdateEvent.GetType()):
                element.OnUpdate(event.time)

            elif (event.type == Engine.Events.AppGuiRenderEvent.GetType()):
                element.OnGuiRender(event.manager)

    def OnWindowResize_(self, event: pygame.event.Event)-> None:
        self.m_Window.SetSize(event.w, event.h)
        self.m_PygameGuiLayer.GetManager().set_window_resolution((event.w, event.h))

    def OnWindowClose_(self, event: pygame.event.Event)-> None:
        self.m_Running = False

    def IsRunning(self)-> bool:
        return self.m_Running

    def IsMinimized(self)-> bool:
        return self.m_Minimized


class ApplicationRegistry(object):

    s_WasCreated: bool = False

    s_ApplicationInstance: Application = None

    @staticmethod
    def Create(props: Engine.WindowProps = Engine.WindowProps())-> Application:
        """ Creates a new application using the passed props parameter.
        |
        |-If you try to create two applications in one program,
        | then you will get an error saying that the Application has already been created.
        """

        Engine.Log.Assert(not ApplicationRegistry.WasCreated(), "The Application has already been created!")

        # Indicates that the application has already been created
        ApplicationRegistry.s_WasCreated = True
        ApplicationRegistry.s_ApplicationInstance = Application(props)

        return ApplicationRegistry.GetApplication()

    @staticmethod
    def GetApplication()-> Application:
        """ Returns the Application instance.
        |
        |-If the Application was not created before calling this function,
        | then the default Application is created, else it returns an instance of an existing Application.
        """
        if (not ApplicationRegistry.WasCreated()):
            return ApplicationRegistry.Create()

        return ApplicationRegistry.s_ApplicationInstance

    @staticmethod
    def WasCreated()-> bool:
        """ Returns whether an application instance was created.
        |
        |-If the application was created, then returns True, else False.
        """
        return ApplicationRegistry.s_WasCreated

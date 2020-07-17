import sys
sys.path.append("../../")
import Engine

from MoonSimulatorLayer import MoonSimulatorLayer

from MoonSimulatorGuiLayer import MoonSimulatorGuiLayer

app = Engine.ApplicationRegistry.Create(Engine.WindowProps("MoonSimulator", 1000, 700))
app.AddLayer(MoonSimulatorLayer())
app.AddLayer(MoonSimulatorGuiLayer())
app.Run()

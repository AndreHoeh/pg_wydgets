from MainMenueController import MainMenueController
from widgets.Container import Container
from widgets.Button import Button
from widget_config import button_config, container_config


class MainMenu:
    def __init__(self, scene) -> None:
        self.scene = scene
        self.controller = MainMenueController()
        self.container = Container(self.scene, 50, 50, 120, 250, container_config)
        b1 = Button(self.scene, 10, 10, 100, 50, button_config)
        b1.on_click = self.controller.t_on  # link a state machine trigger to this buttons on_click event
        b2 = Button(self.scene, 10, 65, 100, 50, button_config)
        self.container.add_widget("button2", b2)
        if (btn2 := self.container.elements["button2"]) is not None:
            btn2.on_click = self.controller.t_off
        self.container.add_widget("button1", b1)

    def update(self):
        self.container.update()

    def draw(self):
        self.container.draw()

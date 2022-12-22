from MainMenueController import MainMenueController
from widgets.Container import Container
from widgets.Button import Button
from widget_config import button_config, container_config


class MainMenu:
    def __init__(self, scene) -> None:
        self.scene = scene
        self.controller = MainMenueController()
        self.container = Container(self.scene, 50, 50, 230, 80, container_config)
        self._last_state = self.controller.state
        b1 = Button(self.scene, 10, 10, 100, 50, button_config)
        b1.on_click = self.controller.t_on  # link a state machine trigger to this buttons on_click event
        b1.text = "Activate"
        b2 = Button(self.scene, 120, 10, 100, 50, button_config)
        b2.text = "Deactivate"
        # add buttons to the container
        self.container.add_widget("button1", b1)
        self.container.add_widget("button2", b2)
        # access the button via the container
        self.container.elements["button2"].on_click = self.controller.t_off
        caption = Button(self.scene, 115, 68, 60, 30, button_config)
        self.container.add_widget("text_caption", caption)

    def update(self):
        if (state := self.controller.state) != self._last_state:
            self._last_state = state
            if state == "IDLE":
                self.container.hide()
                self.container.deactivate()
                self.container.elements["text_caption"].set_color_idle()
            elif state == "ACTIVE":
                self.container.activate()
                self.container.show()
                self.container.elements["text_caption"].set_color_active()
        self.container.update()

    def draw(self):
        self.container.draw()

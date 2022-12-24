from MainMenueController import MainMenueController
from widgets.Container import Container
from widgets.Button import Button
from widget_config import button_config


class MainMenu:
    def __init__(self, scene) -> None:
        self.scene = scene
        self.controller = MainMenueController()
        self.container = Container(50, 50, 230, 80)
        self._last_state = self.controller.state
        btn1 = Button(
            self.scene,
            x=0,
            y=self.container.rect.height // 2,
            w=self.container.rect.width // 2,
            h=self.container.rect.height // 2,
            config=button_config,
        )
        btn1.on_click = self.controller.t_on  # link a state machine trigger to this buttons on_click event
        btn1.text = "Activate"
        btn2 = Button(
            self.scene,
            x=self.container.rect.width // 2,
            y=self.container.rect.height // 2,
            w=self.container.rect.width // 2,
            h=self.container.rect.height // 2,
            config=button_config,
        )
        btn2.text = "Deactivate"
        btn2.on_click = self.controller.t_off
        # add buttons to the container
        self.container.add_widget("button1", btn1)
        self.container.add_widget("button2", btn2)
        # add another button, that is only used as a textbox
        caption = Button(
            self.scene,
            x=0,  # left of container
            y=0,  # top of container
            w=self.container.rect.width,
            h=self.container.rect.height // 2,
            config=button_config,
        )
        self.container.add_widget("text_caption", caption)

    def update(self):
        if (state := self.controller.state) != self._last_state:
            self._last_state = state
            if state == "IDLE":
                self.container.elements["text_caption"].set_color_idle()
            elif state == "ACTIVE":
                self.container.elements["text_caption"].set_color_active()
        self.container.update()

    def draw(self):
        self.container.draw()

from MainMenueController import MainMenueController

from widgets.Container import Container
from widgets.Container import GridContainer
from widgets.Button import Button
from widgets.TextBox import TextBox
from widget_config import button_config, textbox_config


class MainMenu:

    MARGIN = 3
    COLS = 3
    ROWS = 6

    def __init__(self, scene) -> None:
        self.scene = scene
        self.controller = MainMenueController()
        self.container = Container(50, 50, 230, 80)
        self._last_state = self.controller.state
        btn1 = Button(
            self.scene,
            x=0,
            y=self.container.rect.height // 2 + self.MARGIN,
            w=self.container.rect.width // 2,
            h=self.container.rect.height // 2,
            config=button_config,
        )
        # link a state machine trigger to this buttons on_release event
        btn1.on_release = self.controller.t_on
        btn1.text = "Activate"
        btn2 = Button(
            self.scene,
            x=self.container.rect.width // 2 + self.MARGIN,
            y=self.container.rect.height // 2 + self.MARGIN,
            w=self.container.rect.width // 2,
            h=self.container.rect.height // 2,
            config=button_config,
        )
        btn2.text = "Deactivate"
        btn2.on_release = self.controller.t_off
        # add buttons to the container
        self.container.add_widget("button1", btn1)
        self.container.add_widget("button2", btn2)
        caption = TextBox(
            self.scene,
            x=0,  # left of container, no offset
            y=0,  # top of container
            w=self.container.rect.width,
            h=self.container.rect.height // 2,
            config=textbox_config,
        )
        caption.text = 'Press "Activate"!'
        self.container.add_widget("text_caption", caption)
        self.setup_button_grid()

    def setup_button_grid(self):
        self.grid = GridContainer(
            x=50,
            y=150,
            w=150,
            h=150,
            cols=self.COLS,
            rows=self.ROWS,
            margin=self.MARGIN,
        )
        for r in range(self.ROWS):
            for c in range(self.COLS):
                btn = Button(self.scene, 0, 0, 0, 0, button_config)
                text = "btn" + str((r * self.grid.cols) + c)
                btn.text = text
                self.grid.add_widget(text, btn, c, r)

    def update(self):
        if (state := self.controller.state) != self._last_state:
            self._last_state = state
            if state == "IDLE":
                self.container.elements["text_caption"].set_color_idle()
                self.container.elements["text_caption"].text = "IDLE"
                self.container.elements["text_caption"].text_align_left(10)

            elif state == "ACTIVE":
                self.container.elements["text_caption"].set_color_active()
                self.container.elements["text_caption"].text = "ACTIVE"
                self.container.elements["text_caption"].text_align_right(10)
        self.container.update()
        self.grid.update()

    def draw(self):
        self.container.draw()
        self.grid.draw()

from widgets.Widget import Widget
from font.fonts import GameFonts as Fonts


class Button(Widget):
    def __init__(self, surface, x: float, y: float, width: float, height: float, config={}):
        super().__init__(surface, x, y, width, height, config)
        self.color_text_idle = config.get("color_text_idle", (50, 50, 50))
        self.color_text_active = config.get("color_text_active", (255, 20, 0))
        self._color_text = (0, 0, 0)  # ! add color based on state support
        self.font_size = config.get("font_size", 16)
        # self.font = pygame.font.SysFont("Consolas", self.font_size)
        self.text = config.get("text", None)

    def update(self):
        super().update()

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.render_text_img()

    def alignTextRect(self):
        self.text_rect.center = (self._rect.x + self._rect.width // 2, self._rect.y + self._rect.height // 2)

    def render_text_img(self):
        self.text_img = Fonts.shared.text_mono.render(self.text, False, self.color_text_idle)
        self.text_rect = self.text_img.get_rect()

    def draw(self):
        super().draw()
        if self.text:
            self.alignTextRect()
            self._surf.blit(self.text_img, self.text_rect)

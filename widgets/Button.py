from widgets.Widget import Widget
from font.fonts import GameFonts as Fonts


class Button(Widget):
    def __init__(self, surface, x: float, y: float, w: float, h: float, config={}):
        super().__init__(surface, x, y, w, h, config)
        self.color_fill_idle = config.get("color_fill_idle", (100, 0, 0))
        self.color_fill_hover = config.get("color_fill_hover", (0, 100, 0))
        self.color_fill_active = config.get("color_fill_active", (0, 0, 100))
        self.color_stroke_idle = config.get("color_stroke_idle", (100, 0, 0))
        self.color_stroke_hover = config.get("color_stroke_hover", (0, 100, 0))
        self.color_stroke_active = config.get("color_stroke_active", (0, 0, 100))
        self.color_text_idle = config.get("color_text_idle", (50, 50, 50))
        self.color_text_active = config.get("color_text_active", (255, 20, 0))
        self._color_text = self.color_text_idle
        self.text = config.get("text", "Hello")

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
        self.text_rect.center = (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)

    def render_text_img(self):
        self.text_img = Fonts.shared.text_mono.render(self.text, False, self._color_text)
        self.text_rect = self.text_img.get_rect()

    def draw(self):
        super().draw()
        if self.text:
            self.alignTextRect()
            self._surf.blit(self.text_img, self.text_rect)

    def set_color_idle(self):
        self.render_text_img()
        self._color_text = self.color_text_idle

    def set_color_active(self):
        self.render_text_img()
        self._color_text = self.color_text_active

    def handle_on_click(self):
        print("click")
        self._color_fill = self.color_fill_active
        self._color_stroke = self.color_stroke_active
        super().handle_on_click()

    def handle_on_release(self):
        print("release")
        self._color_fill = self.color_fill_idle
        self._color_stroke = self.color_stroke_idle
        super().handle_on_release()

    def handle_on_entry(self):
        print("entry")
        self._color_fill = self.color_fill_hover
        self._color_stroke = self.color_stroke_hover
        super().handle_on_entry()

    def handle_on_leave(self):
        print("leave")
        self._color_fill = self.color_fill_idle
        self._color_stroke = self.color_stroke_idle
        super().handle_on_leave()

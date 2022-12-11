import pygame
from widgets.Widget import Widget


class Button(Widget):
    def __init__(self, surface, x: float, y: float, width: float, height: float, config={}):
        super().__init__(surface, x, y, width, height, config)
        self.color_text_idle = config.get("color_text_idle", (50, 50, 50))
        self.color_text_active = config.get("color_text_active", (255, 20, 0))
        self._color_text = (0, 0, 0)  # ! add color based on state support
        self.font_size = config.get("font_size", 16)
        self.text = config.get("text", "Button")
        self.text_redraw = True
        self.font = pygame.font.SysFont("Calibri", self.font_size)
        if self.text:
            self.render_text_img()

    def update(self):
        super().update()

    def alignTextRect(self):
        self.text_rect.center = (self._rect.x + self._rect.width // 2, self._rect.y + self._rect.height // 2)

    def render_text_img(self):  # ! when do we do this?
        if self.text_redraw:
            self.text_img = self.font.render(self.text, False, self.color_text_idle)
            self.text_rect = self.text_img.get_rect()
            self.text_redraw = False

    def draw(self):
        super().draw()
        if self.text:
            self.alignTextRect()
            self._surf.blit(self.text_img, self.text_rect)

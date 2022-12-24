import pygame
from font.fonts import GameFonts as Fonts


from typing import Dict, Any, List, Tuple
from widgets.WidgetProtocol import WidgetProtocol


type_widget_config = Dict[str, Any]


class TextBox(WidgetProtocol):
    def __init__(self, surface, x: float, y: float, w: float, h: float, config: type_widget_config = {}):
        self._surf: pygame.Surface = surface
        self.rect = pygame.Rect((x, y), (w, h))
        self._hidden: bool = False
        self._active: bool = True
        self._pressed: bool = False
        self._hovered: bool = False
        self._scale: int = config.get("scale", 1)
        self.radius = config.get("radius", 10)
        self.color_fill_idle = config.get("color_fill_idle", (100, 0, 0))
        self.color_fill_hover = config.get("color_fill_hover", (0, 100, 0))
        self.color_fill_active = config.get("color_fill_active", (0, 0, 100))
        self.color_text_idle = config.get("color_text_idle", (50, 50, 50))
        self.color_text_hover = config.get("color_text_hover", (100, 100, 50))
        self.color_text_active = config.get("color_text_active", (200, 200, 0))
        self.color_stroke_idle = config.get("color_stroke_idle", (100, 0, 0))
        self.color_stroke_hover = config.get("color_stroke_hover", (0, 100, 0))
        self.color_stroke_active = config.get("color_stroke_active", (0, 0, 100))
        self._color_fill: Tuple[int, int, int] = self.color_fill_idle
        self._color_text: Tuple[int, int, int] = self.color_text_idle
        self._color_stroke: Tuple[int, int, int] = self.color_stroke_idle
        self.stroke_width = config.get("stroke_width", 1)
        self.text = config.get("text", "Text")

    def update(self):
        pass

    def draw(self):
        if self._hidden:
            return
        pygame.draw.rect(self._surf, self._color_fill, self.rect, border_radius=self.radius)
        if self._color_stroke:
            pygame.draw.rect(
                self._surf,
                self._color_stroke,
                self.rect,
                border_radius=self.radius,
                width=self.stroke_width,
            )
        if self.text:
            self.alignTextCenter()
            self._surf.blit(self.text_img, self.text_rect)

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, value):
        self._text = value
        self.render_text_img()

    def alignTextCenter(self):
        self.text_rect.center = (self.rect.x + self.rect.width // 2, self.rect.y + self.rect.height // 2)

    def render_text_img(self):
        self.text_img = Fonts.shared.text_mono.render(self.text, False, self._color_text)
        self.text_rect = self.text_img.get_rect()

    def set_color_idle(self):
        self._color_text = self.color_text_idle
        self._color_fill = self.color_fill_idle
        self._color_stroke = self.color_stroke_idle
        self.render_text_img()

    def set_color_active(self):
        self._color_text = self.color_text_active
        self._color_fill = self.color_fill_active
        self._color_stroke = self.color_stroke_active
        self.render_text_img()

    def set_color_hover(self):
        self._color_text = self.color_text_hover
        self._color_fill = self.color_fill_hover
        self._color_stroke = self.color_stroke_hover
        self.render_text_img()

    def hide(self):
        self._hidden = True

    def show(self):
        self._hidden = False

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

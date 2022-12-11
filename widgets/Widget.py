import pygame

from abc import abstractmethod, ABC
from typing import Dict, Any, List, Tuple

type_widget_config = Dict[str, Any]


class Widget(ABC):
    def __init__(self, surface, x: float, y: float, width: float, height: float, config: type_widget_config = {}):
        self._surf: pygame.Surface = surface
        self._rect = pygame.Rect((x, y), (width, height))
        self._hidden: bool = False
        self._active: bool = True
        self._pressed: bool = False
        self._color_fill: Tuple[int, int, int] = (0, 0, 0)
        self._color_stroke: Tuple[int, int, int] = (0, 0, 0)
        self._scale: int = config.get("scale", 1)
        self.radius = config.get("radius", 10)
        self.color_fill_idle = config.get("color_fill_idle", (100, 0, 0))
        self.color_fill_hover = config.get("color_fill_hover", (0, 100, 0))
        self.color_fill_active = config.get("color_fill_active", (0, 0, 100))
        self.color_stroke_idle = config.get("color_stroke_idle", (100, 0, 0))
        self.color_stroke_hover = config.get("color_stroke_hover", (0, 100, 0))
        self.color_stroke_active = config.get("color_stroke_active", (0, 0, 100))
        self.stroke_width = config.get("stroke_width", 1)
        self.on_click = None
        self.on_click_params = []
        self.on_release = None
        self.on_release_params = []

    def update(self):
        if not self._active:
            return
        left_click_pressed = pygame.mouse.get_pressed()[0]
        x, y = pygame.mouse.get_pos()
        if self.contains(x, y):
            if left_click_pressed:
                if not self._pressed:
                    self._pressed = True
                    self._color_fill = self.color_fill_active
                    self._color_stroke = self.color_stroke_active
                    self.handle_on_click()
                return
            elif self._pressed:
                self._pressed = False
                self.handle_on_release()
                return
            self._color_fill = self.color_fill_hover
            self._color_stroke = self.color_stroke_hover
            return

        if not left_click_pressed:
            self._pressed = False
            self._color_fill = self.color_fill_idle
            self._color_stroke = self.color_stroke_idle
            return

    def draw(self):
        if self._hidden:
            return
        pygame.draw.rect(self._surf, self._color_fill, self._rect, border_radius=self.radius)
        if self._color_stroke:
            pygame.draw.rect(
                self._surf,
                self._color_stroke,
                self._rect,
                border_radius=self.radius,
                width=self.stroke_width,
            )

    def handle_on_click(self):
        if self.on_click:
            self.on_click(*self.on_click_params)

    def handle_on_release(self):
        if self.on_release:
            self.on_release(*self.on_release_params)

    def contains(self, x, y):
        """# to compensate for a wrong mouse position when scaling the scene up"""
        x_scaled = x // self._scale
        y_scaled = y // self._scale
        return self._rect.collidepoint(x_scaled, y_scaled)

    def hide(self):
        self._hidden = True

    def show(self):
        self._hidden = False

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

    def move(self, x, y):
        self._rect = self._rect.move(x, y)

    def get_rect(self):
        return self._rect

    def get_x(self):
        return self._rect.x

    def get_y(self):
        return self._rect.y

    def get_center(self):
        return self._rect.center

    def get_width(self):
        return self._rect.width

    def get_height(self):
        return self._rect.height

    def set_pos(self, x=None, y=None):
        """Sets the new position.
        If one position is not given, the old position is used.
        """
        if x and y:
            self._rect.move_ip(x, y)
        elif not x and y:
            self._rect.move_ip(self._rect.x, y)
        elif not y and x:
            self._rect.move_ip(x, self._rect.y)

    def set_width(self, width):
        self._rect.width = width

    def set_height(self, height):
        self._rect.height = height

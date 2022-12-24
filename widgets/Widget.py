import pygame

from abc import abstractmethod, ABC
from typing import Dict, Any, List, Tuple

type_widget_config = Dict[str, Any]


class Widget(ABC):
    def __init__(self, surface, x: float, y: float, w: float, h: float, config: type_widget_config = {}):
        self._surf: pygame.Surface = surface
        self.rect = pygame.Rect((x, y), (w, h))
        self._hidden: bool = False
        self._active: bool = True
        self._pressed: bool = False
        self._hovered: bool = False
        self._scale: int = config.get("scale", 1)
        self.radius = config.get("radius", 10)
        self._color_fill: Tuple[int, int, int] = (150, 150, 140)
        self._color_stroke: Tuple[int, int, int] = (60, 60, 50)
        self.stroke_width = config.get("stroke_width", 1)
        self.on_click = None
        self.on_click_params = []
        self.on_release = None
        self.on_release_params = []
        self.on_entry = None
        self.on_entry_params = []
        self.on_leave = None
        self.on_leave_params = []

    def update(self):
        if not self._active:
            return
        left_click_pressed = pygame.mouse.get_pressed()[0]
        x, y = pygame.mouse.get_pos()
        if self.contains(x, y):
            if left_click_pressed:
                if not self._pressed:
                    self._pressed = True
                    self.handle_on_click()
                return
            elif self._pressed:
                self._pressed = False
                self.handle_on_release()
                return
            elif not self._hovered:
                self._hovered = True
                self.handle_on_entry()
            return

        if not left_click_pressed and self._hovered:
            self._hovered = False
            self._pressed = False
            self.handle_on_leave()
            return

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

    def handle_on_click(self):
        if self.on_click:
            self.on_click(*self.on_click_params)

    def handle_on_release(self):
        if self.on_release:
            self.on_release(*self.on_release_params)

    def handle_on_entry(self):
        if self.on_entry:
            self.on_entry(*self.on_entry_params)

    def handle_on_leave(self):
        if self.on_leave:
            self.on_leave(*self.on_leave_params)

    def contains(self, x, y):
        """# to compensate for a wrong mouse position when scaling the scene up"""
        x_scaled = x // self._scale
        y_scaled = y // self._scale
        return self.rect.collidepoint(x_scaled, y_scaled)

    def hide(self):
        self._hidden = True

    def show(self):
        self._hidden = False

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

import pygame
from widgets.TextBox import WidgetProtocol

from typing import Dict, Any


class Container(WidgetProtocol):
    def __init__(self, x: float, y: float, w: float, h: float):
        # super().__init__(surface, x, y, width, height, config)
        self.rect = pygame.Rect((x, y), (w, h))
        self.elements: Dict[str, Any] = {}
        self._hidden: bool = False
        self._active: bool = True

    def add_widget(self, widget_id, widget):
        widget.rect.update(self.rect.x + widget.rect.x, self.rect.y + widget.rect.y, widget.rect.w, widget.rect.h)
        self.elements[widget_id] = widget

    def update(self):
        if not self._active:
            return
        for w_id in self.elements.keys():
            self.elements[w_id].update()

    def draw(self):
        if self._hidden:
            return
        for w_id in self.elements.keys():
            self.elements[w_id].draw()

    def hide(self):
        self._hidden = True

    def show(self):
        self._hidden = False

    def activate(self):
        self._active = True

    def deactivate(self):
        self._active = False

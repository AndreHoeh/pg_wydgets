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

    def add_widget(self, widget_id: str, widget):
        widget.rect_update(self.rect.x + widget.rect.x, self.rect.y + widget.rect.y, widget.rect.w, widget.rect.h)
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


class GridContainer(Container):
    def __init__(self, x: float, y: float, w: float, h: float, cols: int, rows: int, margin: int):
        super().__init__(x, y, w, h)
        self.cols: int = cols
        self.rows: int = rows
        self.margin: int = margin

    def add_widget(self, widget_id: str, widget, col: int, row: int):
        """
        If widget width or heigth of the widget is 0 it is replaced with the grid element size.
        The element size depends on the size of the GridContainer and the number of collumns and rows.
        The widget position is used as an offset to the position in the grid.
        """
        x_offste = col * (self.rect.width // self.cols) + col * self.margin
        y_offste = row * (self.rect.height // self.rows) + row * self.margin
        width = widget.rect.w if widget.rect.w > 0 else self.rect.width // self.cols
        height = widget.rect.h if widget.rect.h > 0 else self.rect.height // self.rows

        widget.rect_update(
            self.rect.x + widget.rect.x + x_offste,
            self.rect.y + widget.rect.y + y_offste,
            width,
            height,
        )
        self.elements[widget_id] = widget

from widgets.Widget import Widget
from typing import List, Dict


class Container(Widget):
    def __init__(self, surface, x: float, y: float, width: float, height: float, config={}):
        super().__init__(surface, x, y, width, height, config)
        self.elements: Dict[str, Widget] = {}

    def add_widget(self, widget_id, widget):
        widget._rect.update(self._rect.x + widget._rect.x, self._rect.y + widget._rect.y, widget._rect.w, widget._rect.h)
        self.elements[widget_id] = widget

    def update(self):
        if self._active:
            super().update()
        for w_id in self.elements.keys():
            self.elements[w_id].update()

    def draw(self):
        if not self._hidden:
            super().draw()
        for w_id in self.elements.keys():
            self.elements[w_id].draw()

    def hide_all_elements(self):
        for w_id in self.elements.keys():
            self.elements[w_id].hide()

    def show_all_elements(self):
        for w_id in self.elements.keys():
            self.elements[w_id].show()

    def activate_all_elements(self):
        for w_id in self.elements.keys():
            self.elements[w_id].activate()

    def deactivate_all_elements(self):
        for w_id in self.elements.keys():
            self.elements[w_id].deactivate()
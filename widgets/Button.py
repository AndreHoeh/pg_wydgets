import pygame
from widgets.TextBox import TextBox


class Button(TextBox):
    def __init__(self, surface, x: float, y: float, w: float, h: float, config={}):
        super().__init__(surface, x, y, w, h, config)
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

    def handle_on_click(self):
        print("click")
        self._color_fill = self.color_fill_active
        self._color_stroke = self.color_stroke_active
        if self.on_click:
            self.on_click(*self.on_click_params)

    def handle_on_release(self):
        print("release")
        self._color_fill = self.color_fill_idle
        self._color_stroke = self.color_stroke_idle
        if self.on_release:
            self.on_release(*self.on_release_params)

    def handle_on_entry(self):
        print("entry")
        self._color_fill = self.color_fill_hover
        self._color_stroke = self.color_stroke_hover
        if self.on_entry:
            self.on_entry(*self.on_entry_params)

    def handle_on_leave(self):
        print("leave")
        self._color_fill = self.color_fill_idle
        self._color_stroke = self.color_stroke_idle
        if self.on_leave:
            self.on_leave(*self.on_leave_params)

    def contains(self, x, y):
        """# to compensate for a wrong mouse position when scaling the scene up"""
        x_scaled = x // self._scale
        y_scaled = y // self._scale
        return self.rect.collidepoint(x_scaled, y_scaled)

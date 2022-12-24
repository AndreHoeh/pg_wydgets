from typing import Protocol


class WidgetProtocol(Protocol):
    def update(self) -> None:
        """widgets need to be updated"""

    def draw(self) -> None:
        """widgets need to be drawn"""

    def hide(self):
        """Hide the widget"""

    def show(self):
        """Show the widget"""

    def activate(self):
        """Activate the widget"""

    def deactivate(self):
        """Deactivate the widget"""

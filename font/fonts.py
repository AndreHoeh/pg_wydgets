import pygame


class GameFonts:
    __slots__ = "text_mono"

    shared: "GameFonts" = None  # type: ignore

    def __init__(self, path: str) -> None:
        self.text_mono = pygame.font.Font(f"{path}/font/JetBrains_Mono/JetBrainsMono-Thin.ttf", 12)

    @classmethod
    def setup(cls, path: str):
        """
        Creates the shared instance
        """
        cls.shared = GameFonts(path)

    @classmethod
    def get_shared(cls):
        return cls.shared

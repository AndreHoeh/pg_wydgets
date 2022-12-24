import pygame
import os
from MainMenue import MainMenu
from font.fonts import GameFonts


# * add 'simple' state machine as controller
# * widget pos is relative to container pos
# * add a function to add a widget to a container
# * add text
# * add callbacks
# ? put click inside outside check into widget
# ? what is best way for callback stuff on_click etc.?

# ! add GridContainer
# ! remove visuals from container


class App:
    def __init__(self):
        self.res = self.width, self.height = (640, 360)
        self.scene = pygame.display.set_mode(self.res, pygame.SCALED)
        self.clock = pygame.time.Clock()
        self.running = True
        self.events = []
        self.main_menue = MainMenu(self.scene)

    def update(self):
        self.main_menue.update()

    def draw(self):
        self.scene.fill((210, 200, 150))
        self.main_menue.draw()
        pygame.display.flip()

    def run(self):
        while self.running:
            self.events = pygame.event.get()
            self.handle_basic_events()
            self.update()
            self.draw()
            self.clock.tick(144)
            pygame.display.set_caption(f"FPS: {self.clock.get_fps():.0f}")

    def handle_basic_events(self):
        for event in self.events:
            if event.type == pygame.QUIT:
                self.running = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                elif event.key == pygame.K_F11:
                    pygame.display.toggle_fullscreen()


if __name__ == "__main__":
    pygame.init()
    path = os.path.dirname(__file__)
    # * SETUP FONTS
    GameFonts.setup(path=path)
    fonts = GameFonts.get_shared()
    # * SETUP GAME
    os.environ["SDL_VIDEO_CENTERED"] = "1"  # center window
    os.environ["pg_BLEND_ALPHA_SDL2 "] = "1"  # faster blitting when using SDL2
    app = App()
    app.run()

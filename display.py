import sdl2
import sdl2.ext


class Display:
    def __init__(self, WIDTH, HEIGHT):
        sdl2.ext.init()

        self.WIDTH = WIDTH
        self.HEIGHT = HEIGHT

        self.window = sdl2.ext.Window("SLAM App", size=(self.WIDTH, self.HEIGHT), position=(0, 0))
        self.window.show()

    def paint(self, img):
        # junk
        events = sdl2.ext.get_events()
        for event in events:
            if event.type == sdl2.SDL_QUIT:
                exit(0)

        # draw
        surf = sdl2.ext.pixels3d(self.window.get_surface())
        surf[:, :, 0:3] = img.swapaxes(0, 1)

        # blit
        self.window.refresh()

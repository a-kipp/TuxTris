import pygame as pg


class Display:
    def __init__(self):
        from tetris import config
        self.config = config
        # game ground
        self.config.pictures = []
        for n in range(1, 8):
            try:
                self.config.pictures.append(
                    pg.transform.scale(pg.image.load("res/tetrisblock_%d.gif" % n),
                                       (self.config.blocksize, self.config.blocksize)))
            except FileNotFoundError as e:
                print(e.errno)

        # show screen
        pg.init()
        self.screen = pg.display.set_mode([self.config.width, self.config.height])
        self.screen.fill((0, 0, 0))

    def run(self):
        for n, color in enumerate(self.config.grid):  # from 0 to 199
            if color > 0:
                x = n % self.config.columns * self.config.distance
                y = n // self.config.columns * self.config.distance
                self.screen.blit(self.config.pictures[color], (x, y))
        pg.display.flip()

    def getEvents(self):
        return pg.event.get()

    def getPgQuitEvent(self):
        return pg.QUIT

    def quit(self):
        pg.quit()
        # todo: find a way to quit in a proper way
        exit(0)

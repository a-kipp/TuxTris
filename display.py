from asciiRender import ASCIIRender


class Display:
    def __init__(self, config):
        self.config = config
        if config.is_console_mode:
            self.ASCIIRender = ASCIIRender(config)

            # show bash
        else:
            pass
            # pygameGui

        # game ground

    def run(self):
        self.ASCIIRender.run()

    def updateGrid(self, grid):
        self.ASCIIRender.updateGrid(grid)

    def getEvents(self):
        pass

    def getPgQuitEvent(self):
        pass

    def quit(self):
        self.ASCIIRender.quit()

        pass

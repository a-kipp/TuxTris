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
        if self.config.is_console_mode:
            self.ASCIIRender.run()

    def updateGrid(self, grid):
        if self.config.is_console_mode:
            self.ASCIIRender.updateGrid(grid)

    def updateScore(self, score):
        if self.config.is_console_mode:
            self.ASCIIRender.updateScore(score)

    def set_game_ended(self, has_ended):
        if self.config.is_console_mode:
            self.ASCIIRender.setGameEnded(has_ended)

    def getEvents(self):
        pass

    def getPgQuitEvent(self):
        pass

    def get_input_key(self):
        if self.config.is_console_mode:
            return self.ASCIIRender.input_key

    def quit(self):
        self.ASCIIRender.quit()

        pass

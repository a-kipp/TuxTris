from asciiRender import ASCIIRender


class Display:
    def __init__(self, config):
        self.config = config
        if config.is_console_mode:
            self.ASCIIRender = ASCIIRender(config)
        else:
            pass

    def run(self):
        if self.config.is_console_mode:
            self.ASCIIRender.run()

    def update_grid(self, grid):
        if self.config.is_console_mode:
            self.ASCIIRender.update_grid(grid)

    def update_score(self, score):
        if self.config.is_console_mode:
            self.ASCIIRender.update_score(score)

    def set_game_ended(self, has_ended):
        if self.config.is_console_mode:
            self.ASCIIRender.setGameEnded(has_ended)

    def get_input_key(self):
        if self.config.is_console_mode:
            return self.ASCIIRender.input_key

    def quit(self):
        if self.config.is_console_mode:
            self.ASCIIRender.quit()
        else:
            pass

from asciiRender import ASCIIRender
class Display:
    def __init__(self):
        from tetris import config
        self.config = config
        if config.is_console_mode:
            self.ASCIIRender = ASCIIRender()


            #show bash
        else:
            pass
            #pygameGui

        # game ground

    def run(self):
        self.ASCIIRender.run()

    def getEvents(self):
        pass

    def getPgQuitEvent(self):
        pass

    def quit(self):
        pass
import signal
import time

from config import Config
from display import Display
from gameLogic import GameLogic


class Tetris:
    def __init__(self):
        signal.signal(signal.SIGINT, self.signal_handler)  # ^C
        signal.signal(signal.SIGTERM, self.signal_handler)  # process termination

        self.config = Config()
        self.display = Display(self.config)
        self.game_logic = GameLogic(self.config)
        self.goOn = True

    def run(self):
        self.display.run()

        while self.goOn:
            time_A = time.time()

            self.display.updateGrid(self.game_logic.do_logic(self.display.get_input_key()))

            time_B = time.time()
            time.sleep(self.config.refresh_rate - (time_B - time_A))
        self.display.quit()

    def signal_handler(self, sig, frame):
        """A custom signal handler to stop the game"""

        print("Got Signal: %s " % sig)

        if sig == signal.SIGINT or sig == signal.SIGTERM:
            self.goOn = False


if __name__ == "__main__":
    Tetris().run()

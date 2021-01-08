import signal
import time
import traceback

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

            input_key = self.display.get_input_key()
            if input_key == 113:
                # quit
                self.goOn = False

            try:
                self.display.updateGrid(self.game_logic.do_logic(input_key))
            except Exception as e:
                if str(e).strip() == "Initial collision":
                    self.goOn = False
                else:
                    traceback.print_exc()

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

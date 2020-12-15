import random
import copy
from figure import Figure


class GameLogic:

    def __init__(self, config):
        self.config = config
        self.tetromino = None

    def getUpdatingTestingGrid(self):
        self.config.grid[random.randint(0, self.config.line - 1)][random.randint(0, self.config.columns - 1)] = "X"
        return self.config.grid

    def do_logic(self, input_key):
        if self.tetromino is None or self.tetromino.is_dead:
            self.tetromino = Figure(self.config.columns, self.config.line, self.config)
        else:
            if input_key == 100:
                self.tetromino.move_right()
            if input_key == 97:
                self.tetromino.move_left()
            if input_key == 115:
                self.tetromino.move_to_bottom()
            if input_key == 119:
                self.tetromino.rotate_right()
            self.tetromino.move_step_down()

        return self.tetromino.draw(copy.deepcopy(self.config.grid))

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
        if self.tetromino is None or self.tetromino.destroy_me:
            self.tetromino = Figure(self.config.columns, self.config.line, self.config)
        else:
            if input_key == 97:
                # move left
                self.tetromino.move_x()
            if input_key == 100:
                # move right
                self.tetromino.move_x(False)
            if input_key == 119:
                # rotate
                self.tetromino.rotate_right()
            self.tetromino.move_y()

        return self.tetromino.draw(copy.deepcopy(self.config.grid))

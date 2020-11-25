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

    def do_logic(self):
        if self.tetromino is None:
            self.tetromino = Figure(self.config.columns, self.config.line)
        else:
            self.tetromino.move_y()
        return self.tetromino.draw(copy.deepcopy(self.config.grid))
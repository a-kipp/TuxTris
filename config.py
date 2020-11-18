class Config:
    def __init__(self):
        # todo: do stuff with params
        self.width = 400
        self.columns = 10
        self.line = 20
        self.blocksize = 40
        self.distance = self.width // self.columns
        self.height = self.distance * self.columns
        self.grid = [0] * self.columns * self.line

        # add test colours
        self.grid[5] = 2
        self.grid[6] = 3

class ASCIIRender:
    def __init__(self):
        from tetris import config
        self.config = config

    def run(self):
        self.config.grid[1][3] = "1"
        for line in self.config.grid:
            for block in line:
                print("[%s]" % block, end='')
            print("")




# falls belegt(1..7)[1||...7]
# self.config.grid[1][3] = "1"

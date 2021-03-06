class Config:
    def __init__(self):
        # todo: do stuff with params
        self.width = 400
        self.columns = 10
        self.line = 20
        self.blocksize = 40
        self.distance = self.width // self.columns
        self.height = self.distance * self.columns
        self.grid = [[" " for _ in range(self.columns)] for _ in range(self.line)]
        self.is_console_mode = True
        self.falling_rate = 0.3
        self.refresh_rate = 0.014  # PC-Masterrace

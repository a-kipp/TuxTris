import random


class Figure:
    # (x, y)
    figures = {
        1: [(0, 0), (0, 1), (1, 1), (2, 1)],
        2: [(0, 1), (1, 1), (2, 0), (2, 1)],
        3: [(0, 0), (1, 0), (1, 1), (2, 1)],
        4: [(0, 1), (1, 0), (1, 1), (2, 0)],
        5: [(0, 1), (1, 0), (1, 1), (2, 1)],
        6: [(0, 0), (0, 1), (1, 0), (1, 1)],
        7: [(0, 0), (0, 1), (0, 2), (0, 3)]
    }
    figure = None
    is_falling = None

    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        self.figure = self.figures[random.randint(1, len(self.figures))]
        self.figure_height = self.figure[len(self.figure) - 1][1] + 1
        self.figure_width = self.figure[len(self.figure) - 1][0] + 1
        self.y = 4
        self.x = 3
        # self.x = random.randint(0, max_x - len(self.figure[0]) - 1)
        is_falling = True

    def update_dimensions(self):
        self.figure_height = self.figure[len(self.figure) - 1][1] + 1
        self.figure_width = self.figure[len(self.figure) - 1][0] + 1

    def stop_falling(self):
        self.is_falling = False

    def move_y(self):
        if self.y < self.max_y - self.figure_height:
            self.y += 1

    def move_x(self, move_left=True):
        if move_left and self.x > 0:
            self.x -= 1
        elif not move_left and self.x < self.max_x - self.figure_width:
            self.x += 1

    def draw(self, grid):
        for pos in self.figure:
            grid[self.y + pos[1]][self.x + pos[0]] = "X"
        return grid

    def rotate_right(self):
        self.figure = [(self.figure[i][1], -self.figure[i][0]) for i in range(len(self.figure))]
        self.update_dimensions()

    def rotate_left(self):
        self.figure = [(-self.figure[i][1], self.figure[i][0]) for i in range(len(self.figure))]
        self.update_dimensions()

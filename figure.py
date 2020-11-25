import random


class Figure:
    # The lists of the individual figures must always have the same length
    # If in doubt, fill in with empty strings
    figures = {
        1: [["1", "", ""], ["1", "1", "1"]],
        2: [["", "", "2"], ["2", "2", "2"]],
        3: [["3", "3", ""], ["", "3", "3"]],
        4: [["", "4", "4"], ["4", "4", ""]],
        5: [["", "5", ""], ["5", "5", "5"]],
        6: [["6", "6"], ["6", "6"]],
        7: [["7"], ["7"], ["7"], ["7"]]
    }
    # (x, y)
    figure_positions = {
        1: [(0, 0), (0, 1), (1, 1), (2, 1)]
    }
    figure = None
    is_falling = None

    def __init__(self, max_x, max_y):
        self.max_x = max_x
        self.max_y = max_y
        # self.figure = self.figures[random.randint(1, len(self.figures))]
        self.figure_id = 1
        self.figure = self.figures[1]
        self.figure_height = self.figure_positions[self.figure_id][len(self.figure_positions[self.figure_id]) - 1][1] + 1
        self.y = 0
        self.x = 3
        # self.x = random.randint(0, max_x - len(self.figure[0]) - 1)
        is_falling = True

    def stop_falling(self):
        self.is_falling = False

    def move_y(self):
        if self.y < self.max_y - self.figure_height:
            self.y += 1

    def move_x(self):
        self.x += 1

    def draw(self, grid):
        for pos in self.figure_positions[self.figure_id]:
            grid[self.y + pos[1]][self.x + pos[0]] = "X"
        return grid

    def rotate_right(self, steps=1):
        """ Rotate a tetris figure
        steps can take positive and negative numbers
        The figure will be rotated "steps"-times with 90deg (right)
        """

        figure = self.figure
        for i in range(0, steps % 4):
            new_figure_list = []
            for row_index, row in enumerate(figure):
                for column_index, column in enumerate(row):
                    if column_index >= len(new_figure_list):
                        new_figure_list.append([])
                    new_figure_list[column_index].append(column)

            figure = []
            for row2 in new_figure_list:
                row2.reverse()
                figure.append(row2)
        self.figure = figure

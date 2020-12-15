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

    def __init__(self, max_x, max_y, config):
        self.max_x = max_x
        self.max_y = max_y
        self.figure = self.figures[random.randint(1, len(self.figures))]
        self.figure_height = self.figure[len(self.figure) - 1][1] + 1
        self.figure_width = self.figure[len(self.figure) - 1][0] + 1
        self.config = config
        self.is_dead = False
        self.x = random.randint(0, max_x - self.figure_width)
        self.y = 0
        if self.is_colliding():
            quit()

    def update_dimensions(self):
        self.figure_height = self.figure[len(self.figure) - 1][1] + 1
        self.figure_width = self.figure[len(self.figure) - 1][0] + 1

    def destroy_me(self):
        self.y -= 1
        for block in self.figure:
            self.config.grid[self.y + block[1]][self.x + block[0]] = "X"
        self.is_dead = True

    def pushback_to_grid(self):
        """push the tetromino back to the grid if partially or fully outside of boundaries"""
        is_outside_boundaries = True
        while is_outside_boundaries:
            for block in self.figure:
                print("self.y: %d" % self.y)
                print("block: %d" % block[1])
                if self.x + block[0] < 0:
                    self.x += 1
                    continue
                if self.x + block[0] >= self.max_x:
                    self.x -= 1
                    continue
                if self.y + block[1] >= self.max_y:
                    self.y -= 1
                    continue
                is_outside_boundaries = False

    def is_colliding(self):
        """check for collision with settled tetrominos on the grid"""
        for block in self.figure:
            if self.config.grid[self.y + block[1]][self.x + block[0]] == "X":
                return True
        return False

    def move_step_down(self):
        self.pushback_to_grid()
        moved = self
        moved.y += 1
        for block in self.figure:
            if self.y + block[1] >= self.max_y:
                self.destroy_me()
                break
        if not self.is_dead:
            print("something")
            if moved.is_colliding():

                self.destroy_me()
            else:
                self = moved

    def move_to_bottom(self):
        while not self.is_dead:
            self.move_step_down()

    def move_right(self):
        moved = self
        moved.x += 1
        moved.pushback_to_grid()
        if not moved.is_colliding():
            self = moved

    def move_left(self):
        moved = self
        moved.x -= 1
        moved.pushback_to_grid()
        if not moved.is_colliding():
            self = moved

    def rotate_right(self):
        rotated = self
        rotated.figure = [(rotated.figure[i][1], -rotated.figure[i][0]) for i in range(len(rotated.figure))]
        rotated.pushback_to_grid()
        if not rotated.is_colliding():
            self = rotated

    def rotate_left(self):
        rotated = self
        rotated.figure = [(-rotated.figure[i][1], rotated.figure[i][0]) for i in range(len(rotated.figure))]
        rotated.pushback_to_grid()
        if not rotated.is_colliding():
            self = rotated

    def draw(self, grid):
        for pos in self.figure:
            grid[self.y + pos[1]][self.x + pos[0]] = "X"
        return grid

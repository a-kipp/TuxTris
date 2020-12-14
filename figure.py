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
        self.destroy_me = False
        self.x = random.randint(0, max_x - self.figure_width)
        self.y = 0
        # if tertominoe at "X" quit()
        if self.check_collision():
            quit()

    def update_dimensions(self):
        self.figure_height = self.figure[len(self.figure) - 1][1] + 1
        self.figure_width = self.figure[len(self.figure) - 1][0] + 1

    def check_collision(self):
        for block in self.figure:
            #if self.x + block[0] == -1 or self.x + block[0] == self.max_x + 1:
            #    return True
            if (self.y + block[1]) < len(self.config.grid) and (self.x + block[0]) < len(self.config.grid[self.y + block[1]]):
                if self.y + block[1] == self.max_y or self.config.grid[self.y + block[1]][self.x + block[0]] != " ":
                    # loop to move the figure up
                    #while
                    self.burnblablabla()
                    return True
            else:

                return True
        return False


    def wall_deflect(self):
        colli = True
        while colli:
            colli = False
            for block in self.figure:
                print("self.y: %d" % self.y)
                print("block: %d" % block[1])
                if self.x + block[0] < 0:
                    self.x += 1
                    colli = True
                if self.x + block[0] > self.max_x:
                    self.x -= 1
                    colli = True
                if self.y + block[1] < 0:
                    self.y += 1
                    colli = True


    def collison_detect(self):
        for block in self.figure:
            if self.config.grid[self.y + block[1]][self.x + block[0]] == "X":
                return True
        return False


    def move_y(self):
        moved = self
        moved.y += 1
        if moved.collison_detect():
            self.destroy_me = True
        elif moved.y > self.max_y:
            self.destroy_me = True
        else:
            self = moved


    def move_down(self):
        while True:
            self.move_y()


    def move_right(self):
        moved = self
        moved.x += 1
        moved.wall_deflect()
        if not moved.collison_detect():
            self = moved


    def move_left(self):
        moved = self
        moved.x -= 1
        moved.wall_deflect()
        if not moved.collison_detect():
            self = moved


    def draw(self, grid):
        for pos in self.figure:
            grid[self.y + pos[1]][self.x + pos[0]] = "X"
        return grid


    def rotate_right(self):
        rotated = self
        rotated.figure = [(self.figure[i][1], -self.figure[i][0]) for i in range(len(self.figure))]
        rotated.wall_deflect()
        if not rotated.collison_detect():
            self = rotated


    def rotate_left(self):
        rotated = self
        rotated.figure = [(-self.figure[i][1], self.figure[i][0]) for i in range(len(self.figure))]
        rotated.wall_deflect()
        if not rotated.collison_detect():
            self = rotated






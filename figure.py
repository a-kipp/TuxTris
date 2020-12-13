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

    def collision_deflect(self):
        # if figure outside grid move towards mid
        colli = True
        while colli:
            colli = False
            for block in self.figure:
                print("self.y: %d" % self.y)
                print("block: %d" % block[1])
                if self.x + block[0] == -1:
                    self.x += 1
                    colli = True
                if self.x + block[0] == self.max_x + 1:
                    self.x -= 1
                    colli = True
                #if self.y + block[1] == self.max_y:
                #    self.y += 1
                #    colli = True
                #if (self.y + block[1]) >= len(self.config.grid):
                #    print("x1")
                #    self.check_collision()
                #    colli = True
               # if (self.x + block[0]) >= len(self.config.grid[self.y + block[1]]):
                #    print("x2")
                #    self.y -= 1
                #    colli = True
                #if self.config.grid[self.y + block[1]][self.x + block[0]] != " ":
                #    print("x3")
                #   self.y -= 1
                #    colli = True

    def burnblablabla(self):
        for block in self.figure:
            self.config.grid[self.y + block[1]][self.x + block[0]] = "X"
        self.destroy_me = True

    def move_down(self):
        while not self.check_collision():
            self.y += 1
        self.check_collision()
        self.burnblablabla()

    def move_y(self):
        self.y += 1
        if self.check_collision():
            self.collision_deflect()
            self.burnblablabla()

    def move_x(self, move_left=True):
        if move_left and self.x > 0:
            self.x -= 1
            if self.check_collision():
                self.collision_deflect()
        elif not move_left and (self.x + self.figure_width) < self.max_x:
            self.x += 1
            if self.check_collision():
                self.collision_deflect()

    def draw(self, grid):
        for pos in self.figure:
            grid[self.y + pos[1]][self.x + pos[0]] = "X"
        return grid

    def rotate_right(self):
        self.figure = [(self.figure[i][1], -self.figure[i][0]) for i in range(len(self.figure))]
        self.collision_deflect()
        self.update_dimensions()

    def rotate_left(self):
        self.figure = [(-self.figure[i][1], self.figure[i][0]) for i in range(len(self.figure))]
        self.collision_deflect()
        self.update_dimensions()

import curses
import threading
import time


class ASCIIRender:
    input_key = None
    thread_draw = None
    thread_keylistener = None
    stdscr = None
    stop_threads = False

    def __init__(self, config):
        self.config = config

    def run(self):
        self.thread_draw = threading.Thread(target=curses.wrapper, args=(self.draw,))
        self.thread_draw.start()

        # sleep(1)
        # self.thread_keylistener = threading.Thread(target=self.listenInput, args=(self.stdscr,))
        # self.thread_keylistener.start()

        # curses.wrapper(self.draw)
        return
        # self.config.grid[1][3] = "1"
        # for line in self.config.grid:
        #    for block in line:
        #        print("[%s]" % block, end='')
        #    print("")

    def quit(self):
        self.stop_threads = True
        self.thread_draw.join()

    def listenInput(self, stdscr):
        self.input_key = stdscr.getch()

    def updateGrid(self, grid):
        self.config.grid = grid

    def draw(self, stdscr):
        self.stdscr = stdscr
        stdscr.nodelay(True)
        cursor_x = 0
        cursor_y = 0

        # Clear and refresh the screen for a blank canvas
        stdscr.clear()
        stdscr.refresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        # cursor_x = max(0, cursor_x)
        # cursor_x = min(width - 1, cursor_x)

        while not self.stop_threads:
            time_A = time.time()

            self.listenInput(stdscr)

            # for line in self.grid:
            #     for block in line:
            #         print("[%s]" % block, end='')
            #     print("")
            # continue

            # Initialization
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            free_lines_before_grid = 1

            # Declaration of strings
            title = "TuxTris - A TeamTux Game Project"[:width - 1]
            dimensions = "Width: {}, Height: {}".format(width, height)
            short_help = "Control: move left 'a', move right 'd', rotate 'w', move down 's'"
            command_prompt_text = "Type to control: " + str(self.input_key)

            # Turning on attributes for title
            stdscr.attron(curses.color_pair(2))
            stdscr.attron(curses.A_BOLD)

            # Rendering title
            stdscr.addstr(0, 0, title)

            # Turning off attributes for title
            stdscr.attroff(curses.color_pair(2))
            stdscr.attroff(curses.A_BOLD)

            for i, line in enumerate(self.config.grid):
                cursor_y = i + free_lines_before_grid + 1
                lineText = ""
                for block in line:
                    lineText = lineText + ("[%s]" % block)
                i = i + 1

                stdscr.addstr(cursor_y, 1, lineText)

            # Render short help text
            stdscr.addstr(cursor_y + 3, 0, short_help, curses.color_pair(1))

            # Render command prompt
            stdscr.addstr(cursor_y + 5, 0, command_prompt_text, curses.color_pair(3))

            # Render dimensions text
            stdscr.addstr(height - 1, 0, dimensions, curses.color_pair(1))

            stdscr.move(cursor_y + 5, len(command_prompt_text) + 1)

            # Define Framerate
            time_B = time.time()
            time.sleep(self.config.refresh_rate - (time_B - time_A))

            stdscr.addstr(1, 0, str(self.config.refresh_rate - (time_B - time_A)))

            # Refresh the screen
            stdscr.refresh()


# falls belegt(1..7)[1||...7]
# self.config.grid[1][3] = "1"

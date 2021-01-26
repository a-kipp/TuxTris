import copy
import curses
import threading
import time


class ASCIIRender:
    input_key = None
    thread_draw = None
    thread_keylistener = None
    stdscr = None
    stop_threads = False
    score = 0
    game_ended = False

    def __init__(self, config):
        self.config = copy.deepcopy(config)

    def run(self):
        self.thread_draw = threading.Thread(target=curses.wrapper, args=(self.draw,))
        self.thread_draw.start()

        return

    def quit(self):
        self.stop_threads = True
        self.thread_draw.join()

    def listenInput(self, stdscr):
        self.input_key = stdscr.getch()

    def updateGrid(self, grid):
        self.config.grid = grid

    def updateScore(self, score):
        self.score = score

    def setGameEnded(self, has_ended):
        self.game_ended = has_ended

    def draw(self, stdscr):
        self.stdscr = stdscr
        stdscr.nodelay(True)
        cursor_y = 0

        # Clear and refresh the screen for a blank canvas
        stdscr.clear()
        stdscr.refresh()

        # Start colors in curses
        curses.start_color()
        curses.init_pair(1, curses.COLOR_CYAN, curses.COLOR_BLACK)
        curses.init_pair(2, curses.COLOR_RED, curses.COLOR_BLACK)
        curses.init_pair(3, curses.COLOR_BLACK, curses.COLOR_WHITE)

        while not self.stop_threads:
            time_A = time.time()

            self.listenInput(stdscr)

            # Initialization
            stdscr.clear()
            height, width = stdscr.getmaxyx()
            free_lines_before_grid = 1

            # Declaration of strings
            title = "TuxTris - A TeamTux Game Project"[:width - 1]
            dimensions = "Width: {}, Height: {}".format(width, height)
            short_help = "Control: move left 'a', move right 'd', rotate 'w', move down 's', quit 'q'"
            command_prompt_text = "Your score: %d" % self.score
            game_ended_text = "Game ended! - " + command_prompt_text
            window_too_small_text = "Window to small, at least 27 lines required!"

            # Turning on attributes for title
            stdscr.attron(curses.color_pair(2))
            stdscr.attron(curses.A_BOLD)

            # Rendering title
            stdscr.addstr(0, 0, title)

            # Turning off attributes for title
            stdscr.attroff(curses.color_pair(2))
            stdscr.attroff(curses.A_BOLD)

            if height >= 27:
                try:
                    if self.game_ended:
                        stdscr.addstr(free_lines_before_grid + 10, 0, game_ended_text, curses.color_pair(3))
                    else:
                        for i, line in enumerate(self.config.grid):
                            cursor_y = i + free_lines_before_grid + 1
                            lineText = ""
                            for block in line:
                                lineText = lineText + ("[%s]" % block)

                            stdscr.addstr(cursor_y, 1, lineText)

                    # Render short help text
                    stdscr.addstr(cursor_y + 3, 0, short_help, curses.color_pair(1))

                    # Render command prompt
                    stdscr.addstr(cursor_y + 5, 0, command_prompt_text, curses.color_pair(3))

                    # Render dimensions text (only for debugging)
                    # stdscr.addstr(height - 1, 0, dimensions, curses.color_pair(1))

                    stdscr.move(cursor_y + 5, len(command_prompt_text) + 1)
                except Exception as e:
                    if str(e).strip() == "_curses.error":
                        stdscr.addstr(1, 0, str(e).strip())
            else:
                stdscr.addstr(1, 0, window_too_small_text)

            # Define Framerate
            time_B = time.time()
            time.sleep(self.config.refresh_rate - (time_B - time_A))

            # Add refresh rate delay to the display (only for debugging)
            # stdscr.addstr(1, 0, str(self.config.refresh_rate - (time_B - time_A)))

            # Refresh the screen
            stdscr.refresh()

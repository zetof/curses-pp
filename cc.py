import curses

class CC:

  def __init__(self, window):
    self.window = window
    curses.curs_set(0)
    window_size = window.getmaxyx()
    self.max_col = window_size[0] - 1
    self.max_line = window_size[1] - 1



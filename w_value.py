import curses
from widget import Widget


class W_Value(Widget):

    def __init__(self, low, high, val, label, line, col):
        self._low = low
        self._high = high
        self._val = val
        self._selected = False
        super().__init__(label, line, col)

    def draw(self, window):
        window.addstr(self._line, self._col,
                      self._label[0], curses.color_pair(1))
        window.addstr(self._key, curses.color_pair(1) | curses.A_STANDOUT)
        window.addstr("{}: ".format(self._label[1]), curses.color_pair(1))
        window.addstr('-', curses.color_pair(2))
        window.addstr(" [ {} ] ".format(self._val),
                      curses.color_pair(3) | curses.A_BOLD)
        window.addstr('+', curses.color_pair(2))
        window.refresh()

    def send_key(self, key):
        if key == '+' and self._val < self._high:
            self._val += 1
            return True
        if key == '-' and self._val > self._low:
            self._val -= 1
            return True
        return False

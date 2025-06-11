import curses
from widget import Widget


class W_Value(Widget):

    def __init__(self, low, high, val, label, line, col):
        self._low = low
        self._high = high
        self._val = val
        super().__init__(label, line, col)

    def draw(self, window):
        window.addstr(self._line, self._col, self._label[0])
        window.addstr(self._key, curses.A_STANDOUT)
        window.addstr("{}: ".format(self._label[1]))
        window.addstr('-')
        window.addstr(" [ {} ] ".format(self._val))
        window.addstr('+')
        window.refresh()

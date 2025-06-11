import curses
from threading import Thread
from time import sleep
from w_value import W_Value


class CC(Thread):

    def __init__(self):
        self._widgets = []
        self._running = True
        self._delay = .1

    def _init_params(self, window):
        curses.curs_set(0)
        window_size = window.getmaxyx()
        window.nodelay(True)
        self.max_col = window_size[0] - 1
        self.max_line = window_size[1] - 1
        self._window = window
        self.draw_all()

    def run(self, window):
        self._init_params(window)
        while self._running:
            try:
                key = window.getkey()
                if str(key) == 'q':
                    self.stop()
                if self.select_widget(key):
                    self.stop()
            except Exception:
                pass
            sleep(self._delay)

    def start(self):
        Thread.__init__(self)
        curses.wrapper(self.run)

    def stop(self):
        self._running = False

    def set_theme(self, val_color, button_color, label_color):
        pass

    def add_w_value(self, low, high, val, label, col, line):
        self._widgets.append(W_Value(low, high, val, label, col, line))

    def draw_all(self):
        for widget in self._widgets:
            widget.draw(self._window)

    def select_widget(self, key):
        for widget in self._widgets:
            if widget.get_key() == key:
                return True
        return False

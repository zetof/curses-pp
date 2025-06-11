import curses
from enum import Enum
from threading import Thread
from time import sleep
from w_value import W_Value


class TC(Enum):
    LABEL = 1
    BUTTON = 2
    VAL = 3


class CC(Thread):

    def __init__(self, label_color=209, button_color=221, value_color=155):
        self._label_color = label_color
        self._button_color = button_color
        self._value_color = value_color
        self._widgets = []
        self._active_widget = None
        self._running = True
        self._delay = .1

    def _init_params(self, window):
        curses.curs_set(0)
        window_size = window.getmaxyx()
        window.nodelay(True)
        self.max_col = window_size[0] - 1
        self.max_line = window_size[1] - 1
        curses.init_pair(1, self._label_color, 0)
        curses.init_pair(2, self._button_color, 0)
        curses.init_pair(3, self._value_color, 0)
        self._window = window
        self.draw_all()

    def run(self, window):
        self._init_params(window)
        while self._running:
            try:
                key = str(window.getkey())
                if key == 'q':
                    self.stop()
                elif key in ['-', '+']:
                    self.send_key_to_widget(key)
                else:
                    self.select_widget(key)
            except Exception:
                pass
            sleep(self._delay)

    def start(self):
        Thread.__init__(self)
        curses.wrapper(self.run)

    def stop(self):
        self._running = False

    def add_w_value(self, low, high, val, label, col, line):
        self._widgets.append(W_Value(low, high, val, label, col, line))

    def draw_all(self):
        for widget in self._widgets:
            widget.draw(self._window)

    def select_widget(self, key):
        for widget in self._widgets:
            if widget.get_key() == key:
                self._active_widget = widget

    def send_key_to_widget(self, key):
        if self._active_widget.send_key(key):
            self._active_widget.draw(self._window)

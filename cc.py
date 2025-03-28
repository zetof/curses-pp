import curses
from threading import Thread
from time import sleep


class CC(Thread):

    def __init__(self):
        self._running = True
        self._delay = .001
        Thread.__init__(self)
        curses.wrapper(self.run)

    def _init_params(self, window):
        curses.curs_set(0)
        window_size = window.getmaxyx()
        window.nodelay(True)
        self.max_col = window_size[0] - 1
        self.max_line = window_size[1] - 1

    def run(self, window):
        self._init_params(window)
        while self._running:
            try:
                key = window.getkey()
                if str(key) == 'q':
                    self.stop()
            except Exception:
                pass
            sleep(self._delay)

    def stop(self):
        self._running = False

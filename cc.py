import curses
from threading import Thread
from time import sleep


class CC(Thread):

    def __init__(self, window):
        self._running = True
        self._delay = .001
        self._window = window
        curses.curs_set(False)
        window_size = window.getmaxyx()
        window.nodelay(True)
        self.max_col = window_size[0] - 1
        self.max_line = window_size[1] - 1
        Thread.__init__(self)

    def run(self):
        while self._running:
            try:
                key = self._window.getkey()
                if str(key) == 'q':
                    self.stop()
            except Exception as e:
                pass
            sleep(self._delay)

    def stop(self):
        self._running = False

    def is_running(self):
        return self._running

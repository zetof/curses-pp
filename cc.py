import curses
from threading import Thread
from time import sleep


class CC(Thread):

    def __init__(self):
        self._running = True
        self._delay = .001
        Thread.__init__(self)
        curses.wrapper(self.run)

    def run(self, window):
        print(window)
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

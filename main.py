import curses
from cc import CC


def main(window):
    cc = CC(window)
    cc.start()
    cc.join()


if __name__ == "__main__":
    curses.wrapper(main)

import curses
from cc import CC

def main(window):
  cc = CC(window)
  #curses.init_pair(1, curses.COLOR_BLACK, curses.COLOR_WHITE)
  #app.attron(curses.A_UNDERLINE)
  #app.attron(curses.color_pair(1))
  #app.addstr(1, 1, "TEST")
  window.getkey()

if __name__ == "__main__":
  curses.wrapper(main)

import animate
import ascii_art
import curses
import time
 
#animate.rain_effect(ascii.gambit_header)

def main():
    stdscr = curses.initscr()
    curses.noecho()
    curses.cbreak()
    stdscr.keypad(True)
    stdscr.addstr(0,0, "Gambit")
    stdscr.refresh()

if __name__ == "__main__":
    main()


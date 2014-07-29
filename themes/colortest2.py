#!/usr/bin/env python
import sys

ESCAPE = chr(27)

def fg(color):
    return ESCAPE + '[38;5;{0}m'.format(color)

def bg(color):
    return ESCAPE + '[48;5;{0}m'.format(color)

def reset():
    return ESCAPE + '[48;0m'

if __name__ == "__main__":
    if len(sys.argv) < 4:
        print 'Usage: colortest.py fg bg test_string'
        sys.exit(1)

    _fg = eval(sys.argv[1])
    _bg = eval(sys.argv[2])
    #fg, bg = map(int, sys.argv[1:3])
    test_string = sys.argv[3]

    #print ' ' * len(str(bg_start)),
    for fg_color in _fg:
        print ' ' * (len(test_string) - len(str(fg_color))), fg_color,
    print

    for bg_color in _bg:
        print bg_color, bg(bg_color),
        for fg_color in _fg:
            print fg(fg_color), test_string,
        print reset()

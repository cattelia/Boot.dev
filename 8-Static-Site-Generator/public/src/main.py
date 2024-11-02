#!/bin/sh
# ./main.sh || https://stackoverflow.com/questions/4377109/shell-script-execute-a-python-program-from-within-a-shell-script

from textnode import *


def main():

    t = TextNode("This is a text node", "BOLD", "https://www.boot.dev")
    #print(t.text, t.text_type, t.url)
    print(t) # Testing: __repr__()

    s = TextNode("welcome", "italic")
    #print(s.text, s.text_type, s.url)
    print(s) # Testing: __repr__()

main()

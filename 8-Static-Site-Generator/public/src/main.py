#!/bin/sh
# ./main.sh || https://stackoverflow.com/questions/4377109/shell-script-execute-a-python-program-from-within-a-shell-script

from textnode import *


def main():
    node = TextNode("This is a text node", TextType.BOLD, "https://www.boot.dev")
    print(node)


main()

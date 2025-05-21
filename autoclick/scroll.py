import sys

import dotool


def scroll_down():
    dotool.wheel("+4")


def scroll_up():
    dotool.wheel("-4")


def main():
    if __name__ == "__main__":
        if len(sys.argv) > 1:
            if sys.argv[1] == "down":
                scroll_down()
            elif sys.argv[1] == "up":
                scroll_up()


if __name__ == "__main__":
    main()

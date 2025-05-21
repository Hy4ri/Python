import time

import dotool


def thunar():
    dotool.key("super+1")
    dotool.mouseto("0 0")
    time.sleep(2)
    dotool.mousemove("100 109")
    time.sleep(1)
    dotool.click("right")


def test():
    dotool.mouseto("0 0")
    time.sleep(1)
    dotool.mousemove("0 19")


def main():
    thunar()
    # test()


if __name__ == "__main__":
    main()

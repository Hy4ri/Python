import subprocess


def key(key):
    command = subprocess.Popen(["echo", "key", key], stdout=subprocess.PIPE, text=True)
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def keydown(key):
    command = subprocess.Popen(
        ["echo", "keydown", key], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def keyup(key):
    command = subprocess.Popen(
        ["echo", "keyup", key], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def type0(text):
    command = subprocess.Popen(
        ["echo", "type", text], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def click(button):
    command = subprocess.Popen(
        ["echo", "click", button], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def buttondown(button):
    command = subprocess.Popen(
        ["echo", "buttondown", button], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def buttonup(button):
    command = subprocess.Popen(
        ["echo", "buttonup", button], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def wheel(amount):
    command = subprocess.Popen(
        ["echo", "wheel", amount], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def hwheel(amount):
    command = subprocess.Popen(
        ["echo", "hwheel", amount], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def mouseto(cord):
    command = subprocess.Popen(
        ["echo", "mouseto", cord], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def mousemove(cord):
    command = subprocess.Popen(
        ["echo", "mousemove", cord], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def keydelay(ms):
    command = subprocess.Popen(
        ["echo", "keydelay", ms], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def keyhold(ms):
    command = subprocess.Popen(
        ["echo", "keyhold", ms], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def typedelay(ms):
    command = subprocess.Popen(
        ["echo", "typedelay", ms], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def typehold(ms):
    command = subprocess.Popen(
        ["echo", "typehold", ms], stdout=subprocess.PIPE, text=True
    )
    subprocess.Popen(
        ["dotool"], stdin=command.stdout, stdout=subprocess.PIPE, text=True
    )


def main():
    print("key: Simulates pressing and releasing a key")
    print("keydown: Simulates pressing a key down")
    print("keyup: Simulates releasing a key")
    print("type0: Types the specified text")
    print("click: Simulates a mouse button click")
    print("buttondown: Simulates pressing a mouse button down")
    print("buttonup: Simulates releasing a mouse button")
    print("wheel: Simulates vertical mouse wheel movement")
    print("hwheel: Simulates horizontal mouse wheel movement")
    print("mouseto: Moves the mouse to the specified coordinates")
    print("mousemove: Moves the mouse relative to current position")
    print("keydelay: Sets delay between key events in milliseconds")
    print("keyhold: Sets duration to hold a key in milliseconds")
    print("typedelay: Sets delay between typed characters in milliseconds")
    print("typehold: Sets duration to hold typed characters in milliseconds")


if __name__ == "__main__":
    main()

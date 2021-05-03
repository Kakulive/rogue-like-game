import sys
import os

def key_pressed():
    try:
        import tty, termios
    except ImportError:
        try:
            # probably Windows
            import msvcrt
        except ImportError:
            # FIXME what to do on other platforms?
            raise ImportError('getch not available')
        else:
            key = msvcrt.getch().decode('utf-8')
            return key
    else:
        fd = sys.stdin.fileno()
        old_settings = termios.tcgetattr(fd)
        try:
            tty.setraw(fd)
            ch = sys.stdin.read(1)
        finally:
            termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
        return ch

def clear_screen():
    if os.name == "nt":
        os.system('cls')
    else:
        os.system('clear')

def read_from_file(filename, color, separator=":"):
    with open(filename, 'r' ) as file:
        lines = file.readlines()
        new_list = []
        for element in lines:
            element_list = element.replace("\n", "").split(separator)
            element_list[0] = f"{color}{element_list[0]}\u001b[37m"
            new_list.append(element_list)
    return new_list
import time
import os
import sys
import platform

#os specifc imports
if platform.system() == "Windows":
    import winsound
    import msvcrt
else:
    import select
    import termios
    import tty

def beep(pitch):
    if platform.system() == "Windows":
        winsound.Beep(pitch, 150)
    else:
        print('\a', end='', flush=True)

def key_pressed():
    if platform.system() == "Windows":
        return msvcrt.kbhit() and msvcrt.getch() == b'\r'
    else:
        dr, _, _ = select.select([sys.stdin], [], [], 0)
        if dr:
            return sys.stdin.read(1) == '\n'
        return False

#main menu
print("Python metronome by ep1c-boi! \nplease input your desired BPM.\n")
bpm = int(input("bpm= "))

#interval calcs
interval = 60 / bpm
beat = 0

if platform.system() != "Windows":
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    tty.setcbreak(fd)

#audio + visualizer
try:
    while True:
        line = "| " if beat % 4 == 0 else "> "
        pitch = 1600 if beat % 4 == 0 else 1000

        os.system('cls' if platform.system() == "Windows" else 'clear')
        print("Press Enter to end.")
        print(line)
        beep(pitch)

        time.sleep(interval)
        beat += 1

        if key_pressed():
            break
finally:
    if platform.system() != "Windows":
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
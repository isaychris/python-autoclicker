import pyautogui
from pynput.keyboard import *
from random import randrange

#  ======== Settings ========
delay = 60 # Static delay in seconds
rand_delay = 15 # Random range argument between 1 and the number, in seconds
resume_key = Key.f1
run_rand = Key.f2
pause_key = Key.f3
exit_key = Key.esc
#  ==========================

pause = True
running = True
rand_num = False

def on_press(key):
    global running, pause, rand_num

    if key == resume_key:
        pause = False
        rand_num = False
        print("[Resumed Static Delay]")
    elif key == run_rand:
        pause = False
        rand_num = True
        print("[Resumed Random Delay]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def display_controls():
    print("// AutoClicker by iSayChris. Additional Features by Derplime.")
    print("// - Settings: ")
    print("\t Static delay = " + str(delay) + " sec")
    print("\t Random delay = 1 to " + str(rand_delay) + " sec\n")
    print("// - Controls:")
    print("\t F1 = Resume Static Delay")
    print("\t F2 = Resume Random Delay")
    print("\t F3 = Pause")
    print("\t ESC = Exit")
    print("-----------------------------------------------------")
    print('Press F1 or F2 to start ...')


def main():
    lis = Listener(on_press=on_press)
    lis.start()

    display_controls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            if rand_num:
                pyautogui.PAUSE = randrange(1, rand_delay)
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()
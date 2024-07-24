import pyautogui
from pynput.keyboard import *

#  ======== settings ========
delay = 1  # in seconds
resume_key = Key.f1
pause_key = Key.f2
exit_key = Key.esc
#  ==========================

pause = True
running = True

def onPress(key):
    global running, pause

    if key == resume_key:
        pause = False
        print("[Resumed]")
    elif key == pause_key:
        pause = True
        print("[Paused]")
    elif key == exit_key:
        running = False
        print("[Exit]")


def displayControls():
    print("=====================================================")
    print("                 AutoClicker by iSayChris            ")
    print("              Personalized by SoyAlex2024            ")
    print("=====================================================")
    print("                       Settings                      ")
    print("-----------------------------------------------------")
    print(f" Delay: \t\t {delay} sec                       ")
    print("-----------------------------------------------------")
    print("                       Controls                      ")
    print("-----------------------------------------------------")
    print(" F1 \t= Resume                                       ")
    print(" F2 \t= Pause                                        ")
    print(" F3 \t= Exit                                         ")
    print("-----------------------------------------------------")
    print('Press F1 to start ...')


def main():
    lis = Listener(onPress=onPress)
    lis.start()

    displayControls()
    while running:
        if not pause:
            pyautogui.click(pyautogui.position())
            pyautogui.PAUSE = delay
    lis.stop()


if __name__ == "__main__":
    main()

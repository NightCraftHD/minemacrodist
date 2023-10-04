import pygetwindow as gw
import time
import threading
import pyautogui
import re

from pynput import keyboard

lastkeynotback = True

stop = False


def run_instructions(instr):
    print(instr)
    global stop
    for s in instr:
        save_s = s
        if not lastkeynotback:
            break

        if stop:
            break

        if s.find("Forwards") == 0:
            match = re.search(r'-?\d+', s)
            number_str = match.group()
            number = float(number_str) if '.' in number_str else int(number_str)
            pyautogui.keyDown('w')
            for i in range(0, number):
                if stop:
                    break
                time.sleep(0.175)
            pyautogui.keyUp('w')

        if s.find("Backward") == 0:
            pyautogui.keyDown('s')
            for i in range(0, number):
                if stop:
                    break
                time.sleep(0.17)
            pyautogui.keyUp('s')

        if s.find("Right") == 0:
            pyautogui.keyDown('d')
            for i in range(0, number):
                if stop:
                    break
                time.sleep(0.17)
            pyautogui.keyUp('d')
            pyautogui.moveRel(200, 0, 1)

        if s.find("Left") == 0:
            pyautogui.keyDown('a')
            for i in range(0, number):
                if stop:
                    break
                time.sleep(0.17)
            pyautogui.keyUp('a')

        if s == "Short-Click":
            pyautogui.click()

        if s.find("Break for ") == 0:
            match = re.search(r'-?\d+', s)
            number_str = match.group()
            number = float(number_str) if '.' in number_str else int(number_str)
            pyautogui.mouseDown()
            time.sleep(number)
            pyautogui.mouseUp()

        if s == "Anti AFK":
            pyautogui.moveRel(100, 0, 0)
            pyautogui.moveRel(-100, 0, 0)

        if s.find("Eat") == 0:
            match = re.search(r'-?\d+', s)
            number_str = match.group()
            number = float(number_str) if '.' in number_str else int(number_str)
            pyautogui.press(str(number))
            pyautogui.mouseDown(button='right')
            time.sleep(2)
            pyautogui.mouseUp(button='right')

        if s.find("Wait") == 0:
            match = re.search(r'-?\d+', s)
            number_str = match.group()
            number = float(number_str) if '.' in number_str else int(number_str)
            for i in range(0, number):
                if stop:
                    break
                time.sleep(1)

        if s.find("Slot") == 0:
            match = re.search(r'-?\d+', s)
            number_str = match.group()
            number = float(number_str) if '.' in number_str else int(number_str)
            pyautogui.press(str(number))


def test_for_window(instr):
    instr.remove(instr[len(instr) - 1])
    global stop
    stop = False
    while lastkeynotback:
        correctWindow = False
        time.sleep(3)
        focused_window = gw.getWindowsWithTitle(gw.getActiveWindowTitle())

        if stop:
            break
        if focused_window[0].title.find("Lunar Client") != -1:
            print(focused_window[0].title + " ")
            correctWindow = True
        elif focused_window[0].title.find("Minecraft") != -1:
            print(focused_window[0].title + " ")
            correctWindow = True
        else:
            correctWindow = False

        if correctWindow:
            run_instructions(instr)


def on_keypress(key):
    try:
        print(f"Key pressed: {key.char}")
    except AttributeError:
        print(f"Special key pressed: {key}")
        if key == keyboard.Key.backspace:
            print("yay")
            global lastkeynotback
            lastkeynotback = False


def addListener():
    listener = keyboard.Listener(on_press=on_keypress)
    listener.start()
    global lastkeynotback
    while lastkeynotback:
        time.sleep(1)
    listener.stop()


def play(label):
    global lastkeynotback
    lastkeynotback = False
    global stop
    stop = True
    time.sleep(0.1)
    lastkeynotback = True
    instr = label.split("\n")
    instr.remove(instr[len(instr) - 1])
    threadTestWindow = threading.Thread(target=test_for_window, args=(instr,))
    threadTestWindow.start()
    threadListen = threading.Thread(target=addListener)
    threadListen.start()


def stopButton():
    global stop
    stop = True



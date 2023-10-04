import tkinter.filedialog
from tkinter import END, DISABLED
from pathlib import Path
import re
import pynput
import customtkinter
import tkinter as tk
import pygetwindow
import pyautogui
import time
import threading
import threading
import Play

root = None
instruct = ""
slider_val = 1
slider = None
globtype = ""


def addText(text):
    label.configure(state='normal')
    label.insert(END, text + "\n")
    label.configure(state='disabled')


def doneEdit(type):
    if type == "Eat":
        addText(type + " slot " + str(slider_val))
    else:
        addText(type + " " + str(slider_val))
    root.destroy()


def sliderChanged(event):
    global slider_val
    slider_val = int(slider.get())
    if globtype == "Break":
        label2.configure(text="Break for " + str(int(slider.get())))
    elif globtype == "Eat":
        label2.configure(text="Eat in slot " + str(int(slider.get())))
    elif globtype == "Slot":
        label2.configure(text="Change to slot " + str(int(slider.get())))
    elif globtype == "Wait":
        label2.configure(text="Wait for " + str(int(slider.get())))
    else:
        label2.configure(text="Move " + str(int(slider.get())) + " Blocks")


def createSettingsWindow(type):
    print("test")
    global instruct
    global root
    global globtype
    global slider_val
    slider_val = 1
    globtype = type
    instruct += type
    root = customtkinter.CTk()
    root.title(type)
    root.geometry("300x400")
    customtkinter.set_appearance_mode("dark")

    font = customtkinter.CTkFont(family="Monospace", size=16, weight="bold")

    global slider
    global label2
    label2 = customtkinter.CTkLabel(root, font=font, text="Move 1 Blocks")
    if type == "Break":
        label2.configure(text="Break for 1s")
    elif type == "Eat":
        label2.configure(text="Eat in slot 1")
    elif type == "Wait":
        label2.configure(text="Wait for 1s")
    elif type == "Slot":
        label2.configure(text="Change to slot 1")
    slider = customtkinter.CTkSlider(root, from_=1, to=9, command=sliderChanged, number_of_steps=8)
    slider.set(1)
    label2.pack(pady=10)
    slider.pack(pady=10)

    button2 = customtkinter.CTkButton(root, text="Done", command=lambda: doneEdit(type), font=font)
    button2.pack(pady=10)

    root.mainloop()


def loadNew():
    file = tkinter.filedialog.askopenfilename()
    path = Path(file)
    file_name = str(path)
    try:
        with open(str(path), "r") as file:
            file_contents = file.read()

            # Step 3: Check the file extension
            if file_name.endswith(".mm"):
                label.configure(state='normal')
                label.delete(0.0, END)
                label.insert(END, file_contents)
                label.configure(state='disabled')
            else:
                tkinter.messagebox.showwarning("Warning", "This is not the correct file type.")

    except FileNotFoundError:
        print(f"The file '{file_name}' was not found.")
    except Exception as e:
        print(f"An error occurred: {e}")


def clear():
    label.configure(state='normal')
    label.delete(0.0, END)
    label.configure(state='disabled')


def save():
    p = tkinter.filedialog.asksaveasfilename(defaultextension=".mm",
                                             filetypes=(("minemacro file", "*.mm"), ("All files", "*.*")))
    path = Path(p)

    with open(str(path), "w") as file:
        file.write(label.get(0.0, END))


root = customtkinter.CTk()
root.geometry("500x650")
customtkinter.set_appearance_mode("dark")
root.iconbitmap("MM.ico")

root.minsize(500, 650)
root.maxsize(500, 650)

menu = tkinter.Menu(root)
root.configure(menu=menu)
filemenu = tkinter.Menu(menu, tearoff=0)
menu.add_cascade(label='File', menu=filemenu)
filemenu.add_command(label='Save', command=save)
filemenu.add_command(label='Load', command=loadNew)

customtkinter.set_default_color_theme("TestCard.json")

font = customtkinter.CTkFont(family="Monospace", size=16, weight="bold")

sidebar = customtkinter.CTkFrame(root, width=200)
sidebar.pack(fill=customtkinter.Y, side=customtkinter.LEFT)

label = customtkinter.CTkTextbox(sidebar, font=font, width=200, height=470)
label.configure(state=DISABLED)
label.pack(pady=10, padx=30)

playButton = customtkinter.CTkButton(sidebar, text="Play", command=lambda: Play.play(label.get(0.0, 'end')), font=font)
playButton.pack(pady=10, side=customtkinter.BOTTOM)

stopButton = customtkinter.CTkButton(sidebar, text="Stop", command=lambda: Play.stopButton(), font=font)
stopButton.pack(pady=10, side=customtkinter.BOTTOM)

clearButton = customtkinter.CTkButton(sidebar, text="Clear", command=lambda: clear(), font=font)
clearButton.pack(pady=10, side=customtkinter.BOTTOM)

maincontent = customtkinter.CTkFrame(root, bg_color="#202123")
maincontent.pack(fill=customtkinter.BOTH, expand=True)

button1 = customtkinter.CTkButton(maincontent, text="Move Forwards", command=lambda: createSettingsWindow("Forwards"),
                                  font=font)
button1.pack(pady=10)
button2 = customtkinter.CTkButton(maincontent, text="Move Backwards",
                                  command=lambda: createSettingsWindow("Backwards"), font=font)
button2.pack(pady=10)
button3 = customtkinter.CTkButton(maincontent, text="Move Right", command=lambda: createSettingsWindow("Right"),
                                  font=font)
button3.pack(pady=10)
button4 = customtkinter.CTkButton(maincontent, text="Move Left", command=lambda: createSettingsWindow("Left"),
                                  font=font)
button4.pack(pady=10)
button4 = customtkinter.CTkButton(maincontent, text="Attack (Short Click)", command=lambda: addText("Short-Click"), font=font)
button4.pack(pady=10)
button4 = customtkinter.CTkButton(maincontent, text="Break (Long Click)",
                                  command=lambda: createSettingsWindow("Break"), font=font)
button4.pack(pady=10)
button7 = customtkinter.CTkButton(maincontent, text="Eat", command=lambda: createSettingsWindow("Eat"), font=font)
button7.pack(pady=10)
button6 = customtkinter.CTkButton(maincontent, text="Anti AFK", command=lambda: addText("Anti AFK"), font=font)
button6.pack(pady=10)
button5 = customtkinter.CTkButton(maincontent, text="Wait", command=lambda: createSettingsWindow("Wait"), font=font)
button5.pack(pady=10)
button8 = customtkinter.CTkButton(maincontent, text="Change Slot", command=lambda: createSettingsWindow("Slot"),
                                  font=font)
button8.pack(pady=10)

root.mainloop()

# minemacrodist

# MineMacro

MineMacro is an OpenSource Minecraft Macro Software. It lets you control your character to automate semi-automatic farms or any other repetative task. It has a simple GUI and Macro Profiles are save- and loadable. Macros will only play while using any Minecraft version on the normal Minecraft launcher or Lunar Client (more support coming soon).


## Table of Contents

- [minemacrodist](#minemacrodist)
- [MineMacro](#minemacro)
  * [Installation](#installation)
    + [Allow MineMacro on Windows Defender](#allow-minemacro-on-windows-defender--windows-11--)
    + [Run with Python](#run-python)
  * [Use MineMacro](#use-minemacro)
    + [GUI](#gui-)
    + [Explanation](#explanation-)
  * [Issues](#issues)





## Installation

Unzip the .zip located in Releases. If you get an Anti-Virus alert after unzipping you have to allow the Installer on your PC. If you don't trust it, you will have to compile the python program yourself. If Python is intalled this isn't hard. More to that later.


### Allow MineMacro on Windows Defender (Windows 11):

Hit Start and type Windows Security and click the follow option

![Screenshot 2023-10-04 222018](https://github.com/NightCraftHD/minemacrodist/assets/66378341/1cde08e1-e85a-4ead-9ea5-12bf6301a58d)

---------------------------------------------------------------------------------------------------------------------

Click "Protection History"

![Screenshot 2023-10-04 221910](https://github.com/NightCraftHD/minemacrodist/assets/66378341/86cab4b0-b0a0-4adc-baae-9fe7bfdf5097)

---------------------------------------------------------------------------------------------------------------------

Find the correct File (Double check so you don't allow a Virus)

![Screenshot 2023-10-04 221925](https://github.com/NightCraftHD/minemacrodist/assets/66378341/80b0c8f4-8de0-4974-bd1f-1c81e612a4b3)

---------------------------------------------------------------------------------------------------------------------

Click Actions

![Screenshot 2023-10-04 221928](https://github.com/NightCraftHD/minemacrodist/assets/66378341/bc42b356-eeca-4f88-a442-5f6d438e87d6)

---------------------------------------------------------------------------------------------------------------------

Click Restore

![Screenshot 2023-10-04 221933](https://github.com/NightCraftHD/minemacrodist/assets/66378341/490a1f61-9ac2-45ef-b3fa-3bcc6918ce4c)

---------------------------------------------------------------------------------------------------------------------

Or Click Allow on Device

![image](https://github.com/NightCraftHD/minemacrodist/assets/66378341/24398c9f-041e-4703-a67e-9d04049e5c38)

---------------------------------------------------------------------------------------------------------------------

After this run the installation. When the installation is finished you can launch it from the windows start menu or if selected a Desktop-Shortcut.


### Run with Python

Make sure Python and PIP are installed. Then run the following commands:

```python
pip install pynput==1.6.8
pip install pygetwindow
pip install pyautogui
pip install tkinter
pip install custontkinter
pip install pathlib
python GUI.py
```


## Use MineMacro
**IMPORTANT: THE PROGRAM AUTOMATICALLY LOOPS**


### GUI:

##### **1: Action selector**: Click actions to use them. They will appear in the action panel (left). Actions will be explained later.

##### **2: Control center**: Start or Stop the Macro. Clear will clear the action panel.

##### **3: Action panel**: Displays all actions that have been selected. 

##### **4: File Selector**: Save your design to a MineMacro file or load on old one. Files can also be shared with others, although **I don't recommend using files from people you cannot trust**.

![1 (15)](https://github.com/NightCraftHD/minemacrodist/assets/66378341/d35cd136-d532-47d8-af1a-b69d59a7d2fc)

### Explanation:

#### Action Explanation

**Move Forwards:**
Move forwards the selected number of blocks (This will never be 100% accurate. I recommend not using for exact movements) e. g. collecting xp from a farm

**Move Backwards:** 
Move backwards the selected number of blocks

**Move Right:**
Move right the selected number of blocks

**Move Left:** 
Move left the selected number of blocks

**Attack:** 
Clicks once -> Hit

**Break:** 
Select the number of seconds the LMB is pressed -> Break

**Eat:** 
Select the slot ywhere your food it. The program will automatically eat. If you are using an item (e. g. Pickaxe, Sword) you will need to switch back to it using the slot action.

**Anti AFK:** 
Moves mouse around. This will always move the mouse back to the same spot, regardless of sensitivity.

**Wait:** 
Wait selected amount of seconds.

**Slot:**
Select a slot to switch to.

All actions can be used as many times as you would like.

Remeber: The program will automatically loop. It is not required to manually use actions to loop.

![Screenshot 2023-10-04 224340](https://github.com/NightCraftHD/minemacrodist/assets/66378341/ecda55c6-2fba-4235-bb08-5fd580c2aae3)


#### Action Settings Window

Use the slider to change the number of Blocks/Seconds. If more are needed simply add another action.

![Screenshot 2023-10-04 224355](https://github.com/NightCraftHD/minemacrodist/assets/66378341/46c6d5d4-2200-46f4-98b2-0fe8c5ddbf89)


#### Control Panel

Stop will stop the current macro. Please note that when you do not have a Minecraft window open, the macro will not run. If you return to the window it will continue.

Start will start the macro described in the action panel. If another macro is currentlyy running, it is not needed to stop the macro. You can simply hit start.

Clear will clear the whole action panel. If you have a long macro you can save it and edit the .mm file using Notepad. While doing this make sure you keep the MineMacro format (e. g. Slot 5 not Slot-5) or the program might have problems reading the file.

![Screenshot 2023-10-04 224345](https://github.com/NightCraftHD/minemacrodist/assets/66378341/56bcb519-520d-42a5-b288-f563310f5a80)



## Issues

If you have any problems, you are welcome to send me an email at kiyanstudios@gmail.com.

Disclaimer: This is not intended for public Server use. Use in Singleplayer or your own Servers only. I am not responsible for any consiquences that follow after the use of the program, although I can almost guarantee it will not cause problems in Singleplayer because it simulates Key-Presses. 

## Thanks a lot for installing!


import os
import time
import keyboard
import sys

def clear():
    os.system("cls" if os.name == "nt" else "clear")
    sys.stdout.flush()

screen = [
    [1, 1, 1, 1, 1, 1, 1, 1, 0, 2, 0, 2, 0, 2, 0],
    [1, 0, 2, 0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2],
    [1, 2, 0, 2, 0, 2, 0, 1, 0, 2, 0, 2, 0, 2, 0],
    [1, 0, 2, 0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2],
    [1, 2, 0, 2, 0, 2, 0, 1, 0, 2, 0, 2, 0, 2, 0],
    [1, 0, 2, 0, 2, 0, 2, 1, 2, 0, 2, 0, 2, 0, 2],
    [1, 2, 0, 2, 0, 2, 0, 1, 0, 2, 1, 1, 1, 1, 1],
    [1, 0, 2, 0, 2, 0, 2, 1, 2, 0, 1, 0, 2, 0, 1],
    [1, 1, 1, 2, 0, 1, 1, 1, 0, 2, 1, 2, 0, 2, 1],
    [0, 2, 1, 0, 2, 1, 2, 0, 2, 0, 1, 0, 2, 0, 1],
    [2, 0, 1, 2, 0, 1, 0, 2, 0, 2, 1, 1, 0, 1, 1],
    [0, 2, 1, 0, 2, 1, 2, 0, 2, 0, 2, 1, 2, 1, 2],
    [2, 0, 1, 2, 0, 1, 1, 1, 1, 1, 1, 1, 0, 1, 0],
    [0, 2, 1, 0, 2, 0, 2, 0, 2, 0, 2, 0, 2, 1, 2],
    [2, 0, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 1, 0],
]

playerpos = [1, 1]
playerchar = "{#}"

showingstats = True

render = ""
delta = 0.
prevtime = time.time()

while True:
    if keyboard.is_pressed("esc"):
        break
    delta = time.time() - prevtime
    prevtime = time.time()
    newrender = ""

    # movement with the keyboard
    if keyboard.is_pressed("w") and screen[playerpos[1] - 1][playerpos[0]] != 1:
        playerpos = [playerpos[0], playerpos[1] - 1]
    elif keyboard.is_pressed("s") and screen[playerpos[1] + 1][playerpos[0]] != 1:
        playerpos = [playerpos[0], playerpos[1] + 1]
    if keyboard.is_pressed("d") and screen[playerpos[1]][playerpos[0] + 1] != 1:
        playerpos = [playerpos[0] + 1, playerpos[1]]
    elif keyboard.is_pressed("a") and screen[playerpos[1]][playerpos[0] - 1] != 1:
        playerpos = [playerpos[0] - 1, playerpos[1]]

    # draw the ascii render to the screen
    for y, i in enumerate(screen):
        line = ""
        for x, n in enumerate(i):
            if x == playerpos[0] and y == playerpos[1]:
                line += f"\033[32m{playerchar}\033[0m"
            elif n == 1:
                line += "\033[93m▒▒▒\033[0m"
            elif n == 0:
                line += "\033[90m░░░\033[0m"
            elif n == 2:
                line += "\033[97m░░░\033[0m"
        newrender += line + "\n"
    if showingstats:
        # show player position and debug info
        newrender += f"--DEBUG--\nPOSITION {playerpos}\n"

    if render != newrender or render == "":
        clear()
        sys.stdout.write(newrender)
        print("\033[H", end="")
        render = newrender
    time.sleep(delta / 15)

from gtts import gTTS
from playsound import playsound
import os
import subprocess
import json
import secrets

active_process = None

# Prereq:
#   Install sox (Linux)
#       Arch Linux: 
#           $ sudo pacman -S sox
#       Ubuntu: 
#           $ sudo apt-get update
#           $ sudo apt-get install sox
#           $ sudo apt-get install libsox-fmt-all
def play_mp3(path, active_process):
    try:
        active_process.terminate()
    except:
        pass

    DEVNULL = open(os.devnull, 'wb')
    try:
        active_process = subprocess.Popen(['play', path, 'tempo', '1.5'], stdout = DEVNULL, stderr = DEVNULL)
    finally:
        DEVNULL.close()

f = open('db.json',)
data = json.load(f)

flow = [
    ["_greeting", "_education", "_finances", "_exit"],
    ["_greeting", "_finances", "_exit"],
    ["_greeting", "_aboutNEU", "_finances","_exit"],
    ["_greeting", "_finances", "_grill", "_exit"],
    ["_greeting", "_education", "_finances", "_grill", "_exit"],
    ["_greeting", "_aboutNEU", "_education", "_exit"],
    ["_greeting", "_aboutNEU", "_education", "_finances", "_exit"],
]

while (True):
    print("----------START----------")
    chosen_flow = secrets.choice(flow)

    for item in chosen_flow:
        state = data[item]

        while(state):
            keys = list(state.keys())
            chosen_key = secrets.choice(keys)
            print("VO: "+chosen_key, end="")
            speech = gTTS(text = chosen_key, lang='en', slow=False)
            speech.save('temp.mp3')

            #####
            # If sox isn't installed use the playsound library 
            play_mp3('temp.mp3', active_process)
            # os.system("play temp.mp3 tempo 1.5")
            # playsound('temp.mp3')
            #####
            try:
                input("")
            except EOFError:
                state = state[chosen_key]
                continue
            state = state[chosen_key]

    print("-----------END-----------", end="")
    input("")

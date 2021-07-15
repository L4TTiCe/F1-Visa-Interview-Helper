import json
import secrets

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
            input("")

            state = state[chosen_key]
    print("-----------END-----------", end="")
    input("")

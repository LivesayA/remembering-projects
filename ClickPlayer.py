import time
import json
import pyautogui

pyautogui.FAILSAFE = True

with open("mouse_recording.json", "r") as f:
    events = json.load(f)
    
print("Starting replay in 3 seconds...")
time.sleep(3)

previous_time = 0

for event in events:
    #Calculate delay between this event and previous one.
    delay = event["time"] - previous_time
    time.sleep(delay)
    previous_time = event["time"]
    
    if event["type"] == "move":
        pyautogui.moveTo(event["x"], event["y"])
    elif event["type"] == "click":
        if event["pressed"]:
            pyautogui.mouseDown(event["x"], event["y"])
        else:
            pyautogui.mouseUp(event["x"], event["y"])

print("Replay finished.")
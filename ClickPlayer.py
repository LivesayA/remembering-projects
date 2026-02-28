import time
import json
import pyautogui

with open("mouse_recording.json", "r") as f:
    events = json.load(f)
    
print("Starting replay in 3 seconds...")
time.sleep(3)

start_time = time.time()

for event in events:
    while time.time() - start_time < event["time"]:
        pass
    
    if event["type"] == "move":
        pyautogui.moveTo(event["x"], event["y"])
    elif event["type"] == "click":
        if event["pressed"]:
            pyautogui.mouseDown(event["x"], event["y"])
        else:
            pyautogui.mouseUp(event["x"], event["y"])

print("Replay finished.")
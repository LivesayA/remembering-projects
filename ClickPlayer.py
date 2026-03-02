import time
import json
import pyautogui

class ClickPlayer:
    def __init__(self, filename, loop=False, speed=1.0):
        self.filename = filename
        self.loop = loop
        self.speed = speed
        self.events = self.load_events()
        
        pyautogui.FAILSAFE = True
        
    def load_events(self):
        with open(self.filename, "r") as f:
            return json.load(f)
    
    def play_once(self):
        previous_time = 0
        
        for event in self.events:
            delay = (event["time"] - previous_time) / self.speed
            time.sleep(max(delay, 0))
            previous_time = event["time"]
            
            if event["type"] == "move":
                pyautogui.moveTo(event["x"], event["y"])
            elif event["type"] == "click":
                if event["pressed"]:
                    pyautogui.mouseDown(event["x"], event["y"])
                else:
                    pyautogui.mouseUp(event["x"], event["y"])
    
    def play(self):
        print("Starting replay in 3 seconds...")
        time.sleep(3)
        
        if self.loop:
            while True:
                self.play_once()
        else:
            self.play_once()
            
if __name__ == "__main__":
    player = ClickPlayer(
        filename="mouse_recording.json",
        loop=True, #Set to false for single playback
        speed=1.0 #1.0 = normal speed
    )
    
    player.play()

with open("mouse_recording.json", "r") as f:
    events = json.load(f)
    
print("Starting replay in 3 seconds...")
time.sleep(3)

#previous_time = 0

#for event in events:
    #Calculate delay between this event and previous one.
#    delay = event["time"] - previous_time
#    time.sleep(delay)
#    previous_time = event["time"]
#    
#    if event["type"] == "move":
#        pyautogui.moveTo(event["x"], event["y"])
#    elif event["type"] == "click":
#        if event["pressed"]:
#            pyautogui.mouseDown(event["x"], event["y"])
#        else:
#            pyautogui.mouseUp(event["x"], event["y"])

#print("Replay finished.")
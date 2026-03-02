import time
import json
import threading
import pyautogui


class ClickPlayer:
    def __init__(self):
        self.events = []
        self.loop = False
        self.speed = 1.0
        
        self.running = False
        self.paused = False
        self.thread = None
        
        pyautogui.FAILSAFE = True
        
    def load_events(self):
        with open(self.filename, "r") as f:
            self.events = json.load(f)
    
    def play_once(self):
        previous_time = 0
        
        for event in self.events:
            if not self.running:
                return
            
            while self.paused:
                time.sleep(0.1)
            
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
                    
    def run(self):
        self.running = True
        while self.running:
            self.play_once()
            if not self.loop:
                break
        self.running = False
    
    def start(self):
        if not self.events:
            print("No events loaded.")
            return
        
        if not self.running:
            self.thread = threading.Thread(target=self.run)
            self.thread.start()
            
    def stop(self):
        self.running = False
        
    def toggle_pause(self):
        self.paused = not self.paused
        print("Paused" if self.paused else "Resumed")
        
class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom AutoClicker")
        
        self.player = ClickPlayer()
            
if __name__ == "__main__":
    player = ClickPlayer(
        filename="mouse_recording.json",
        loop=True, #Set to false for single playback
        speed=1.0 #1.0 = normal speed
    )
    
    player.play()

# with open("mouse_recording.json", "r") as f:
#     events = json.load(f)
    
# print("Starting replay in 3 seconds...")
# time.sleep(3)

# previous_time = 0

# for event in events:
#     #Calculate delay between this event and previous one.
#     delay = event["time"] - previous_time
#     time.sleep(delay)
#     previous_time = event["time"]
    
#     if event["type"] == "move":
#         pyautogui.moveTo(event["x"], event["y"])
#     elif event["type"] == "click":
#         if event["pressed"]:
#             pyautogui.mouseDown(event["x"], event["y"])
#         else:
#             pyautogui.mouseUp(event["x"], event["y"])

# print("Replay finished.")
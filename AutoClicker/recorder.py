import time
import json
from pynput import mouse

class Recorder:
    def __init__(self):
        self.events = []
        self.start_time = None
        self.listener - None
    
    def _on_click(self, x, y, button, pressed):
        if self.start_time is None:
            self.start_time = time.time()
            
        event_time = time.time() - self.start_time
        
        self.events.append({
            "type": "click",
            "x": x,
            "y": y,
            "button": str(button),
            "pressed": pressed,
            "time": event_time
        })
        
    def _on_move(self, x, y):
        if self.start_time is None:
            self.start_time = time.time()
        
        event_time = time.time() - self.start_time
        
        self.events.append({
            "type": "move",
            "x": x,
            "y": y,
            "time": event_time
        })
        
    def start(self):
        self.events = []
        self.start_time = None
        self.listener = mouse.Listener(
            on_click=self._on_click,
            on_move=self._on_move
        )
        self.listener.start()
        print("Recording started.")
        
    def stop(self, filename="mouse_recording.json"):
        if self.listener:
            self.listener.stop()
            self.listener = None
            
        with open(filename, "w") as f:
            json.dump(self.events, f, indent=4)
            
        print("Recording saved to", filename)
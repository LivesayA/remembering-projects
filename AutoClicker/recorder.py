import time, json, logging
from pynput import mouse
from pathlib import Path

logger = logging.getLogger(__name__)

class Recorder:
    def __init__(self, config):
        self.config = config
        self.events = []
        self.start_time = None
        self.listener = None
        self.last_position = None
    
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
        if not self.config.get("record_moves"):
            return
        
        if self.start_time is None:
            self.start_time = time.time()
        
        threshold = self.config.get("move_threshold")
        
        if self.last_position:
            dx = abs(x - self.last_position[0])
            dy = abs(y - self.last_position[1])
            if dx < threshold and dy < threshold:
                return
        
        self.last_position = (x, y)
        
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
        logger.info("Recording started. (Hotkey)")
        #print("Recording started.")
        
    def stop(self, filename="mouse_recording.json"):
        
        filename = self.config.get("recording_file")
        
        with open(filename, "w") as f:
            json.dump(self.events, f, indent=4)
            
        #logger.info("Recording saved to %s", filename)
        
        BASE_DIR = Path(__file__).resolve().parent
        filename = BASE_DIR / "mouse_recording.json"
        
        if self.listener:
            self.listener.stop()
            self.listener = None
            
        with open(filename, "w") as f:
            json.dump(self.events, f, indent=4)
        logger.info("Recording saved to %s", filename)
        #print("Recording saved to", filename)
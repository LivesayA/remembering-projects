import time, json, threading, pyautogui, logging

logger = logging.getLogger(__name__)

class ClickPlayer:
    def __init__(self, config):
        self.config = config
        self.events = []
        
        self.pause_event = threading.Event()
        self.stop_event = threading.Event()
        self.thread = None
        
        pyautogui.FAILSAFE = True
        pyautogui.PAUSE = 0
        
    def load_events(self, filename):
        logger.info("Loading file: %s", filename)
        
        filename = self.config.get("recording_file")
        with open(filename, "r") as f:
            self.events = json.load(f)
        
        logger.info("Loaded %d events", len(self.events))    
        logger.info("Loaded events from %s", filename)
    
    def _play_once(self):
        previous_time = 0
        speed = self.config.get("speed", 1.0)
        
        for event in self.events:
            if self.stop_event.is_set():
                return
            
            while self.pause_event.is_set():
                time.sleep(0.05)
            
            
            delay = (event["time"] - previous_time) / speed
            #delay = (event["time"] - previous_time) / self.config.get("speed")
            time.sleep(max(delay, 0))
            previous_time = event["time"]
            
            if event["type"] == "move":
                pyautogui.moveTo(event["x"], event["y"], duration=0)
            elif event["type"] == "click":
                if event["pressed"]:
                    pyautogui.mouseDown(event["x"], event["y"])
                else:
                    pyautogui.mouseUp(event["x"], event["y"])
                    
    def _run(self):
        logger.info("Playback started")
        while not self.stop_event.is_set():
            self._play_once()
            if not self.config.get("loop"):
                break
        logger.info("Playback stopped")
    
    def start(self):
        if not self.events:
            logger.info("No events loaded.")
            #print("No events loaded.")
            return
        
        if self.thread and self.thread.is_alive():
            return
        
        self.stop_event.clear()
        self.pause_event.clear()
        
        self.thread = threading.Thread(target=self._run, daemon=True)
        self.thread.start()
        
        # if not self.running:
        #     self.thread = threading.Thread(target=self._runrun)
        #     self.thread.start()
            
    def stop(self):
        self.stop_event.set()
        #self.running = False
        
    def toggle_pause(self):
        if self.pause_event.is_set():
            self.pause_event.clear()
            logger.info("Playback resumed")
        else:
            self.pause_event.set()
            logger.info("Playback paused")
        # self.paused = not self.paused
        # logger.info("Paused" if self.paused else "Resumed")
        #print("Paused" if self.paused else "Resumed")
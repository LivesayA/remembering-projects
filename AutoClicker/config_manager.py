import json
import os

class ConfigManager:
    def __init__(self, filename="config.json"):
        self.filename = filename
        self.config = {
            "speed": 1.0,
            "loop": False,
            "move_threshold": 5,
            "record_moves": True,
            "hotkeys": {
                "start": "f6",
                "stop": "f7",
                "pause": "f8",
                # "start_recording": "f9",
                # "stop_recording": "f10"
            },
            "last_file": ""
        }
        
        self.load()
        
    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.config.update(json.load(f))
                
    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.config, f, indent=4)
            
    def get(self, key, default=None):
        return self.config.get(key, default)
    
    def set(self, key, value):
        self.config[key] = value
        self.save()
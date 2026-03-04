import json
import os

class ConfigManager:
    def __init__(self, filename="config.json"):
        self.filename = filename
        self.config = {
            "speed": 1.0,
            "loop": False,
            "hotkeys": {
                "start": "f6",
                "stop": "f7",
                "pause": "f8"
            },
            "last_file": "",
            "record_moves": True
        }
        
        self.load()
        
    def load(self):
        if os.path.exists(self.filename):
            with open(self.filename, "r") as f:
                self.config.update(json.load(f))
                
    def save(self):
        with open(self.filename, "w") as f:
            json.dump(self.config, f, indent=4)
            
    def get(self, key):
        return self.config.get(key)
    
    def set(self, key, value):
        self.config[key] = value
        self.save()
from pynput import keyboard

class GlobalHotkeyManager:
    
    def __init__(self, start_callback, stop_callback, pause_callback, config):
        hotkey_config = config.get("hotkeys")
        
        self.manager = keyboard.GlobalHotKeys({
            f"<{hotkey_config['start']}>": start_callback,
            f"<{hotkey_config['stop']}>": stop_callback,
            f"<{hotkey_config['pause']}>": pause_callback
        })
    
    def start(self):
        self.manager.start()
        
    def stop(self):
        self.manager.stop()
        
    def pause(self):
        self.manager.pause()
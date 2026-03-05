from pynput import keyboard

# start_recording, stop_recording,

class GlobalHotkeyManager:
    
    def __init__(self, start_callback, stop_callback, pause_callback, config):
        hotkey_config = config.get("hotkeys")
        
        self.manager = keyboard.GlobalHotKeys({
            f"<{hotkey_config['start']}>": start_callback,
            f"<{hotkey_config['stop']}>": stop_callback,
            f"<{hotkey_config['pause']}>": pause_callback
            # f"<{hotkey_config['start_recording']}>": start_recording,
            # f"<{hotkey_config['stop_recording']}>": stop_recording
            
        })
    
    def start(self):
        self.manager.start()
        
    def stop(self):
        self.manager.stop()
        
    # def start_recording(self):
    #     self.manager.start_recording()
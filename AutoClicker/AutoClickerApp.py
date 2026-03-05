import tkinter as tk
from tkinter import ttk, filedialog
import logging

from recorder import Recorder
from player import ClickPlayer
from config_manager import ConfigManager
from hotkeys import GlobalHotkeyManager

logger = logging.getLogger(__name__)

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom AutoClicker")
        
        self.config = ConfigManager()
        self.recorder = Recorder(self.config)
        self.player = ClickPlayer(self.config)
        
        
        self.create_widgets()
        
        self.hotkeys = GlobalHotkeyManager(
            start_callback=self.player.start,
            stop_callback=self.player.stop,
            pause_callback=self.player.toggle_pause,
            config=self.config
        )
        
        self.hotkeys.start()
        
    def create_widgets(self):
        
        main = ttk.Frame(self.root, padding=10)
        main.pack(fill="both", expand=True)
        
        self.status_var = tk.StringVar(value="Ready")
        
        #GUI Elements
        
        #Recording Frame
        record_frame = ttk.LabelFrame(main, text="Recording")
        record_frame.pack(fill="x", pady=5)
        
        
        tk.Button(record_frame, text="Start Recording", 
                  command=self.recorder.start).pack(side="left", padx=5) #Starting a recording
        
        tk.Button(record_frame, text="Stop Recording", 
                  command=self.recorder.stop).pack(side="left", padx=5) #Stopping a recording
        
        #Playback Frame
        playback_frame = ttk.LabelFrame(main, text="Playback")
        playback_frame.pack(fill="x", pady=5)
        
        tk.Button(playback_frame, text="Load Recording", 
                  command=self.load_file).pack(side="left", padx=5) #Loading a Recording
        
        tk.Button(playback_frame, text="Start Playback", 
                  command=self.player.start).pack(side="left", padx=5) #Starting Playback
        
        tk.Button(playback_frame, text="Stop Playback", 
                  command=self.player.stop).pack(side="left", padx=5) #Stopping Playback
        
        tk.Button(playback_frame, text="Pause / Resume",
                  command=self.player.toggle_pause).pack(side="left", padx=5) #Toggle Pause
        
        #Settings Frame
        settings_frame = ttk.LabelFrame(main, text="Settings")
        settings_frame.pack(fill="x", pady=5)
        
        self.loop_var = tk.BooleanVar(value=self.config.get("loop"))
        ttk.Checkbutton(settings_frame, text="Loop", 
                        variable=self.loop_var, 
                        command=self.update_loop).pack(side="left", pady=5)
        
        ttk.Label(settings_frame, text="Speed:").pack(side="left")
        self.speed_entry = ttk.Entry(settings_frame, width=6)
        self.speed_entry.insert(0, str(self.config.get("speed")))
        self.speed_entry.pack(side="left", padx=5)
        
        ttk.Button(settings_frame, text="Apply",
                   command=self.update_speed).pack(side="left", padx=5)
        
        #Status Bar
        status_label = ttk.Label(self.root, textvariable=self.status_var, 
                                 relief="sunken", anchor="w")
        status_label.pack(fill="x", side="bottom")
        
    def stop_recording(self):
        self.recorder.stop()
        
    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filename:
            self.config.set("recording_file", filename)
            self.player.load_events(filename)
            self.config.set("last_file", filename)
            self.status_var.set(f"Loaded {filename}")
            logger.info("Loaded: %s", filename)
            #print("Loaded: ", filename)
            
    def update_loop(self):
        self.config.set("loop", self.loop_var.get())
        
    def update_speed(self):      
        try:
            speed = float(self.speed_entry.get())
            self.config.set("speed", speed)
            self.status_var.set("Speed updated")
            #self.player.speed = float(self.speed_entry.get())
        except ValueError:
            logger.info("Invalid speed value entered.")
            self.status_var.set("Invalid speed value")
            #print("Invalid speed value.")
            
    def on_key_press(self, key):
        try:
            if key.char == 's': #Start
                self.player.start()
            elif key.char == 'x': #Stop
                self.player.stop()
            elif key.char == 'p': #Pause
                self.player.toggle_pause()
        except AttributeError:
            pass
        

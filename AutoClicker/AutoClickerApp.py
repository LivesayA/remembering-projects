import tkinter as tk
from tkinter import filedialog
from recorder import Recorder
from player import ClickPlayer

class AutoClickerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Custom AutoClicker")
        
        self.recorder = Recorder()
        self.player = ClickPlayer()
        
        #GUI Elements
        tk.Button(root, text="Start Recording", 
                  command=self.recorder.start).pack() #Starting a recording
        
        tk.Button(root, text="Stop Recording", 
                  command=self.recorder.stop).pack() #Stopping a recording
        
        tk.Button(root, text="Load Recording", 
                  command=self.load_file).pack() #Loading a Recording
        
        tk.Button(root, text="Start Playback", 
                  command=self.player.start).pack() #Starting Playback
        
        tk.Button(root, text="Stop Playback", 
                  command=self.player.stop).pack() #Stopping Playback
        
        tk.Button(root, text="Pause / Resume",
                  command=self.player.toggle_pause).pack() #Toggle Pause
        
        self.loop_var = tk.BooleanVar()
        tk.Checkbutton(root, text="Loop", variable=self.loop_var, command=self.update_loop).pack()
        
        tk.Label(root, text="Speed (1,0 = normal)").pack()
        self.speed_entry = tk.Entry(root)
        self.speed_entry.insert(0, "1.0")
        self.speed_entry.pack()
        
        tk.Button(root, text="Apply Speed", command=self.update_speed).pack()
        
    def stop_recording(self):
        self.recorder.stop()
        
    def load_file(self):
        filename = filedialog.askopenfilename(filetypes=[("JSON Files", "*.json")])
        if filename:
            self.player.load_events(filename)
            print("Loaded: ", filename)
            
    def update_loop(self):
        self.player.loop = self.loop_var.get()
        
    def update_speed(self):      
        try:
            self.player.speed = float(self.speed_entry.get())
        except ValueError:
            print("Invalid speed value.")
            
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
        

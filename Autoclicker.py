import time, json
from pynput import mouse

events = []
start_time = None

def on_click(x, y, button, pressed):
    global start_time
    if start_time is None:
        start_time = time.time()
        
    event_time = time.time() - start_time
    
    events.append({
        "type": "click",
        "x": x,
        "y": y,
        "button": str(button),
        "pressed": pressed,
        "time": event_time
    })
    
    print(f"{'Pressed' if pressed else 'Released'} at {(x,y)}")
    
def on_move(x,y):
    global start_time
    if start_time is None:
        start_time = time.time()
    
    event_time = time.time() - start_time
    
    events.append({
        "type": "move",
        "x": x,
        "y": y,
        "time": event_time
    })
    
with mouse.Listener(on_click=on_click, on_move=on_move) as listener:
    print("Recording... Press Ctrl+C to stop.")
    try:
        listener.join()
    except KeyboardInterrupt:
        with open("mouse_recording.json", "w") as f:
            json.dump(events, f, indent=4)
        print("Recording saved.")
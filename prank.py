#!/usr/bin/env python3
import tkinter as tk
import time
import random
import threading

class HackedScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.root.attributes('-topmost', True)
        
        self.time_left = 3599
        
        self.setup_ui()
        self.glitch_effect()
        self.update_timer()

    def setup_ui(self):
        # Matrix Hintergrund zuerst erstellen (damit er hinten ist)
        self.canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Hauptframe über dem Canvas
        frame = tk.Frame(self.root, bg='black')
        frame.place(relx=0.5, rely=0.5, anchor='center')
        frame.lift()  # Frame über Canvas heben

        # Schädel
        skull = tk.Label(frame, text="☠️", font=('Courier', 72), bg='black', fg='red')
        skull.pack()

        # HACKED Text
        self.title_label = tk.Label(frame, text="SYSTEM HACKED",
                                    font=('Courier', 64, 'bold'),
                                    bg='black', fg='red')
        self.title_label.pack(pady=20)

        # Timer
        self.timer_label = tk.Label(frame, text="00:59:59",
                                    font=('Courier', 48, 'bold'),
                                    bg='black', fg='yellow')
        self.timer_label.pack(pady=10)

        # Warnungstext
        warning_text = """ALL YOUR FILES HAVE BEEN ENCRYPTED!

To recover your data, send 0.5 BTC to:

bc1qNepfloH4ck3dPr4nkL0lR0fL42069xXxX

Time remaining before PERMANENT DELETION..."""

        warning = tk.Label(frame, text=warning_text,
                           font=('Courier', 16),
                           bg='black', fg='white',
                           justify='center',
                           wraplength=800)
        warning.pack(pady=30)

        # Progress Bar
        self.progress = tk.Canvas(frame, width=600, height=30, bg='black',
                                  highlightthickness=2, highlightbackground='red')
        self.progress.pack(pady=20)
        self.progress_fill = self.progress.create_rectangle(0, 0, 0, 30, fill='red')

        # Hacked by
        hacked_by = tk.Label(self.root, text="Hacked by Nepflo",
                            font=('Courier', 20, 'bold'),
                            bg='black', fg='lime',
                            anchor='se')
        hacked_by.place(relx=1.0, rely=1.0, anchor='se', x=-20, y=-20)

        self.start_matrix()

    def glitch_effect(self):
        colors = ['red', '#ff00ff', '#00ffff', 'red', 'darkred']

        def glitch():
            while True:
                time.sleep(0.1)
                color = random.choice(colors)
                try:
                    self.title_label.config(fg=color)
                except:
                    break

        threading.Thread(target=glitch, daemon=True).start()

    def update_timer(self):
        hours = self.time_left // 3600
        minutes = (self.time_left % 3600) // 60
        seconds = self.time_left % 60

        time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
        try:
            self.timer_label.config(text=time_str)
        except:
            return

        # Progress bar füllen (rückwärts)
        progress_width = 600 * (self.time_left / 3599)
        try:
            self.progress.coords(self.progress_fill, 0, 0, progress_width, 30)
        except:
            pass

        if self.time_left > 0:
            self.time_left -= 1
            self.root.after(1000, self.update_timer)

    def start_matrix(self):
        chars = "01アイウエオカキクケコサシスセソタチツテトナニヌネノハヒフヘホマミムメモ"

        drops = []
        for x in range(0, 1920, 30):
            drops.append({'x': x, 'y': random.randint(-1000, 0), 
                       'speed': random.randint(3, 8), 'chars': []})

        def animate():
            try:
                for drop in drops:
                    drop['y'] += drop['speed']
                    if drop['y'] > 1080:
                        drop['y'] = random.randint(-100, -10)
                        for char in drop['chars']:
                            self.canvas.delete(char)
                        drop['chars'] = []

                    if random.random() > 0.9:
                        char = random.choice(chars)
                        text = self.canvas.create_text(drop['x'], drop['y'], text=char,
                                                       fill='#003300', font=('Courier', 14))
                        drop['chars'].append(text)
                        if len(drop['chars']) > 15:
                            old = drop['chars'].pop(0)
                            self.canvas.delete(old)
                
                self.root.after(50, animate)
            except:
                pass

        animate()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = HackedScreen()
    app.run()

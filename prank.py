#!/usr/bin/env python3
import tkinter as tk
import time
import random
import threading

class FsocietyScreen:
    def __init__(self):
        self.root = tk.Tk()
        
        # Echte Vollbild ohne Fensterrahmen
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.configure(bg='black')
        
        # Mauszeiger verstecken (optional)
        self.root.config(cursor='none')
        
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        
        self.time_left = 3599
        self.glitch_active = True
        self.blink_state = True
        
        # Ein Canvas für ALLES (Hintergrund + UI)
        self.canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.canvas.pack(fill='both', expand=True)
        
        # Matrix Rain im Hintergrund
        self.setup_matrix_rain()
        
        # UI Elemente auf dem Canvas
        self.setup_ui()
        
        # Exit mit Alt+F4 und Escape
        self.root.bind('<Alt-F4>', lambda e: self.close())
        self.root.bind('<Escape>', lambda e: self.close())
        
        # Starte Effekte
        self.start_effects()

    def close(self):
        self.root.destroy()

    def setup_matrix_rain(self):
        self.chars = "日ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ0123456789"
        self.colors = ['#003300', '#005500', '#007700', '#009900', '#00bb00', '#00dd00', '#00ff00']
        self.drops = []
        
        for x in range(0, self.width, 20):
            self.drops.append({
                'x': x,
                'y': random.randint(-1000, 0),
                'speed': random.randint(3, 12),
                'items': []
            })

    def setup_ui(self):
        # Hauptcontainer in der Mitte
        center_x = self.width // 2
        center_y = self.height // 2
        
        # Guy Fawkes Maske (ASCII)
        mask_text = """
       ████████████       
     ██░░░░░░░░░░░░██     
   ██░░░░░░░░░░░░░░░░██   
  ██░░░░░░░░░░░░░░░░░░██  
 ██░░░░░░░░░░░░░░░░░░░░██ 
██░░░░░░░░░░░░░░░░░░░░░░██
██░░██░░░░░░░░░░░░░░██░░██
██░██░░░░░░░░░░░░░░░░██░██
██░██░░░░░░░░░░░░░░░░██░██
██░██░░░░░░░░░░░░░░░░██░██
██░██░░░░░░░░░░░░░░░░██░██
 ██░██░░░░░░░░░░░░░░██░██ 
 ██░░██░░░░░░░░░░░░██░░██ 
  ██░░████████████░░██  
   ██░░░░░░░░░░░░░░██   
     ██████████████     
        ██░░░░██        
        ██░░░░██        
          ████          
"""
        
        # Maske zeichnen
        self.canvas.create_text(center_x, 120, text=mask_text,
                               font=('Courier', 10), fill='#ff0040',
                               anchor='center', tags='mask')
        
        # Slogan
        slogans = [
            "We are Anonymous.",
            "We are Legion.",
            "We do not forgive.",
            "We do not forget.",
            "Expect us."
        ]
        
        y_pos = 280
        self.slogan_items = []
        for i, text in enumerate(slogans):
            color = '#00ff41' if i % 2 == 0 else '#ff0040'
            item = self.canvas.create_text(center_x, y_pos, text=text,
                                          font=('Courier', 14, 'bold'),
                                          fill=color, anchor='center')
            self.slogan_items.append(item)
            y_pos += 25
        
        # Trennlinie
        self.canvas.create_line(center_x-300, y_pos+10, center_x+300, y_pos+10,
                               fill='#00ff41', width=2)
        
        # Haupttitel
        self.title_main = self.canvas.create_text(center_x, y_pos+60,
                                                  text="SYSTEM HACKED",
                                                  font=('Courier', 48, 'bold'),
                                                  fill='#ff0040',
                                                  anchor='center')
        
        self.title_glitch = self.canvas.create_text(center_x-3, y_pos+57,
                                                    text="SYSTEM HACKED",
                                                    font=('Courier', 48, 'bold'),
                                                    fill='#00ff41',
                                                    anchor='center')
        
        # Subtitle
        self.canvas.create_text(center_x, y_pos+110,
                               text="[!] YOUR PRIVACY HAS BEEN COMPROMISED [!]",
                               font=('Courier', 16, 'bold'),
                               fill='#ff6600', anchor='center')
        
        # Terminal Box
        box_y = y_pos + 160
        self.canvas.create_rectangle(center_x-280, box_y, center_x+280, box_y+180,
                                    outline='#ff0040', fill='#0a0a0a', width=2)
        
        term_text = """>>> INITIATING SEQUENCE...
>>> BYPASSING FIREWALL... [OK]
>>> GAINING ROOT ACCESS... [OK]
>>> ENCRYPTING FILES... [OK]
>>> UPLOADING TO SERVER... [OK]

TARGET: Linux Mint Workstation
STATUS: COMPROMISED
ENCRYPTION: AES-256
BACKUPS: PURGED"""
        
        self.canvas.create_text(center_x, box_y+90, text=term_text,
                               font=('Courier', 11), fill='#00ff41',
                               anchor='center', justify='left')
        
        # Blinkender Cursor
        self.cursor = self.canvas.create_text(center_x+250, box_y+170,
                                             text="_", font=('Courier', 14, 'bold'),
                                             fill='#00ff41', anchor='se')
        
        # Bitcoin
        btc_y = box_y + 210
        self.canvas.create_text(center_x, btc_y,
                               text="═══ PAYMENT REQUIRED ═══",
                               font=('Courier', 14, 'bold'),
                               fill='#ff0040', anchor='center')
        
        self.canvas.create_text(center_x, btc_y+30,
                               text="TRANSFER 0.5 BTC TO:",
                               font=('Courier', 12),
                               fill='#ffffff', anchor='center')
        
        self.canvas.create_text(center_x, btc_y+60,
                               text="bc1qAnonymousFsocietyNepflo42069",
                               font=('Courier', 18, 'bold'),
                               fill='#ffff00', anchor='center')
        
        # Timer
        timer_y = btc_y + 110
        self.canvas.create_text(center_x, timer_y,
                               text="TIME UNTIL PERMANENT DELETION:",
                               font=('Courier', 14),
                               fill='#ff0040', anchor='center')
        
        self.timer_text = self.canvas.create_text(center_x, timer_y+50,
                                                 text="00:59:59",
                                                 font=('Courier', 52, 'bold'),
                                                 fill='#ff0040',
                                                 anchor='center')
        
        # Progress Bar
        bar_y = timer_y + 100
        self.canvas.create_rectangle(center_x-300, bar_y, center_x+300, bar_y+20,
                                  outline='#ff0040', fill='#0a0a0a', width=2)
        self.progress_bar = self.canvas.create_rectangle(center_x-298, bar_y+2, 
                                                       center_x+298, bar_y+18,
                                                       fill='#ff0040', outline='')
        
        # Warning
        warn_y = bar_y + 60
        self.warning_text = self.canvas.create_text(center_x, warn_y,
                                                   text="⚠ DO NOT ATTEMPT TO CLOSE THIS WINDOW ⚠\n"
                                                        "⚠ DO NOT RESTART OR SHUTDOWN ⚠",
                                                   font=('Courier', 12, 'bold'),
                                                   fill='#ff0000',
                                                   anchor='center')
        
        # Signature
        self.canvas.create_text(self.width-30, self.height-30,
                               text="[ HACKED BY NEPFLO | ANONYMOUS | FSOCIETY ]",
                               font=('Courier', 11),
                               fill='#00ff41', anchor='se')

    def start_effects(self):
        threading.Thread(target=self.animate_matrix, daemon=True).start()
        threading.Thread(target=self.glitch_effect, daemon=True).start()
        threading.Thread(target=self.pulse_timer, daemon=True).start()
        threading.Thread(target=self.update_timer, daemon=True).start()
        threading.Thread(target=self.blink_cursor, daemon=True).start()
        threading.Thread(target=self.slogan_glitch, daemon=True).start()

    def animate_matrix(self):
        def update():
            try:
                for drop in self.drops:
                    drop['y'] += drop['speed']
                    
                    if drop['y'] > self.height:
                        drop['y'] = random.randint(-500, -50)
                        drop['speed'] = random.randint(3, 12)
                        for item in drop['items']:
                            self.canvas.delete(item)
                        drop['items'] = []
                    
                    if random.random() > 0.8:
                        char = random.choice(self.chars)
                        color_idx = min(len(drop['items']) // 3, len(self.colors)-1)
                        color = self.colors[color_idx]
                        
                        item = self.canvas.create_text(drop['x'], drop['y'],
                                                      text=char, fill=color,
                                                      font=('Courier', 12))
                        drop['items'].append(item)
                        
                        if len(drop['items']) > 20:
                            old = drop['items'].pop(0)
                            self.canvas.delete(old)
                
                self.root.after(50, update)
            except:
                pass
        
        update()

    def glitch_effect(self):
        colors = ['#ff0040', '#00ff41', '#ffffff', '#ff6600', '#00ffff']
        while self.glitch_active:
            time.sleep(0.1)
            try:
                offset_x = random.choice([-3, 0, 3])
                self.canvas.coords(self.title_glitch, 
                                 self.width//2 - 3 + offset_x, 
                                 self.canvas.coords(self.title_glitch)[1])
                self.canvas.itemconfig(self.title_glitch, fill=random.choice(colors))
                
                if random.random() > 0.95:
                    original = "SYSTEM HACKED"
                    corrupted = ''.join(random.choice(['▓', '▒', '░', '█']) 
                                      if random.random() > 0.7 else c for c in original)
                    self.canvas.itemconfig(self.title_main, text=corrupted)
                    time.sleep(0.05)
                    self.canvas.itemconfig(self.title_main, text=original)
            except:
                pass

    def pulse_timer(self):
        colors = ['#ff0040', '#ff2244', '#ff4466', '#ff6688', '#ff88aa']
        idx = 0
        while True:
            try:
                self.canvas.itemconfig(self.timer_text, fill=colors[idx % len(colors)])
                idx += 1
                time.sleep(0.1)
            except:
                return

    def blink_cursor(self):
        while True:
            try:
                current = self.canvas.itemcget(self.cursor, 'fill')
                new_color = '#0a0a0a' if current == '#00ff41' else '#00ff41'
                self.canvas.itemconfig(self.cursor, fill=new_color)
                time.sleep(0.5)
            except:
                return

    def slogan_glitch(self):
        colors = ['#00ff41', '#ff0040', '#ffffff']
        while True:
            time.sleep(random.uniform(0.3, 1.5))
            try:
                item = random.choice(self.slogan_items)
                self.canvas.itemconfig(item, fill='#ffffff')
                time.sleep(0.08)
                self.canvas.itemconfig(item, fill=random.choice(colors))
            except:
                pass

    def update_timer(self):
        while self.time_left > 0:
            hours = self.time_left // 3600
            minutes = (self.time_left % 3600) // 60
            seconds = self.time_left % 60
            
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            try:
                self.canvas.itemconfig(self.timer_text, text=time_str)
                
                # Update progress bar
                progress_width = 596 * (self.time_left / 3599)
                coords = self.canvas.coords(self.progress_bar)
                self.canvas.coords(self.progress_bar, coords[0], coords[1], 
                                 coords[0] + progress_width, coords[3])
            except:
                return
            
            self.time_left -= 1
            time.sleep(1)
        
        try:
            self.canvas.itemconfig(self.timer_text, text="00:00:00", fill='#ff0000')
            self.canvas.itemconfig(self.warning_text, 
                                 text="[!] TIME EXPIRED - INITIATING WIPE SEQUENCE [!]")
        except:
            pass

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FsocietyScreen()
    app.run()
        

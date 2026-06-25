#!/usr/bin/env python3
import tkinter as tk
import time
import random
import threading

class FsocietyScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.configure(bg='black')
        self.root.attributes('-topmost', True)
        self.root.overrideredirect(True)
        
        self.width = self.root.winfo_screenwidth()
        self.height = self.root.winfo_screenheight()
        
        self.time_left = 3599
        self.glitch_active = True
        self.blink_state = True
        
        # WICHTIG: Zuerst Matrix-Rain Canvas erstellen (im Hintergrund)
        self.rain_canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.rain_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        # Dann CRT-Effekt darüber
        self.setup_crt_effect()
        
        # Dann das Main Frame (im Vordergrund)
        self.setup_ui()
        
        self.start_effects()
        
        self.root.bind('<Escape>', lambda e: self.root.destroy())
        self.root.bind('<Alt-F4>', lambda e: self.root.destroy())

    def setup_crt_effect(self):
        self.scanline_canvas = tk.Canvas(self.root, bg='black', highlightthickness=0)
        self.scanline_canvas.place(x=0, y=0, relwidth=1, relheight=1)
        
        for y in range(0, self.height, 3):
            self.scanline_canvas.create_line(0, y, self.width, y, fill='#0a0a0a', width=1)

    def setup_ui(self):
        self.main_frame = tk.Frame(self.root, bg='black')
        self.main_frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # Frame in den Vordergrund bringen (über die Canvas-Elemente)
        self.main_frame.lift()
        
        mask_ascii = """
            ████████████            
        ████░░░░░░░░░░████        
      ████░░░░░░░░░░░░░░░░████      
    ████░░░░░░░░░░░░░░░░░░░░████    
   ████░░░░░░░░░░░░░░░░░░░░░░░███   
  ████░░░░░░░░░░░░░░░░░░░░░░░░░███  
 ████░░░░░░░░░░░░░░░░░░░░░░░░░░░███ 
 ███░██░░░░░░░░░░░░░░░░░░░░░░██░███ 
███░██░░░░░░░░░░░░░░░░░░░░░░░░██░███
███░██░░░░░░░░░░░░░░░░░░░░░░░░██░███
███░██░░░░░░░░░░░░░░░░░░░░░░░░██░███
███░██░░░░░░░░░░░░░░░░░░░░░░░░██░███
 ███░██░░░░░░░░░░░░░░░░░░░░░░██░███ 
 ████░██░░░░░░░░░░░░░░░░░░░░██░████ 
  ████░██░░░░░░░░░░░░░░░░░░██░████  
   ████░██░░░░░░░░░░░░░░░░██░████   
    ████░████████████████░████    
      ████░░░░░░░░░░░░░░████      
        ████░░░░░░░░░░████        
          ██████████████          
            ██░░░░░░██            
            ██░░░░░░██            
            ██░░░░░░██            
              ██░░██              
                ████                
"""
        
        self.mask_frame = tk.Frame(self.main_frame, bg='black')
        self.mask_frame.pack(pady=(0, 20))
        
        self.mask_label = tk.Label(self.mask_frame, text=mask_ascii,
                                   font=('Courier', 8), bg='black', fg='#ff0040',
                                   justify='center', padx=10)
        self.mask_label.pack()
        
        self.slogan_frame = tk.Frame(self.main_frame, bg='black')
        self.slogan_frame.pack(pady=10)
        
        slogans = [
            "We are Anonymous.",
            "We are Legion.",
            "We do not forgive.",
            "We do not forget.",
            "Expect us."
        ]
        
        self.slogan_labels = []
        colors = ['#00ff41', '#ff0040', '#00ff41', '#ff0040', '#00ff41']
        for i, text in enumerate(slogans):
            lbl = tk.Label(self.slogan_frame, text=text,
                          font=('Courier', 14, 'bold'), bg='black', 
                          fg=colors[i])
            lbl.pack(pady=2)
            self.slogan_labels.append(lbl)
        
        sep = tk.Frame(self.main_frame, bg='#00ff41', height=2, width=600)
        sep.pack(pady=20)
        
        self.title_container = tk.Frame(self.main_frame, bg='black')
        self.title_container.pack(pady=15)
        
        self.title_bg = tk.Label(self.title_container, text="SYSTEM HACKED",
                                font=('Courier', 42, 'bold'), bg='black', fg='#ff0040')
        self.title_bg.pack()
        
        self.title_glitch1 = tk.Label(self.title_container, text="SYSTEM HACKED",
                                     font=('Courier', 42, 'bold'), bg='black', fg='#00ff41')
        self.title_glitch1.place(relx=0.5, rely=0.5, anchor='center', x=-2, y=-2)
        
        self.title_main = tk.Label(self.title_container, text="SYSTEM HACKED",
                                  font=('Courier', 42, 'bold'), bg='black', fg='#ffffff')
        self.title_main.place(relx=0.5, rely=0.5, anchor='center')
        
        self.subtitle = tk.Label(self.main_frame, 
                                 text="[!] YOUR PRIVACY HAS BEEN COMPROMISED [!]",
                                 font=('Courier', 16, 'bold'), bg='black', fg='#ff6600')
        self.subtitle.pack(pady=10)
        
        self.term_frame = tk.Frame(self.main_frame, bg='#0a0a0a', 
                                   highlightbackground='#ff0040',
                                   highlightthickness=2, padx=25, pady=20)
        self.term_frame.pack(pady=15)
        
        term_text = """>>> INITIATING SEQUENCE...
>>> BYPASSING FIREWALL... [OK]
>>> GAINING ROOT ACCESS... [OK]
>>> ENCRYPTING FILES... [OK]
>>> UPLOADING TO SERVER... [OK]

TARGET: Linux Mint Workstation
STATUS: COMPROMISED
ENCRYPTION: MILITARY-GRADE AES-256
BACKUPS: PURGED

All personal files have been encrypted.
Your documents, photos, and sensitive data
are now under our control."""
        
        self.term_label = tk.Label(self.term_frame, text=term_text,
                                   font=('Courier', 11), bg='#0a0a0a', fg='#00ff41',
                                   justify='left', padx=10, pady=10)
        self.term_label.pack()
        
        self.cursor_label = tk.Label(self.term_frame, text="_", 
                                    font=('Courier', 14, 'bold'),
                                    bg='#0a0a0a', fg='#00ff41')
        self.cursor_label.place(relx=0.95, rely=0.95, anchor='se')
        
        btc_frame = tk.Frame(self.main_frame, bg='black', padx=20, pady=10)
        btc_frame.pack(pady=15)
        
        btc_title = tk.Label(btc_frame, text="═══ PAYMENT REQUIRED ═══",
                            font=('Courier', 14, 'bold'), bg='black', fg='#ff0040')
        btc_title.pack()
        
        btc_amount = tk.Label(btc_frame, text="TRANSFER 0.5 BTC TO:",
                             font=('Courier', 12), bg='black', fg='#ffffff')
        btc_amount.pack(pady=5)
        
        self.btc_addr = tk.Label(btc_frame, 
                                text="bc1qAnonymousFsocietyNepflo42069",
                                font=('Courier', 18, 'bold'), bg='black', fg='#ffff00')
        self.btc_addr.pack(pady=5)
        
        timer_title = tk.Label(self.main_frame, text="TIME UNTIL PERMANENT DELETION:",
                              font=('Courier', 14), bg='black', fg='#ff0040')
        timer_title.pack(pady=(20, 5))
        
        self.timer_display = tk.Label(self.main_frame, text="00:59:59",
                                     font=('Courier', 56, 'bold'), bg='black', fg='#ff0040')
        self.timer_display.pack()
        
        self.progress_frame = tk.Frame(self.main_frame, bg='#ff0040', padx=2, pady=2)
        self.progress_frame.pack(pady=10)
        
        self.progress_canvas = tk.Canvas(self.progress_frame, width=596, height=21,
                                         bg='#0a0a0a', highlightthickness=0)
        self.progress_canvas.pack()
        self.progress_fill = self.progress_canvas.create_rectangle(0, 0, 596, 21,
                                                                fill='#ff0040',
                                                                outline='')
        
        self.warning = tk.Label(self.main_frame,
                                text="⚠ DO NOT ATTEMPT TO CLOSE THIS WINDOW ⚠\n"
                                     "⚠ DO NOT RESTART OR SHUTDOWN ⚠\n"
                                     "FAILURE TO COMPLY WILL RESULT IN TOTAL DATA LOSS",
                                font=('Courier', 12, 'bold'), bg='black', fg='#ff0000',
                                justify='center', pady=20)
        self.warning.pack()
        
        self.sig = tk.Label(self.root, text="[ HACKED BY NEPFLO | ANONYMOUS | FSOCIETY ]",
                            font=('Courier', 11), bg='black', fg='#00ff41',
                            anchor='se')
        self.sig.place(relx=1.0, rely=1.0, anchor='se', x=-30, y=-30)

    def start_effects(self):
        threading.Thread(target=self.heavy_glitch_effect, daemon=True).start()
        threading.Thread(target=self.matrix_rain, daemon=True).start()
        threading.Thread(target=self.pulse_timer, daemon=True).start()
        threading.Thread(target=self.update_timer, daemon=True).start()
        threading.Thread(target=self.blink_cursor, daemon=True).start()
        threading.Thread(target=self.slogan_glitch, daemon=True).start()
        threading.Thread(target=self.scanline_move, daemon=True).start()

    def heavy_glitch_effect(self):
        colors = ['#ff0040', '#00ff41', '#ffffff', '#ff6600', '#ff0000', '#00ffff', '#ffff00']
        while self.glitch_active:
            time.sleep(random.uniform(0.05, 0.15))
            try:
                x_offset = random.choice([-4, -2, 0, 2, 4])
                y_offset = random.choice([-4, -2, 0, 2, 4])
                
                self.title_glitch1.place_configure(x=-2+x_offset, y=-2+y_offset)
                self.title_bg.config(fg=random.choice(colors))
                
                if random.random() > 0.92:
                    original = "SYSTEM HACKED"
                    corrupted = ''.join(random.choice(['▓', '▒', '░', '█', '▀', '▄', '▌', '▐']) 
                                      if random.random() > 0.6 else c for c in original)
                    self.title_main.config(text=corrupted)
                    time.sleep(0.08)
                    self.title_main.config(text=original)
                    
            except:
                pass

    def slogan_glitch(self):
        colors = ['#00ff41', '#ff0040', '#ffffff']
        while True:
            time.sleep(random.uniform(0.5, 2.0))
            try:
                line = random.choice(self.slogan_labels)
                line.config(fg='#ffffff')
                time.sleep(0.1)
                line.config(fg=random.choice(colors))
            except:
                pass

    def pulse_timer(self):
        colors = ['#ff0040', '#ff2244', '#ff4466', '#ff6688', '#ff88aa', '#ff6688', '#ff4466', '#ff2244']
        idx = 0
        while True:
            try:
                self.timer_display.config(fg=colors[idx % len(colors)])
                idx += 1
                time.sleep(0.1)
            except:
                return

    def blink_cursor(self):
        while True:
            try:
                self.cursor_label.config(fg='#0a0a0a' if self.blink_state else '#00ff41')
                self.blink_state = not self.blink_state
                time.sleep(0.5)
            except:
                return

    def scanline_move(self):
        scanline = self.scanline_canvas.create_rectangle(0, 0, self.width, 8,
                                                        fill='#00ff41', 
                                                        stipple='gray50',
                                                        outline='')
        y = 0
        while True:
            try:
                y = (y + 8) % self.height
                self.scanline_canvas.coords(scanline, 0, y, self.width, y+8)
                time.sleep(0.015)
            except:
                return

    def matrix_rain(self):
        # Verwende das bereits erstellte rain_canvas
        chars = "日ﾊﾐﾋｰｳｼﾅﾓﾆｻﾜﾂｵﾘｱﾎﾃﾏｹﾒｴｶｷﾑﾕﾗｾﾈｽﾀﾇﾍ0123456789:><[]{}|\\"
        colors = ['#00ff41', '#00dd33', '#00bb22', '#009911', '#007700', '#005500', '#003300']
        drops = []
        
        for x in range(0, self.width, 18):
            drops.append({
                'x': x,
                'y': random.randint(-1500, 0),
                'speed': random.randint(4, 20),
                'chars': [],
                'length': random.randint(8, 30)
            })
        
        def animate():
            try:
                for drop in drops:
                    drop['y'] += drop['speed']
                    
                    if drop['y'] > self.height:
                        drop['y'] = random.randint(-500, -50)
                        drop['speed'] = random.randint(4, 20)
                        for char_id in drop['chars']:
                            self.rain_canvas.delete(char_id)
                        drop['chars'] = []
                    
                    if random.random() > 0.75:
                        char = random.choice(chars)
                        color_idx = min(len(drop['chars']), len(colors)-1)
                        color = colors[color_idx]
                        
                        text_id = self.rain_canvas.create_text(drop['x'], drop['y'], 
                                                          text=char, fill=color,
                                                          font=('Courier', 12))
                        drop['chars'].append(text_id)
                        
                        if len(drop['chars']) > drop['length']:
                            old_id = drop['chars'].pop(0)
                            self.rain_canvas.delete(old_id)
                            
            except:
                pass
            
            self.root.after(40, animate)
        
        animate()

    def update_timer(self):
        while self.time_left > 0:
            hours = self.time_left // 3600
            minutes = (self.time_left % 3600) // 60
            seconds = self.time_left % 60
            
            time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
            try:
                self.timer_display.config(text=time_str)
                progress = 596 * (self.time_left / 3599)
                self.progress_canvas.coords(self.progress_fill, 0, 0, progress, 21)
            except:
                return
            
            self.time_left -= 1
            time.sleep(1)
        
        try:
            self.timer_display.config(text="00:00:00", fg='#ff0000')
            self.warning.config(text="[!] TIME EXPIRED - INITIATING WIPE SEQUENCE [!]", 
                              fg='#ff0000')
        except:
            pass

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = FsocietyScreen()
    app.run()

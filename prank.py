#!/usr/bin/env python3
import tkinter as tk
import time
import threading

class RansomScreen:
    def __init__(self):
        self.root = tk.Tk()
        self.root.attributes('-fullscreen', True)
        self.root.attributes('-topmost', True)
        self.root.configure(bg='#050505')
        self.root.config(cursor='none')
        
        self.time_left = 3599
        
        self.root.bind('<Alt-F4>', lambda e: self.root.destroy())
        self.root.bind('<Escape>', lambda e: self.root.destroy())
        
        self.setup_ui()
        self.start_timer()
        
    def setup_ui(self):
        frame = tk.Frame(self.root, bg='#050505')
        frame.place(relx=0.5, rely=0.5, anchor='center')
        
        # DETAILREICHE MASKE (Peak ASCII Art)
        mask = """
         ⠀⠀⠀⠀⠀⣀⣤⣶⣶⣶⡾⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠿⠶⢶⣶⣶⣶⣶⣶⣦⣤⣤⣤⣀⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⢀⣼⡿⠛⠁⠀⠀⠀⠀⢀⣠⣴⡶⠾⠛⠛⠛⠛⠛⠛⠛⠛⠒⠶⠶⠶⢤⣤⣤⣬⣭⣭⣽⡿⠟⠻⠿⣶⣦⣄⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⣠⣿⠏⠀⠀⠀⠀⢀⣴⡾⢟⣩⣥⡶⠶⠞⠛⠛⠛⠛⠛⠿⠶⠶⢶⣶⣶⣶⣶⣤⣤⣤⣶⠶⠶⠶⠶⠶⠆⠉⠛⢿⣦⣄⠀⠀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀⠀⣠⣴⠟⣩⣴⠟⣉⡤⠴⠖⠒⠛⠛⠛⠛⢳⡀⠀⠀⠀⠀⠀⠀⠀⢀⣠⡤⠤⠤⠤⢤⣄⡀⠀⠀⠀⠀⠈⠻⣷⡀⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀⠀⠸⠋⣠⡾⠋⣠⣾⡥⠶⠒⠛⢻⠛⠓⠒⠶⢤⣵⡀⠀⠀⠀⠀⠀⠀⠈⣠⠀⠀⠀⠀⠀⠀⠉⢳⡄⠀⠀⠀⠀⢹⣷⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⣰⣿⠃⠀⠀⠀⠀⠀⠀⠉⢀⡾⠋⠉⠓⠄⠀⠀⠈⠀⠀⠀⢀⡼⠉⠙⢦⡀⠀⠀⠀⠀⢰⠃⣀⡤⠶⢲⠛⠛⠛⠛⠛⠳⠶⣤⡀⠀⣿⡇⠀⠀⠀⠀
⠀⠀⠀⠀⣠⣾⣿⠃⠀⠀⠀⠀⠀⠀⠀⣠⡟⠈⠦⠤⠀⠀⣴⣿⣿⣿⣷⣆⠀⠈⣀⡴⠚⣿⡄⠀⠀⠀⢀⣗⠉⠀⠀⠀⠃⢀⣀⣁⡀⠀⠐⠈⠙⢦⠹⣿⣆⠀⠀⠀
⠀⠀⢀⣴⡿⢿⣷⠶⠖⠒⠒⠂⠀⠀⠻⢻⣇⠀⠁⠀⠀⠘⢿⣿⣿⣿⣿⡟⠀⠀⣋⣀⣀⣼⠇⠀⣠⣤⣾⠀⠑⠄⠀⠀⣴⣿⣿⣿⣿⡆⠀⠀⠀⢸⣧⡈⠻⣷⡄⠀
⠀⢠⣿⢟⡴⠋⠀⣠⣶⡿⠿⠿⢿⣦⣤⣈⠻⣦⣀⡔⠒⠄⠀⠉⠉⠉⠁⠀⣀⠀⠉⢀⣼⠟⠀⠀⠈⠙⢿⣄⠀⠀⠀⠀⠈⠻⠿⠿⠟⠁⠀⠠⠃⡼⢧⡉⢦⠹⣿⡀
⠀⣿⡏⢸⠇⠀⣼⡟⠁⠀⠀⣦⡀⠈⠙⠻⠃⠈⠙⠳⢦⣤⣼⣉⣓⣈⣉⣉⣤⡽⠿⠛⠁⠀⠀⠀⠀⠀⢸⡟⠲⢖⣁⠀⠢⡤⠀⠐⠒⣄⣀⡴⠾⢷⠀⢷⠀⢧⣿⡇
⢸⣿⠀⢸⡄⢰⣿⠀⠀⠀⣰⣿⣿⣦⣄⠀⠀⠀⠀⠀⠀⠀⠈⠉⠉⠉⠉⠁⣀⣤⣄⠀⠀⠀⠀⠀⠀⠀⠘⢿⣦⣄⠈⠉⠉⠉⠉⠉⠉⠉⣴⡄⠀⠀⠀⣸⠀⡜⣿⡇
⠸⣿⡄⢸⡇⢸⣿⠀⠾⠿⢿⣇⠀⠉⠛⢿⣶⣤⣀⠀⠀⠀⠒⠒⠒⠒⠚⢱⡟⠉⠉⣀⣀⣀⠀⠀⠀⠀⠀⠀⢙⣿⣷⣀⠀⠀⠀⠀⠀⠀⣿⣧⡀⠀⡴⠋⢠⢣⣿⠃
⠀⢿⣧⠸⣇⠀⢿⡆⠀⠀⠈⣿⣦⡀⠀⠀⠈⢻⡿⠿⣷⣦⣤⣀⡀⠀⠀⠈⣿⡄⠸⠏⠉⠻⠗⠀⠀⠀⠀⣠⣾⠏⠙⠀⠉⠲⠤⠀⠀⣼⣿⣿⣇⢀⡤⠖⢁⣾⠏⠀
⠀⠈⢿⣧⡈⠳⢤⡀⠀⠀⠀⢹⣿⣿⣶⣄⡀⢸⣧⡀⠀⠈⠉⠛⠻⢿⣶⣦⣌⣁⡀⠀⠀⠀⠀⠀⠰⢶⣾⠿⠋⠀⠀⠀⠀⠀⣀⣴⣿⠛⢻⣿⣿⠀⠀⢀⣾⠏⠀⠀
⠀⠀⠀⠙⣿⣆⠀⠀⠀⠀⠀⢸⣿⣿⣿⣿⣿⣿⣿⣷⣦⣀⠀⠀⠀⠀⣿⠏⠉⠛⠛⠻⠿⣶⣶⣶⣶⣤⣤⣤⣤⣴⣶⣶⠿⣿⠋⠁⢻⡆⠘⣿⣿⡄⠀⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠈⢻⣧⡀⠀⠀⠀⠀⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣦⣴⣿⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠀⠉⢿⠉⠀⠀⠀⠀⣿⡀⠀⣸⣧⣴⣿⣿⡇⠀⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠀⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣶⣶⣶⣤⣼⣿⣤⣤⣤⣤⣾⣦⣤⣤⣴⣶⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⢻⣷⡀⠀⠀⠸⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡇⠀⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠻⣷⣄⠀⠀⢻⣿⠿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣷⣄⠀⢻⣧⡀⠙⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠙⢿⣦⡀⠹⣷⣄⢀⣿⠉⠙⠻⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⠀⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠹⣿⣄⠈⠻⣿⣏⠀⠀⠀⠀⠈⠙⣿⡿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⠀⢸⣿⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⢿⣧⡀⠈⠻⣦⣄⠀⠀⠀⢀⣿⠁⠀⠀⠉⠙⠻⢿⣿⢿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⣿⡿⢻⡇⠀⢸⣿⡇⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠻⣿⣄⠀⠈⠛⢷⣤⣀⣼⡏⠀⠀⠀⠀⠀⠀⢸⣿⠀⠀⠈⠉⢹⣿⠉⠉⠙⣿⡟⠉⣽⡟⠀⣿⣁⣿⠁⠀⢸⣿⠃⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠻⣷⣄⠀⠀⠉⠛⠿⣷⣦⣄⣀⡀⠀⠀⢸⣿⠀⠀⠀⠀⣾⡏⠀⠀⢠⣿⠀⣠⣿⣥⣴⣾⡿⠁⠀⠀⣾⡟⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⢿⣦⣄⡀⠀⠀⠉⠛⠛⠿⠿⢿⣿⣿⣶⣶⣶⣶⣿⡷⠶⠶⠾⠿⠿⠟⠛⠛⠋⠁⠀⠀⢀⣼⡟⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠛⠻⢿⣶⣦⣤⣄⣀⡀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⣀⣀⣀⣤⣴⡾⠋⠀⠀⠀⠀⠀
⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠀⠈⠉⠛⠛⠿⠿⠿⠿⢿⣷⣶⣶⣶⣶⣶⣶⣾⣿⣿⡿⠿⠿⠿⠟⠛⠉⠁⠀⠀⠀⠀⠀⠀⠀               
                   
"""
        
        # Logo Container
        logo_frame = tk.Frame(frame, bg='#050505')
        logo_frame.pack(pady=(0, 20))
        
        tk.Label(logo_frame, text=mask, font=('Courier', 7), 
                bg='#050505', fg='#ff0040', justify='center').pack()
        
        # FSOCIETY Text unter der Maske
        tk.Label(frame, text="F S O C I E T Y", 
                font=('Courier', 24, 'bold'), 
                bg='#050505', fg='#ffffff').pack(pady=(0, 10))
        
        # Slogan
        slogan = """We are Anonymous.
We are Legion.
We do not forgive.
We do not forget.
Expect us."""
        
        tk.Label(frame, text=slogan, font=('Courier', 12), 
                bg='#050505', fg='#00aa00', justify='center').pack(pady=15)
        
        # Trennlinie
        tk.Frame(frame, bg='#333333', height=1, width=600).pack(pady=20)
        
        # Ransom Info
        tk.Label(frame, text="YOUR FILES HAVE BEEN ENCRYPTED", 
                font=('Consolas', 26, 'bold'), 
                bg='#050505', fg='#ff0000').pack(pady=(0, 15))
        
        info = """All files have been encrypted with military-grade AES-256.

To restore your files, send 0.5 BTC to:"""
        
        tk.Label(frame, text=info, font=('Consolas', 12), 
                bg='#050505', fg='#aaaaaa', justify='center').pack()
        
        # Bitcoin
        tk.Label(frame, text="bc1qNepfloH4ck3dPr4nk42069xXxX", 
                font=('Consolas', 18, 'bold'), 
                bg='#050505', fg='#ffff00').pack(pady=15)
        
        # Timer
        self.timer_label = tk.Label(frame, text="00:59:59", 
                                   font=('Consolas', 56, 'bold'), 
                                   bg='#050505', fg='#ff0000')
        self.timer_label.pack(pady=10)
        
        tk.Label(frame, text="Time until decryption key is destroyed", 
                font=('Consolas', 11), bg='#050505', fg='#666666').pack()
        
        # Warning
        tk.Label(frame, text="DO NOT CLOSE THIS WINDOW", 
                font=('Consolas', 14, 'bold'), 
                bg='#050505', fg='#ff0000').pack(pady=30)
        
        # ID
        tk.Label(self.root, text="ID: NEPFLO-ANON-77X", 
                font=('Courier', 10), bg='#050505', fg='#222222').place(
                relx=1.0, rely=1.0, anchor='se', x=-30, y=-30)

    def start_timer(self):
        def update():
            while self.time_left > 0:
                hours = self.time_left // 3600
                minutes = (self.time_left % 3600) // 60
                seconds = self.time_left % 60
                
                time_str = f"{hours:02d}:{minutes:02d}:{seconds:02d}"
                try:
                    self.timer_label.config(text=time_str)
                except:
                    return
                
                self.time_left -= 1
                time.sleep(1)
            
            try:
                self.timer_label.config(text="00:00:00", fg='#660000')
            except:
                pass
        
        threading.Thread(target=update, daemon=True).start()

    def run(self):
        self.root.mainloop()

if __name__ == "__main__":
    app = RansomScreen()
    app.run()

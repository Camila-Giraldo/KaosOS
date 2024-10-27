import customtkinter as ck
from PIL import Image, ImageTk
import os
import subprocess
from datetime import datetime

images_path = os.path.join(os.path.dirname(__file__), "images")
programs_path = os.path.join(os.path.dirname(__file__), "Programs")

class DesktopFrame(ck.CTkFrame):
    def __init__(self, master):
        super().__init__(master)
        self.configure(bg_color="black")
        screen_width = master.winfo_screenwidth()
        screen_height = master.winfo_screenwidth()

        # Background image
        bg_img = Image.open(os.path.join(images_path, "desktop.png")).resize((screen_width, screen_height), Image.LANCZOS)
        background = ImageTk.PhotoImage(bg_img)
        ck.CTkLabel(self, image=background, text="").place(x=0, y=0, relwidth=1, relheight=1)

        # Icons and programs
        self.programs = Programs()
        icons_frame = ck.CTkFrame(self, corner_radius=2, bg_color="#000000")
        icons_frame.pack(side="bottom")
        icons_data = [
            ("power-button.png", self.quit),
            ("calculator.png", self.programs.calculator),
            ("calendar.png", self.programs.calendar),
            ("text_editor.png", self.programs.text_editor),
            ("explorer.png", self.programs.explorer),
        ]
        for icon_name, action in icons_data:
            img = ck.CTkImage(Image.open(os.path.join(images_path, icon_name)).resize((30, 30)), size=(30, 30))
            ck.CTkButton(
                icons_frame, 
                image=img, 
                text="", 
                command=action, 
                fg_color="white", 
                hover_color="gray",
                width= 30
                ).pack(side="left", padx=5, pady=5)

        # Clock frame
        self.frame_clock = ck.CTkFrame(self, width=100, height=100, bg_color="black", corner_radius=2)
        self.frame_clock.pack(side="top", anchor="n", padx=10, pady=10)
        self.clock_label = ck.CTkLabel(self.frame_clock, font=("Whisper", 30))
        self.clock_label.pack()
        self.time_update()
        

    def time_update(self):
        current_time = datetime.now().strftime("%H:%M")
        self.clock_label.configure(text=current_time)
        self.after(1000, self.time_update)


class Programs:
    def calculator(self):
        subprocess.Popen(["python", os.path.join(programs_path, "calculator.py")])

    def calendar(self):
        subprocess.Popen(["python", os.path.join(programs_path, "calendar.py")])

    def explorer(self):
        subprocess.Popen(["python", os.path.join(programs_path, "explorer.py")])

    def text_editor(self):
        subprocess.Popen(["python", os.path.join(programs_path, "text_editor.py")])

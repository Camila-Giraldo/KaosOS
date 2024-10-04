# Global configuration
from datetime import datetime
import customtkinter as ck
import os
import subprocess
from PIL import Image, ImageTk
from data import principal_access as access

# Routes
principal_path = os.path.dirname(__file__)
images_path = os.path.join(principal_path, "images")
programs_path = os.path.join(principal_path, "../Programs")

ck.set_appearance_mode("system")
ck.set_default_color_theme("blue")


class Login:
    def __init__(self):
        """
        Principal screen creation for OS
        """
        self.root = ck.CTk()
        self.root.title("KAOS")
        self.root.iconbitmap(os.path.join(images_path, "logo.ico"))
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()

        # Window configuration to fill the entire screen
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        # Lock screen resizing
        self.root.resizable(False, False)

        # Image-logo loading
        logo = ck.CTkImage(
            light_image=Image.open(os.path.join(images_path, "Kaos.png")),
            dark_image=Image.open(os.path.join(images_path, "Kaos.png")),
            size=(420, 280),
        )

        # Image-user loading

        img_user = ck.CTkImage(
            light_image=Image.open(os.path.join(images_path, "user.png")),
            dark_image=Image.open(os.path.join(images_path, "user.png")),
            size=(180, 180),
        )

        # Image-power loading
        img_pwr = ck.CTkImage(
            light_image=Image.open(os.path.join(images_path, "power-button.png")),
            dark_image=Image.open(os.path.join(images_path, "power-button.png")),
            size=(35, 35),
        )

        # Tag to show the image-logo
        tag_logo = ck.CTkLabel(master=self.root, image=logo, text="")

        # Tag to show the image-user
        tag_user = ck.CTkLabel(master=self.root, image=img_user, text="")

        # Tag to show the image-power
        tag_pwr = ck.CTkLabel(master=self.root, image=img_pwr, text="")

        tag_logo.pack()
        tag_user.pack()

        # Login part
        ck.CTkLabel(self.root, text="User").pack()
        self.user = ck.CTkEntry(self.root)
        self.user.insert(0, "Username")
        self.user.bind("<Button-1>", lambda e: self.user.delete(0, "end"))
        self.user.pack()

        # Password
        ck.CTkLabel(self.root, text="Password").pack()
        self.password = ck.CTkEntry(self.root, show="*")
        self.password.insert(0, "*******")
        self.password.bind("<Button-1>", lambda e: self.password.delete(0, "end"))
        self.password.pack()

        ck.CTkButton(self.root, text="Sign in", command=self.validate).pack(pady=10)

        ck.CTkButton(
            self.root,
            image=img_pwr,
            text="",
            fg_color="transparent",
            hover=False,
            command=self.shutting_down,
        ).pack(side=ck.RIGHT, padx=15, pady=15)

        self.root.mainloop()

    def validate(self):
        """
        Validating the login information
        """
        get_user = self.user.get()
        get_password = self.password.get()

        if get_user != access["user"] or get_password != access["password"]:
            if hasattr(self, "info_login"):
                self.info_login.destroy()
            self.info_login = ck.CTkLabel(self.root, text="User or password incorrect")
            self.info_login.pack()
        else:
            if hasattr(self, "info_login"):
                self.info_login.destroy()

            self.info_login = ck.CTkLabel(
                self.root, text=f"Hello, {get_user}. Wait a moment.."
            )
            self.info_login.pack()

            self.root.destroy()
            
            desktop = Desktop()

    def shutting_down(self):
        """
        Function to shutting down the OS
        """
        self.root.destroy()
        
class Programs:
    def calculator(self):
        route = os.path.join(programs_path, 'calculator.py')
        subprocess.Popen(["python", route])
    
    def calendar(self):
        route = os.path.join(programs_path, 'calendar.py')
        subprocess.Popen(["python", route])
    
    def explorer(self):
        route = os.path.join(programs_path, 'explorer.py')
        subprocess.Popen(["python", route])
    
    def text_editor(self):
        route = os.path.join(programs_path, 'text_editor.py')
        subprocess.Popen(["python", route])
        

programs = Programs()


class Desktop:
    def __init__(self) -> None:
        self.root = ck.CTk()
        self.root.title("Desktop")
        screen_width = self.root.winfo_screenwidth()
        screen_height = self.root.winfo_screenheight()
        
        bg_img = Image.open(os.path.join(images_path, "desktop.png"))
        bg_img = bg_img.resize((screen_width, screen_height), Image.LANCZOS)
        background = ImageTk.PhotoImage(bg_img)
        
        self.root.geometry(f"{screen_width}x{screen_height}+0+0")
        
        bg_label = ck.CTkLabel(self.root, image=background, text="")
        bg_label.place(x = 0, y = 0, relwidth = 1, relheight = 1)
        
        self.buttons_frame = ck.CTkFrame(self.root, corner_radius = 1)
        self.buttons_frame.configure(bg_color = "#000000")
        self.buttons_frame.pack(side = "bottom")
        
        self.icons = [
            (Image.open((os.path.join(images_path, 'power-button.png'))).resize((35, 35)), lambda: self.shutting_down()),
            (Image.open((os.path.join(images_path, 'calculator.png'))).resize((35, 35)), lambda: programs.calculator()),
            (Image.open((os.path.join(images_path, 'calendar.png'))).resize((35, 35)), lambda: programs.calendar()),
            (Image.open((os.path.join(images_path, 'text_editor.png'))).resize((35, 35)), lambda: programs.text_editor()),
            (Image.open((os.path.join(images_path, 'explorer.png'))).resize((35, 35)), lambda: programs.explorer()),
        ]
        
        images_tk = [ImageTk.PhotoImage(image) for image, _ in self.icons]
        
        for i, (images_tk, action) in enumerate(zip(images_tk, (action for _, action in self.icons))):
            button = ck.CTkButton(
                master = self.buttons_frame,
                image = images_tk,
                text = "",
                command = action,
                fg_color = 'white',
                hover_color='gray'
            )
            button.configure(width = images_tk.width(), height = images_tk.height())
            button.pack(side = 'left', padx = 5, pady = 5) 
        
        self.frame_clock = ck.CTkFrame(self.root, width=100, height=100, bg_color="black", corner_radius=2)
        self.frame_clock.pack(side="top", anchor="n", padx = 0, pady= 0)
        
        self.clock_label = ck.CTkLabel(self.frame_clock, font=("Whisper", 30))
        self.clock_label.pack()
        
        self.time_update()
        
    def time_update(self):
        actual_time = datetime.now().strftime("%H:%M")
        self.clock_label.configure(text=actual_time)
        self.root.after(1000, self.time_update)
        self.root.mainloop()
    
    def shutting_down(self):
        """
        Function to shutting down the OS
        """
        self.root.destroy()

Login()

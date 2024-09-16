# Global configuration
import customtkinter as ck
import os
from PIL import Image
from data import principal_access as access 

# Routes
principal_path = os.path.dirname(__file__)
images_path = os.path.join(principal_path, "images")
programs_path = os.path.join(principal_path, "../Programs")

ck.set_appearance_mode("system")
ck.set_default_color_theme("blue")

class Login():
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
            light_image = Image.open(os.path.join(images_path, "Kaos.png")),
            dark_image = Image.open(os.path.join(images_path, "Kaos.png")),
            size = (420, 280)
        )
        
        # Image-user loading
        
        img_user = ck.CTkImage(
            light_image = Image.open(os.path.join(images_path, "user.png")),
            dark_image = Image.open(os.path.join(images_path, "user.png")),
            size=(180, 180)
        )
        
        # Image-power loading
        img_pwr = ck.CTkImage(
            light_image = Image.open(os.path.join(images_path, "power-button.png")),
            dark_image = Image.open(os.path.join(images_path, "power-button.png")),
            size = (35, 35)
        )
        
        # Tag to show the image-logo
        tag_logo = ck.CTkLabel(
            master = self.root,
            image = logo,
            text = ""
        )
        
        # Tag to show the image-user
        tag_user = ck.CTkLabel(
            master = self.root,
            image = img_user,
            text = ""
        )
        
        # Tag to show the image-power
        tag_pwr = ck.CTkLabel(
            master = self.root,
            image = img_pwr,
            text = ""
        )
        
        tag_logo.pack()
        tag_user.pack()
        
        # Login part
        ck.CTkLabel(self.root, text="User").pack()
        self.user = ck.CTkEntry(self.root)
        self.user.insert(0, "Username")
        self.user.bind("<Button-1>", lambda e: self.user.delete(0, 'end'))
        self.user.pack()
        
        # Password
        ck.CTkLabel(self.root, text="Password").pack()
        self.password = ck.CTkEntry(self.root, show="*")
        self.password.insert(0, "*******")
        self.password.bind("<Button-1>", lambda e: self.password.delete(0, 'end'))
        self.password.pack()
        
        ck.CTkButton(self.root, text="Sign in", command=self.validate).pack(pady=10)
        
        ck.CTkButton(
            self.root, 
            image=img_pwr, 
            text = "", 
            fg_color="transparent", 
            hover = False,
            command=self.shutting_down
        ).pack(side=ck.RIGHT, padx= 15, pady = 15)
        
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
            self.info_login = ck.CTkLabel(self.root, text = "User or password incorrect")
            self.info_login.pack()
        else:
            if hasattr(self, "info_login"):
                self.info_login.destroy() 
            
            self.info_login = ck.CTkLabel(self.root, text=f"Hello, {get_user}. Wait a moment..")
            self.info_login.pack()
            
            self.root.destroy()
    
    def shutting_down(self):
        """
        Function to shutting down the OS
        """
        self.root.destroy()
        
        
Login()
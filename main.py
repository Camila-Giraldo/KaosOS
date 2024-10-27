import customtkinter as ck
from login_frame import LoginFrame
from desktop_frame import DesktopFrame

class MainApp(ck.CTk):
    def __init__(self):
        super().__init__()
        self.title("KAOS")
        self.geometry(f"{self.winfo_screenwidth()}x{self.winfo_screenheight()}+0+0")
        self.resizable(True, True)

        # Instanciar los frames
        self.login_frame = LoginFrame(self, self.switch_frame)
        self.desktop_frame = DesktopFrame(self)

        # Mostrar el frame de inicio de sesión al inicio
        self.login_frame.pack(fill="both", expand=True)

    def switch_frame(self, frame_name):
        """Switch to the desired frame based on frame_name."""
        if frame_name == "desktop":
            self.login_frame.pack_forget()  # Oculta el marco de inicio de sesión
            self.desktop_frame.pack(fill="both", expand=True)  # Muestra el marco de escritorio
        elif frame_name == "login":
            self.desktop_frame.pack_forget()  # Oculta el marco de escritorio
            self.login_frame.pack(fill="both", expand=True)

    def show_frame(self, frame_name):
        frame = self.frames[frame_name]
        frame.tkraise()


if __name__ == "__main__":
    app = MainApp()
    app.mainloop()

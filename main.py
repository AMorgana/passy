import customtkinter as ctk

# Set the theme and color
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PassphraseApp(ctk.CTk):
    def __init__(self):
        super().__init__()

        # 1. Main Window Setup
        self.title("Passy")
        self.geometry("700x450")

        # This makes the middle part of the app stretch if we resize it
        self.grid_columnconfigure(0, weight=1)
        self.grid_rowconfigure(2, weight=1)

        # 2. Creating the Containers (Frames)
        # Header Frame (Navigation)
        self.header_frame = ctk.CTkFrame(self, fg_color="transparent")
        self.header_frame.grid(row=0, column=0, padx=20, pady=10, sticky="nsew")

        # Result Frame (The big password display)
        self.result_frame = ctk.CTkFrame(self, corner_radius=10)
        self.result_frame.grid(row=1, column=0, padx=20, pady=10, sticky="nsew")

        # Options Frame (Sliders, Checks, etc.)
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")

if __name__ == "__main__":
    app = PassphraseApp()
    app.mainloop()
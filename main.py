import customtkinter as ctk
# import generator as gen

# Set the theme and color
ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")

class PassphraseApp(ctk.CTk):
    def update_slider_label(self, value):
        self.words_entry.delete(0, "end")
        self.words_entry.insert(0, int(value))

    def update_slider_from_entry(self, value):
        try:
            user_input = self.words_entry.get()
            new_val = int(user_input)

            # clamp values between 2-20
            clamped_val = max(2, min(new_val,20))

            #update slider and the entry box with appropriate value
            self.words_slider.set(clamped_val)
            self.words_entry.delete(0, "end")
            self.words_entry.insert(0, str(clamped_val))

        except ValueError:
            # if a letter is typed, reset box to whatever slide is at
            current_slider_val = int(self.words_slider.get())
            self.words_entry.delete(0, "end")
            self.words_entry.insert(0,str(current_slider_val))

    def __init__(self):
        super().__init__()
        #set font
        self.main_font = ctk.CTkFont(family="Arial", size=30)
        # 1. Main Window Setup
        self.title("Passy")
        self.geometry("900x750")

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

        # The Passphrase Display
        self.passphrase_entry = ctk.CTkEntry(self.result_frame, font=self.main_font, height=60)
        self.passphrase_entry.grid(row=0, column=0, padx=(20, 10), pady=10, sticky="ew")

        # copy button
        self.copy_btn = ctk.CTkButton(self.result_frame, text="Copy", width=60, height=60)
        self.copy_btn.grid(row=0, column=1, padx=(5, 20), pady=20, sticky="e")

        # The Generate Button
        self.generate_btn = ctk.CTkButton(self.result_frame, text="Generate", font=self.main_font,height=50, width=150, corner_radius=25)
        self.generate_btn.grid(row=1, column=0, columnspan=2, padx=(20,20), pady=(5,20), sticky="nsew")

        self.result_frame.grid_columnconfigure(0, weight=1)

        # Options Frame (Sliders, Checks, etc.)
        self.options_frame = ctk.CTkFrame(self)
        self.options_frame.grid(row=2, column=0, padx=20, pady=20, sticky="nsew")
        self.options_frame.grid_columnconfigure(1, weight=1)
        # A.1 Number of Words Label
        self.words_label = ctk.CTkLabel(self.options_frame, text="Number of words:", font=self.main_font)
        self.words_label.grid(row=0, column=0, padx = 10, pady = 10, sticky="w")

        # A.2 Number of Words Slider
        # set the min and max words
        self.words_slider = ctk.CTkSlider(self.options_frame, from_=2, to=20, number_of_steps=18, command=self.update_slider_label)
        self.words_slider.grid(row=0, column=1, padx = 10, pady = 10, sticky="ew")
        self.words_slider.set(4)

        # A.3 The value Label Column 2
        self.words_entry = ctk.CTkEntry(self.options_frame, width=50, font=("Arial", 24))
        self.words_entry.grid(row=0, column=2, padx = 10, pady = 10)
        self.words_entry.insert(0, "4") #set initial value
        self.words_entry.bind("<Return>", self.update_slider_from_entry)
        self.words_entry.bind("<FocusOut>", self.update_slider_from_entry)

        # B.1 Word Separator Label (column 0
        self.separator_label = ctk.CTkLabel(self.options_frame, text="Word Separator:", font=self.main_font)
        self.separator_label.grid(row=1, column=0, padx = 20, pady = 10, sticky="w")

        # B.2 Word separator entry (Columns 1 and 2)
        self.separator_entry = ctk.CTkEntry(self.options_frame, width=50, font=self.main_font)
        self.separator_entry.grid(row=1, column=1, columnspan=2,padx = 10, pady = 10, sticky="ew")

        # Immediately set defaults
        self.separator_entry.insert(0, "!@#$%^&*-")

        # C Complexity toggles
        # C.1 Only use one special symbol?
        self.single_symbol_cb = ctk.CTkCheckBox(self.options_frame, text=" Only use a Single Symbol",
                                                font=self.main_font)
        self.single_symbol_cb.grid(row=2, column=0, columnspan=3, padx=10, pady=10, sticky="w")

        # C.2 include a random 0-9 digit
        self.number_cb = ctk.CTkCheckBox(self.options_frame, text=" Include Number", font=self.main_font)
        self.number_cb.grid(row=3, column=1, padx = 10, pady = 10, sticky="w")

        # C.3 capitalize a random word
        self.capitalize_cb = ctk.CTkCheckBox(self.options_frame, text=" Capitalize", font=self.main_font)
        self.capitalize_cb.grid(row=3, column=0, padx = 10, pady = 10, sticky="w")


if __name__ == "__main__":
    app = PassphraseApp()
    app.mainloop()
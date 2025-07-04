import customtkinter

# App setup
app = customtkinter.CTk()
app.geometry('1920x1080')
app.title('21-Companion')

# Optional dark/light theme
customtkinter.set_appearance_mode("dark")  # or "light"
customtkinter.set_default_color_theme("blue")  # green, dark-blue, etc.

# Main frame for content
main_frame = customtkinter.CTkFrame(app)
main_frame.pack(expand=True)

# Title label
title_label = customtkinter.CTkLabel(main_frame, text="21-Companion", font=("Arial", 48))
title_label.pack(pady=40)

# Buttons
def start_button_pressed():
    print("Start clicked!")

def settings_button_pressed():
    print("Settings clicked!")

def quit_button_pressed():
    app.quit()

def player_options_button_pressed():
    print("Player options clicked!")

# Add buttons
start_btn = customtkinter.CTkButton(main_frame, text="Start", width=200, height=50, command=start_button_pressed)
start_btn.pack(pady=20)

settings_btn = customtkinter.CTkButton(main_frame, text="Settings", width=200, height=50, command=settings_button_pressed)
settings_btn.pack(pady=20)

player_options_button = customtkinter.CTkButton(main_frame, text="Players", width=200, height=50, command=player_options_button_pressed)
player_options_button.pack(pady=20)

quit_btn = customtkinter.CTkButton(main_frame, text="Quit", width=200, height=50, command=quit_button_pressed)
quit_btn.pack(pady=20)

# Run the app
app.mainloop()

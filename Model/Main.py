import time
import tkinter as tk
from tkinter import ttk, messagebox
import pyautogui as cur
import Opener1

# Data for ComboBoxes
browsers = ['Chrome', 'Brave']
modes = ['Light', 'Dark']
sizes = {
    "1920x1080":[712,181,1664,942],
    "1366x768":[488,166,1309,643]
         }

def start_action(event=None):
    mode = 'light'
    browser = 'chrome'
    num = -1
    res = size_combo.get()
    inp = user_entry.get()  # Get user input
    mode = theme_combos.get().lower()  # Get selected theme
    browser = browser_combos.get().lower()  # Get selected browser
    print(inp, mode, browser, res)

    if inp.isdigit():  # Check if input is a valid number
        inp = int(inp)
        if inp > 0 and inp < 100:
            num = inp
            if mode != "select theme" and browser != "select browser" and res != "Select Screen Size":
                Opener1.open_web(browser)
                for i in range(inp):
                    Opener1.full_process(sizes[res],mode)
                    time.sleep(3)
            else:
                messagebox.showwarning("Select", "Select Theme and Browser and Screen Resolution")
        else:
            messagebox.showwarning("Caution", "Enter a valid number between 1 and 99")
            return
    else:
        messagebox.showwarning("Non-Numeric Value!", "Enter a Whole Number")
        return


# Create the main window
root = tk.Tk()
root.title("ChatMaster")
root.geometry("500x450")  # Set the initial window size
root.config(bg="#f1f1f1")  # Set background color

# Create a frame to hold the widgets for a clean layout
frame = tk.Frame(root, bg="#f1f1f1")
frame.pack(fill="both", expand=True, padx=20, pady=20)

# Configure columns and rows to expand
frame.grid_columnconfigure(0, weight=1, uniform="equal")
frame.grid_columnconfigure(1, weight=3, uniform="equal")
frame.grid_rowconfigure(0, weight=1, uniform="equal")
frame.grid_rowconfigure(1, weight=1, uniform="equal")
frame.grid_rowconfigure(2, weight=1, uniform="equal")
frame.grid_rowconfigure(3, weight=1, uniform="equal")

# Labels for User Input
label_user = tk.Label(frame, text="Enter a Number (1-99):", font=("Helvetica", 12), bg="#f1f1f1")
label_user.grid(row=0, column=0, sticky="w", pady=10, padx=10)

# User input entry field
user_entry = tk.Entry(frame, font=("Helvetica", 14), width=30, bd=2, relief="solid", bg="#dfe6e9", fg="#2d3436")
user_entry.grid(row=0, column=1, pady=10, padx=10)

# Labels for ComboBoxes
label_browser = tk.Label(frame, text="Select Browser:", font=("Helvetica", 12), bg="#f1f1f1")
label_browser.grid(row=1, column=0, sticky="w", pady=10, padx=10)

# ComboBox for browser selection
combo_br = tk.StringVar()
browser_combos = ttk.Combobox(frame, textvariable=combo_br, values=browsers, state='readonly', font=("Helvetica", 12))
browser_combos.set('Select Browser')
browser_combos.grid(row=1, column=1, pady=10, padx=10)

# Labels for theme selection
label_theme = tk.Label(frame, text="Select Theme:", font=("Helvetica", 12), bg="#f1f1f1")
label_theme.grid(row=2, column=0, sticky="w", pady=10, padx=10)


# ComboBox for theme selection
combo_th = tk.StringVar()
theme_combos = ttk.Combobox(frame, textvariable=combo_th, values=modes, state='readonly', font=("Helvetica", 12))
theme_combos.set('Select Theme')
theme_combos.grid(row=2, column=1, pady=10, padx=10)

label_size = tk.Label(frame, text="Select Screen Resolution:", font=("Helvetica", 12), bg="#f1f1f1")
label_theme.grid(row=3, column=0, sticky="w", pady=10, padx=10)

screenSize = tk.StringVar()
size_combo = ttk.Combobox(frame,textvariable = screenSize, values=list(sizes.keys()),state="readonly")
size_combo.set("Select Screen Size")
size_combo.grid(row=3,column=1,pady=10,padx=10)

# Start button with rounded edges
start_button = tk.Button(frame, text="Start", command=start_action, font=("Helvetica", 14), bg="#74b9ff", fg="#ffffff",
                         bd=0, relief="flat", padx=20, pady=10)
start_button.grid(row=4,column = 1, columnspan=2, pady=20)


# Add hover effect for the button
def on_enter(e):
    start_button.config(bg="#0984e3")


def on_leave(e):
    start_button.config(bg="#74b9ff")


start_button.bind("<Enter>", on_enter)
start_button.bind("<Leave>", on_leave)

# Start the Tkinter event loop
root.mainloop()

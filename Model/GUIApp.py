import tkinter as tk
from tkinter import messagebox
import bot_model as bm


# Function for the chatbot response
def get_bot_response(event=None):
    user_input = user_entry.get()  # Get the user input
    if user_input.strip() == "":
        messagebox.showwarning("Input Error", "Please enter a message.")
        return
    listbox.insert(tk.END, f"You: {user_input}")  # Display user's message in the listbox
    user_entry.delete(0, tk.END)  # Clear the user input field

    ints = bm.predict_class(user_input.lower())
    response = bm.get_response(ints)
    listbox.insert(tk.END, f"Bot: {response}")  # Display bot's response in the listbox

def clear_content(event=None):
    listbox.delete(0,tk.END)

def exit_app(event=None):
    choice = messagebox.askquestion("Exit","Do you want to exit?")
    if choice.lower() == "yes":
        root.destroy()
    else:
        return

# Create the main window
root = tk.Tk()
root.title("ChatMaster")
root.geometry("1000x700")
root.config(bg="#6e98f3")

# Add a title label
title_label = tk.Label(root, text="ChatMaster By Bharat", font=("Helvetica", 35, "bold"), bg="#6e98f3", fg="#333")
title_label.pack(pady=10)

# Create a Listbox to display chat conversation
listbox = tk.Listbox(root, bg="#84a9f9", fg="#333", font=("Helvetica", 15), selectmode=tk.SINGLE,
                     bd=2,height=15)
listbox.pack(pady=10,padx=20,fill='x')

# Create a Text Entry widget for user input
user_entry = tk.Entry(root, font=("Helvetica", 14), width=60, bd=2,bg="#84a9f9")
user_entry.pack(pady=10)

user_entry.bind('<Return>',get_bot_response)

# Create a Button to trigger bot response
send_button = tk.Button(root, text="Send", font=("Helvetica", 14), bg="#4CAF50", fg="#fff", command=get_bot_response)
send_button.pack(pady=10)

clear_button = tk.Button(root,text="Clear Chat",font=("Helvetica", 14), bg="#4CAF50", fg="#fff", command=clear_content)
clear_button.pack(pady=5)

exit_button = tk.Button(root,text="Exit",font=("Helvetica", 14), bg="#4CAF50", fg="#fff", command=exit_app)
exit_button.pack(pady=5)
# Run the Tkinter event loop
root.mainloop()

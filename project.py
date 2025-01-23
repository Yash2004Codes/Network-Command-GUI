""" 
    
from tkinter import *
import subprocess

def run_command():
    # Get the command entered by the user
    command = command_entry.get()
    
    # Clear the output area
    output_text.delete("1.0", END)
    
    try:
        # Run the command using subprocess
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        
        # Display the result in the output area
        if result.returncode == 0:
            output_text.insert(END, result.stdout)  # Command output
        else:
            output_text.insert(END, f"Error:\n{result.stderr}")  # Error output
    except Exception as e:
        output_text.insert(END, f"Exception:\n{str(e)}")  # Any other exception

# Create the main window
window = Tk()
window.title("Networking Command Tool")
window.geometry("600x400")  # Set window size

# Create a label for the command entry
command_label = Label(window, text="Enter Command:", font=("Arial", 12))
command_label.pack(pady=5)

# Create an entry widget for the user to type the command
command_entry = Entry(window, width=50, font=("Arial", 12))
command_entry.pack(pady=5)

# Create a button to run the command
run_button = Button(window, text="Run Command", command=run_command, font=("Arial", 12))
run_button.pack(pady=10)

# Create a text widget to display the output
output_text = Text(window, wrap=WORD, width=70, height=15, font=("Courier New", 10), bg="#f4f4f4")
output_text.pack(pady=5)

# Run the main loop
window.mainloop()

styled code

from tkinter import *
from tkinter import ttk
import subprocess

def run_command():
    # Get the command entered by the user
    command = command_entry.get()
    
    # Clear the output area
    output_text.delete("1.0", END)
    
    try:
        # Run the command using subprocess
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        
        # Display the result in the output area
        if result.returncode == 0:
            output_text.insert(END, result.stdout)  # Command output
        else:
            output_text.insert(END, f"Error:\n{result.stderr}")  # Error output
    except Exception as e:
        output_text.insert(END, f"Exception:\n{str(e)}")  # Any other exception

# Create the main window
window = Tk()
window.title("Networking Command Tool")
window.geometry("420x420")
window.resizable(False, False)

# Styling
window.configure(bg="#2b2b2b")  # Set background color
style = ttk.Style()
style.configure("TLabel", foreground="white", background="#2b2b2b", font=("Arial", 12))
style.configure("TButton", foreground="#ffffff", background="#5a5aff", font=("Arial", 12))
style.map("TButton", background=[("active", "#4a4aff")])

# Header Label
header_label = Label(window, text="Networking Command Executor", font=("Arial Bold", 16), bg="#2b2b2b", fg="white")
header_label.pack(pady=10)

# Command Label and Entry
command_label = ttk.Label(window, text="Enter Networking Command:")
command_label.pack(pady=5)

command_entry = ttk.Entry(window, width=50, font=("Arial", 12))
command_entry.pack(pady=5)

# Run Button
run_button = ttk.Button(window, text="Run Command", command=run_command)
run_button.pack(pady=10)

# Output Text Widget with Scrollbar
frame = Frame(window, bg="#2b2b2b")
frame.pack(pady=10)

scrollbar = Scrollbar(frame)
scrollbar.pack(side=RIGHT, fill=Y)

output_text = Text(frame, wrap=WORD, width=80, height=20, font=("Courier New", 10), bg="#1e1e1e", fg="#00ff00", yscrollcommand=scrollbar.set)
output_text.pack(side=LEFT)

scrollbar.config(command=output_text.yview)

# Footer Label
footer_label = Label(window, text="Designed by Yash Sharma", font=("Arial", 10), bg="#2b2b2b", fg="#808080")
footer_label.pack(pady=10)

# Run the main loop
window.mainloop()
"""
from tkinter import *
from tkinter import ttk
import subprocess

def run_command():
    # Get the command entered by the user
    command = command_entry.get()
    
    # Clear the output area
    output_text.delete("1.0", END)
    
    try:
        # Run the command using subprocess
        result = subprocess.run(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, text=True, shell=True)
        
        # Display the result in the output area
        if result.returncode == 0:
            output_text.insert(END, result.stdout)  # Command output
        else:
            output_text.insert(END, f"Error:\n{result.stderr}")  # Error output
    except Exception as e:
        output_text.insert(END, f"Exception:\n{str(e)}")  # Any other exception

# Create the main window
window = Tk()
window.title("Networking Command Tool")
window.geometry("800x600")  # Set initial window size
window.state("zoomed")  # Start the app in maximized mode
window.configure(bg="#2b2b2b")

# Styling
style = ttk.Style()
style.configure("TLabel", foreground="white", background="#2b2b2b", font=("Arial", 12))
style.configure("TButton", foreground="#ffffff", background="#5a5aff", font=("Arial", 12))
style.map("TButton", background=[("active", "#4a4aff")])

# Header Label
header_label = Label(window, text="Networking Command Executor", font=("Arial Bold", 25,"bold"), bg="#2b2b2b", fg="white")
header_label.pack(pady=10)

# Command Label and Entry
command_label = ttk.Label(window, text="Enter Networking Command:" ,font=("Arial", 15,"bold"))
command_label.pack(pady=5)

command_entry = ttk.Entry(window, font=("Arial", 15,"bold"))
command_entry.pack(pady=5, fill=X, padx=20)  # Adjusts to window width

# Styling the Button
style.configure("Custom.TButton",
                foreground="#333",  # Text color
                background="#5a5aff",  # Background color
                font=("Arial", 12, "bold"),
                padding=5)



# Run Button with Custom Style
run_button = ttk.Button(window, text="Run Command", command=run_command, style="Custom.TButton")
run_button.pack(pady=10)


# Output Frame with Text Widget and Scrollbar
output_frame = Frame(window, bg="#2b2b2b")
output_frame.pack(pady=10, fill=BOTH, expand=True)

scrollbar = Scrollbar(output_frame)
scrollbar.pack(side=RIGHT, fill=Y)

output_text = Text(output_frame, wrap=WORD, font=("Courier New", 15), bg="#1e1e1e", fg="#00ff00", yscrollcommand=scrollbar.set)
output_text.pack(side=LEFT, fill=BOTH, expand=True)

scrollbar.config(command=output_text.yview)

# Footer Label
footer_label = Label(window, text="Designed by Yash.L.Sharma", font=("Arial", 20,"bold"), bg="#2b2b2b", fg="#FF5733")
footer_label.pack(pady=10)

# Run the main loop
window.mainloop()


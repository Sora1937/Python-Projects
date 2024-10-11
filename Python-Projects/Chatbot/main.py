import customtkinter as ctk
from BowlingChatbot import get_response 

# Function to handle sending messages to the bot
def send_message(event=None):
    user_message = input_box.get()
    if user_message.strip():
        display_message("You", user_message)  # Display user message
        input_box.delete(0, ctk.END)

        # Get the bot's response using the provided bot logic
        bot_response = get_response(user_message)
        display_message("Bot", bot_response)  # Display bot response

    # Auto-scroll to the bottom
    chat_canvas.update_idletasks()
    chat_canvas.yview_moveto(1)

def display_message(sender, message):
    # Create a message frame for the message bubble
    message_frame = ctk.CTkFrame(chat_canvas_inner, fg_color="transparent")
    message_frame.pack(fill='x', padx=10, pady=2, anchor='w' if sender == "Bot" else 'e')
    
    # Create a label for the message
    message_label = ctk.CTkLabel(
        message_frame, 
        text=f"{sender}: {message}",
        anchor="w", 
        fg_color="green" if sender == "Bot" else "blue", 
        padx=10, pady=5, corner_radius=10
    )
    
    # Pack the label with dynamic width based on the message length
    message_label.pack(padx=10, pady=5, anchor='w' if sender == "Bot" else 'e')

# Initialize the appearance of customtkinter
ctk.set_appearance_mode("dark")  # Modes: "System" (default), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (default), "green", "dark-blue"

# Main GUI setup
root = ctk.CTk()
root.title("Bowling Bot")
root.geometry("550x400")  # Set default window size

# Create a scrollable canvas for chat messages
chat_canvas = ctk.CTkCanvas(root, bd=0, highlightthickness=0)
chat_canvas.grid(row=0, column=0, columnspan=2, padx=10, pady=10, sticky="nsew")

# Set the canvas background color manually to match the chat frame
chat_canvas.configure(bg="#2a2d2e")  # Example dark color that matches customtkinter's dark theme

# Create an inner frame for messages inside the canvas
chat_canvas_inner = ctk.CTkFrame(chat_canvas, fg_color="#2a2d2e")
canvas_window = chat_canvas.create_window((0, 0), window=chat_canvas_inner, anchor='nw')  # Keep reference to the window

# Add a scrollbar
scrollbar = ctk.CTkScrollbar(root, orientation="vertical", command=chat_canvas.yview)
scrollbar.grid(row=0, column=2, sticky='ns')

chat_canvas.configure(yscrollcommand=scrollbar.set)

# Function to handle mouse wheel scrolling
def on_mouse_wheel(event):
    # Scroll the canvas based on the wheel movement
    chat_canvas.yview_scroll(int(-1*(event.delta/120)), "units")

# Bind the mouse wheel event to the chat canvas
chat_canvas.bind_all("<MouseWheel>", on_mouse_wheel)

# Configure the root grid to make the frame expand
root.grid_rowconfigure(0, weight=1)
root.grid_columnconfigure(0, weight=1)

# Make the canvas inner frame dynamically adjust its size
def on_configure(event):
    chat_canvas.configure(scrollregion=chat_canvas.bbox("all"))

chat_canvas_inner.bind("<Configure>", on_configure)

# Bind canvas resizing to update the inner frame width
def on_canvas_resize(event):
    chat_canvas.itemconfig(canvas_window, width=event.width)  # Update the width of the canvas window

chat_canvas.bind("<Configure>", on_canvas_resize)

# User input field
input_box = ctk.CTkEntry(root, width=360)
input_box.grid(row=1, column=0, padx=10, pady=10, sticky="ew")

# Send button
send_button = ctk.CTkButton(root, text="Send", command=send_message)
send_button.grid(row=1, column=1, padx=10, pady=10, sticky="ew")

input_box.bind('<Return>', send_message)

# Send greeting message immediately after GUI setup
display_message("Bot", "Hello! I'm the Bowling Alley ChatBot. How can I help you today?")

# Run the customtkinter loop
root.mainloop()

import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk

class LoginFrame(tk.Frame):
    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller

        # Load the background image using Pillow
        self.background_image = Image.open("background.png")  # Ensure you have a background.png in your directory

        # Get the screen width and height
        screen_width = parent.winfo_screenwidth()
        screen_height = parent.winfo_screenheight()

        # Resize the image to fit the screen
        self.background_image = self.background_image.resize((screen_width, screen_height), Image.LANCZOS)
        self.background_photo = ImageTk.PhotoImage(self.background_image)

        # Create a canvas widget that fills the entire screen
        self.canvas = tk.Canvas(self, width=screen_width, height=screen_height)
        self.canvas.pack(fill="both", expand=True)

        # Place the background image on the canvas, stretched to fit the screen
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.background_photo)

        # Create a frame to hold the login widgets and place it over the canvas
        self.login_frame = tk.Frame(self.canvas, bg="white")
        self.login_frame.place(relx=0.5, rely=0.5, anchor=tk.CENTER)  # Center the frame in the canvas

        # Place widgets on the frame
        tk.Label(self.login_frame, text="Login", bg="white",font=("Helvetica", 16,"bold")).grid(row=0, column=0, padx=10, pady=10, columnspan=2)

        tk.Label(self.login_frame, text="Username:", bg="white",font=("Helvetica", 12)).grid(row=1, column=0, padx=10, pady=5)
        self.username_entry = tk.Entry(self.login_frame)
        self.username_entry.grid(row=1, column=1, padx=10, pady=5)

        tk.Label(self.login_frame, text="Password:", bg="white",font=("Helvetica", 12)).grid(row=2, column=0, padx=10, pady=5)
        self.password_entry = tk.Entry(self.login_frame, show="*")
        self.password_entry.grid(row=2, column=1, padx=10, pady=5)

        self.login_button = tk.Button(self.login_frame, text="Login", command=self.login, font=("Helvetica", 12, "bold"), fg="white", bg="blue", relief=tk.GROOVE)
        self.login_button.grid(row=3, column=0, columnspan=2, padx=10, pady=10)

    def login(self):
        username = self.username_entry.get()
        password = self.password_entry.get()

        if username == "user" and password == "user":
            self.controller.show_frame("CustomerFrame")
        elif username == "admin" and password == "admin":
            self.controller.show_frame("ReportFrame")
        else:
            messagebox.showerror("Login Error", "Invalid username or password")

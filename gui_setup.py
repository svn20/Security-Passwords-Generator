'''
This file was build: 01/08/2023

'''

import tkinter as tk
from tkinter import ttk
import string
import random
import pyperclip

class PasswordGeneratorApp:
    '''
    Application Config
    '''
    def __init__(self, root):
        self.root = root
        self.root.title("Password Generator")
        self.root.geometry("400x300")
        self.root.configure(bg="gray25")

        self.style = ttk.Style()
        self.style.configure("Main.TFrame", background="gray25")
        self.style.configure("TButton", background="black", font=("Helvetica", 12))
        self.style.configure("TLabel", background="gray25", foreground="white")

        self.main_frame = ttk.Frame(self.root, padding=10, style="Main.TFrame")
        self.main_frame.pack(expand=True, fill="both")

        self.var = tk.IntVar()

        self.create_option_buttons()
        self.create_action_buttons()

        self.generated_text = tk.StringVar()

        self.selection_label = ttk.Label(self.main_frame,
                        text="Selección actual: Ninguna", font=("Helvetica", 14), style="TLabel")
        self.selection_label.pack(pady=10)

        self.display_label = ttk.Label(self.main_frame,
                        text="", font=("Helvetica", 12), style="TLabel")
        self.display_label.pack(pady=10)

        self.copy_button = ttk.Button(self.main_frame,
                        text="Copiar al portapapeles", command=self.copy_to_clipboard,
                        style="TButton")
        self.copy_button.pack(pady=10)

        self.update_selection_label()

        self.var.trace("w", self.update_selection_label)

    def create_option_buttons(self):
        '''
        We are using an array to
        store our three options
        (according to the size of the array)
        '''
        option_frame = ttk.Frame(self.main_frame, style="Main.TFrame")
        option_frame.pack(pady=10)

        options = [12, 16, 18]
        for index, option in enumerate(options):
            option_button = ttk.Radiobutton(option_frame,
                            text=f"{option} caracteres", variable=self.var, value=option)
            option_button.grid(row=0, column=index, padx=5, pady=5)

    def create_action_buttons(self):
        '''
        Config for the main
        buttons
        '''
        button_frame = ttk.Frame(self.main_frame, style="Main.TFrame")
        button_frame.pack()

        ttk.Button(button_frame, text="Generar texto aleatorio",
                   command=self.generate_random_button,
                   style="TButton").grid(row=0, column=1, padx=5, pady=5)
        ttk.Button(button_frame, text="Limpiar selección",
                   command=self.clear_selection,
                   style="TButton").grid(row=0, column=2, padx=5, pady=5)

    def generate_random_text(self, length):
        '''
        The method makes a perfect way
        to generate random passwords
        '''
        random_text = ''.join(random.choice(string.ascii_letters + string.digits)
                            for _ in range(length))
        return random_text

    def generate_random_button(self):
        '''
        The user must select one of
        the options, so this method
        will generate the passwords
        calling the last method:
        (generate random text)
        '''
        selected_option = self.var.get()
        if selected_option in [12, 16, 18]:
            random_text = self.generate_random_text(selected_option)
            self.display_label.config(text=f"Texto aleatorio: {random_text}")

    def clear_selection(self):
        '''
        Erase the previous option
        selected
        '''
        self.var.set(0)
        self.display_label.config(text="")
        self.generated_text.set("")

    def copy_to_clipboard(self):
        '''
        The user'll be enable to
        copy the password with a click
        instead the manual mode
        '''
        text_to_copy = self.display_label.cget("text").split(": ", 1)[-1]
        if text_to_copy:
            pyperclip.copy(text_to_copy)

    def update_selection_label(self):
        '''
        Updates the user selection from
        the radio buttons
        '''
        selected_option = self.var.get()
        if selected_option in [12, 16, 18]:
            self.selection_label.config(text=f"Selección actual: {selected_option} caracteres")
        else:
            self.selection_label.config(text="Selección actual: Ninguna")

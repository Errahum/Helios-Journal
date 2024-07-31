import tkinter as tk
from tkinter import ttk
from tkcalendar import Calendar
import datetime
import os
import json
from tkinter import messagebox

from src.core.save_data import save_entry


class CalendarApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Helios Journal")

        self.root.geometry("1200x800")

        self.create_widgets()

        # aujourd'hui
        self.show_entry_interface()

    def create_widgets(self):
        # grille
        self.root.columnconfigure(0, weight=0)
        self.root.columnconfigure(1, weight=1)  # Donne plus de poids à la colonne 1 (texte)
        self.root.rowconfigure(0, weight=1)

        # calendrier taille fixe
        self.calendar_frame = ttk.Frame(self.root, width=250, height=250)
        self.calendar_frame.grid_propagate(False)  # Empêche la frame de redimensionner avec le contenu
        self.calendar_frame.grid(row=0, column=0, padx=20, pady=20, sticky="nw")

        self.calendar = Calendar(
            self.calendar_frame,
            selectmode='day',
            year=datetime.datetime.now().year,
            month=datetime.datetime.now().month,
            day=datetime.datetime.now().day
        )
        self.calendar.pack(expand=True, fill=tk.BOTH)

        # frame zone de texte
        self.text_frame = ttk.Frame(self.root)
        self.text_frame.grid(row=0, column=1, padx=20, pady=20, sticky="nsew")
        self.text_frame.columnconfigure(0, weight=1)
        self.text_frame.rowconfigure(0, weight=1)
        self.text_frame.rowconfigure(1, weight=0)

        #zone de texte
        self.text_area = tk.Text(self.text_frame, font=("Arial", 12))
        self.text_area.grid(row=0, column=0, sticky="nsew")

        # bouton de sauvegarde
        self.save_button = ttk.Button(self.text_frame, text="Sauvegarder", command=self.save_entry)
        self.save_button.grid(row=1, column=0, pady=10)
        self.save_button['state'] = tk.DISABLED

        self.calendar.bind("<<CalendarSelected>>", self.show_entry_interface)

    def show_entry_interface(self, event=None):
        selected_date = self.calendar.get_date()
        self.text_area.delete('1.0', tk.END)
        self.save_button['state'] = tk.NORMAL
        self.load_entry(selected_date)

    def save_entry(self):
        selected_date = self.calendar.get_date()
        entry_text = self.text_area.get("1.0", tk.END)
        save_entry(selected_date, entry_text)
        tk.messagebox.showinfo("Sauvegarde", "L'entrée a été sauvegardée avec succès.")

    def load_entry(self, date):
        file_path = os.path.join("entries", "entries.jsonl")
        if os.path.exists(file_path):
            with open(file_path, "r", encoding="utf-8") as file:
                for line in file:
                    entry = json.loads(line)
                    if entry["date"] == date:
                        self.text_area.insert(tk.END, entry["text"])
                        break


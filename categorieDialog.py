import tkinter as tk
from tkinter import ttk
from tkinter import messagebox


class CategorieDialog(tk.Toplevel):
    def __init__(self, parent):
        super().__init__(parent)

        self.parent = parent
        self.result = None

        self.title("Ajouter une catégorie")

        self.create_widgets()
        self.grab_set()

    def create_widgets(self):
        self.nom_label = ttk.Label(self, text="Nom")
        self.nom_label.grid(row=0, column=0, padx=8, pady=8)
        self.nom_entry = ttk.Entry(self)
        self.nom_entry.grid(row=0, column=1, padx=5, pady=8)

        self.ok_button = ttk.Button(self, text="OK", command=self.on_ok)
        self.ok_button.grid(row=1, column=0, padx=10, pady=10)

        self.cancel_button = ttk.Button(self, text="Annuler", command=self.destroy)
        self.cancel_button.grid(row=1, column=1, padx=10, pady=10)

    def on_ok(self):
        nom = self.nom_entry.get()

        if not nom:
            messagebox.showerror("Erreur", "Le nom de la catégorie ne peut pas être vide.")
            return

        self.result = nom
        self.destroy()

import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from categorie import Categorie

class ProduitDialog(tk.Toplevel):
    def __init__(self, parent, produit=None):
        super().__init__(parent)

        self.parent = parent
        self.produit = produit
        self.result = None

        self.title("Ajouter un produit" if produit is None else "Modifier un produit")

        self.create_widgets()
        self.grab_set()

    def create_widgets(self):
        self.nom_label = ttk.Label(self, text="Nom")
        self.nom_label.grid(row=0, column=0, padx=8, pady=8)
        self.nom_entry = ttk.Entry(self)
        self.nom_entry.grid(row=0, column=1, padx=5, pady=8)

        self.marque_label = ttk.Label(self, text="Marque")
        self.marque_label.grid(row=1, column=0, padx=10, pady=8)
        self.marque_entry = ttk.Entry(self)
        self.marque_entry.grid(row=1, column=1, padx=10, pady=8)

        self.description_label = ttk.Label(self, text="Description")
        self.description_label.grid(row=2, column=0, padx=10, pady=8)
        self.description_entry = ttk.Entry(self)
        self.description_entry.grid(row=2, column=1, padx=10, pady=8)

        self.prix_label = ttk.Label(self, text="Prix")
        self.prix_label.grid(row=3, column=0, padx=10, pady=10)
        self.prix_entry = ttk.Entry(self)
        self.prix_entry.grid(row=3, column=1, padx=10, pady=10)

        self.quantite_label = ttk.Label(self, text="Quantité")
        self.quantite_label.grid(row=4, column=0, padx=10, pady=10)
        self.quantite_entry = ttk.Entry(self)
        self.quantite_entry.grid(row=4, column=1, padx=10, pady=10)

        self.categorie_label = ttk.Label(self, text="Catégorie")
        self.categorie_label.grid(row=5, column=0, padx=10, pady=10)
        self.categorie_entry = ttk.Entry(self)
        self.categorie_entry.grid(row=5, column=1, padx=10, pady=10)

        if self.produit is not None:
            self.nom_entry.insert(0, self.produit[2])
            self.marque_entry.insert(0, self.produit[1])
            self.description_entry.insert(0, self.produit[3])
            self.prix_entry.insert(0, self.produit[4])
            self.quantite_entry.insert(0, self.produit[5])
            self.categorie_entry.insert(0, self.produit[6])
            
        self.ok_button = ttk.Button(self, text="OK", command=self.on_ok)
        self.ok_button.grid(row=6, column=0, padx=10, pady=10)

        self.cancel_button = ttk.Button(self, text="Annuler", command=self.destroy)
        self.cancel_button.grid(row=6, column=1, padx=10, pady=10)

    def on_ok(self):
        nom = self.nom_entry.get()
        marque = self.marque_entry.get()
        description = self.description_entry.get()
        prix = int(self.prix_entry.get())
        quantite = int(self.quantite_entry.get())
        categorie_number = self.categorie_entry.get()

        # Vérifier si l'utilisateur a entré un numéro de catégorie valide
        try:
            categorie_id = int(categorie_number)
            categorie = self.parent.categorie.recuperer_par_id(categorie_id)
            if categorie is None:
                raise ValueError("La catégorie n'existe pas")
        except ValueError as e:
            messagebox.showerror("Erreur", str(e))
            return

        self.result = (nom, marque, description, prix, quantite, categorie_id)
        self.destroy()

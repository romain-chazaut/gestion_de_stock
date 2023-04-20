import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from database import Database
from categorie import Categorie
from produit import Produit
from produitDialog import ProduitDialog
from categorieDialog import CategorieDialog


class Application(tk.Tk):
    
    def __init__(self):
        super().__init__()

        self.title("Gestion de stock")
        self.geometry("800x500")

        self.db = Database()
        self.categorie = Categorie(self.db)
        self.produit = Produit(self.db)

        self.create_widgets()

    def create_widgets(self):

        self.tableau = ttk.Treeview(self, columns=("Nom", "Marque", "Description", "Prix", "Quantité", "Catégorie"))

        self.tableau.heading("Nom", text="Nom")
        self.tableau.column("Nom", width=120)

        self.tableau.heading("Marque", text="Marque")
        self.tableau.column("Marque", width=120)

        self.tableau.heading("Description", text="Description")
        self.tableau.column("Description", width=120)

        self.tableau.heading("Prix", text="Prix")
        self.tableau.column("Prix", width=80)

        self.tableau.heading("Quantité", text="Quantité")
        self.tableau.column("Quantité", width=80)

        self.tableau.heading("Catégorie", text="Catégorie")
        self.tableau.column("Catégorie", width=120)

        self.tableau["show"] = "headings"
        self.tableau.pack(fill=tk.BOTH, expand=True)

        self.update_tableau()

        bouton_frame = tk.Frame(self)
        bouton_frame.pack(pady=10)

        bouton_ajouter = tk.Button(bouton_frame, text="Ajouter", command=self.ajouter_produit, bg="#4CAF50", fg="white", padx=30, pady=5)
        bouton_ajouter.grid(row=0, column=0, padx=(10, 40))

        bouton_supprimer = tk.Button(bouton_frame, text="Supprimer", command=self.supprimer_produit, bg="#f44336", fg="white", padx=30, pady=5)
        bouton_supprimer.grid(row=0, column=1, padx=(10, 40))

        bouton_modifier = tk.Button(bouton_frame, text="Modifier", command=self.modifier_produit, bg="#2196F3", fg="white", padx=30, pady=5)
        bouton_modifier.grid(row=0, column=2, padx=(10, 40))
        
        self.ajouter_categorie_button = tk.Button(bouton_frame, text="Ajouter une catégorie", command=self.ajouter_categorie, bg="#9C27B0", fg="white", padx=30, pady=5)
        self.ajouter_categorie_button.grid(row=0, column=3, padx=(10, 40))

    def update_tableau(self):

        for item in self.tableau.get_children():
            self.tableau.delete(item)

        produits = self.produit.recuperer_tout()
        categories = {cat[0]: cat[1] for cat in self.categorie.recuperer_tout()}
        
        for prod in produits:
            self.tableau.insert("", "end", iid=str(prod[0]), values=(prod[1], prod[2], prod[3], prod[4], prod[5], categories[prod[6]]))

    def ajouter_produit(self):
        dialog = ProduitDialog(self)
        self.wait_window(dialog)
        
        if dialog.result is not None:
            nom, marque, description, prix, quantite, categorie = dialog.result
            categorie_id = self.categorie.recuperer_id_par_nom(categorie)
            self.produit.ajouter(marque, nom, description, prix, quantite, categorie_id)
            self.update_tableau()

    def supprimer_produit(self):
        selected_item = self.tableau.selection()
        
        if selected_item:
            id = int(selected_item[0])
            confirm = messagebox.askyesno("Supprimer le produit", "Voulez-vous vraiment supprimer le produit sélectionné ?")
            if confirm:
                self.produit.supprimer(id)
                self.update_tableau()

    def modifier_produit(self):
        selected_item = self.tableau.selection()
        
        if selected_item:
            id = int(selected_item[0])
            produit = self.produit.recuperer_par_id(id)
            dialog = ProduitDialog(self, produit)
            self.wait_window(dialog)
            if dialog.result is not None:
                nom, marque, description, prix, quantite, categorie = dialog.result
                categorie_id = self.categorie.recuperer_id_par_nom(categorie)
                self.produit.modifier(id, marque, nom, description, prix, quantite, categorie_id)
                self.update_tableau()

    def ajouter_categorie(self):
        dialog = CategorieDialog(self)
        self.wait_window(dialog)

        if dialog.result:
            self.categorie.ajouter(dialog.result)
            messagebox.showinfo("Succès", "La catégorie a été ajoutée.")
            self.update_tableau()


if __name__ == "__main__":
    app = Application()
    app.mainloop()


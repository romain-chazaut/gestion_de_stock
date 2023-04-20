class Produit:
    def __init__(self, db):
        self.db = db

    def ajouter(self, nom, marque, description, prix, quantite, id_categorie):
        self.db.cursor.execute(
            "INSERT INTO produit (marque, nom, description, prix, quantite, id_categorie) VALUES (%s, %s, %s, %s, %s, %s)",
            (nom, marque, description, prix, quantite, id_categorie)
        )
        self.db.commit()

    def supprimer(self, id):
        self.db.cursor.execute("DELETE FROM produit WHERE id = %s", (id,))
        self.db.commit()

    def modifier(self, id, nom, marque, description, prix, quantite, id_categorie):
        self.db.cursor.execute(
            "UPDATE produit SET marque = %s, nom = %s, description = %s, prix = %s, quantite = %s, id_categorie = %s WHERE id = %s",
            (nom, marque, description, prix, quantite, id_categorie, id)
        )
        self.db.commit()

    def recuperer_tout(self):
        self.db.cursor.execute("SELECT * FROM produit")
        return self.db.cursor.fetchall()

    def recuperer_par_id(self, id):
        self.db.cursor.execute("SELECT * FROM produit WHERE id = %s", (id,))
        return self.db.cursor.fetchone()
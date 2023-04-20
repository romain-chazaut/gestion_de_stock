class Categorie:
    def __init__(self, db):
        self.db = db

    def ajouter(self, nom):
        self.db.cursor.execute("INSERT INTO categorie (nom) VALUES (%s)", (nom,))
        self.db.commit()

    def recuperer_tout(self):
        self.db.cursor.execute("SELECT * FROM categorie")
        return self.db.cursor.fetchall()
    
    def recuperer_id_par_nom(self, nom):
        self.db.cursor.execute("SELECT id FROM categorie WHERE nom=%s", (nom,))
        result = self.db.cursor.fetchone()
        if result:
            return result[0]
        else:
            self.db.cursor.execute("INSERT INTO categorie (nom) VALUES (%s)", (nom,))
            self.db.commit()
            return self.db.cursor.lastrowid

    def recuperer_par_id(self, id):
        self.db.cursor.execute("SELECT * FROM categories WHERE id = %s", (id,))
        return self.db.cursor.fetchone()

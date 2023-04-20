import mysql.connector
from dotenv import load_dotenv
import os
load_dotenv()

class Database:
    def __init__(self):
        self.connection = mysql.connector.connect(
            host="localhost",
            user="root",
            password=os.getenv("PASSWORD"),
            database="boutique"
        )
        self.cursor = self.connection.cursor()

    def commit(self):
        self.connection.commit()

    def close(self):
        self.connection.close()




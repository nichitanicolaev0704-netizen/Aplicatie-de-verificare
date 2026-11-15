# database.py
import sqlite3

class DatabaseManager:
    def __init__(self):
        self.conn = None

    def deschide_fisier(self, calea_fisier):
        """Deschide un fișier SQL extern (.db / .sqlite)."""
        if self.conn:
            self.conn.close()
        self.conn = sqlite3.connect(calea_fisier)
        return self.obtine_nume_tabele()

    def obtine_nume_tabele(self):
        if not self.conn:
            return []
        cursor = self.conn.cursor()
        cursor.execute("SELECT name FROM sqlite_master WHERE type='table';")
        return [row[0] for row in cursor.fetchall()]

    def citeste_tabel(self, nume_tabel):
        """Returnează tuplele și numele coloanelor pentru un tabel dat."""
        if not self.conn:
            return [], []
        cursor = self.conn.cursor()
        cursor.execute(f"SELECT * FROM [{nume_tabel}]")
        date = cursor.fetchall()
        coloane = [desc[0] for desc in cursor.description]
        return date, coloane

    def inchide(self):
        if self.conn:
            self.conn.close()

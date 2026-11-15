
import sys
from PyQt6.QtWidgets import QApplication, QFileDialog
from database import DatabaseManager
from logic import verifica_dependenta_functionala
from ui import MainWindowUI, STYLE_QSS

class AppController:
    def __init__(self):
        self.db = DatabaseManager()
        self.date_tabel = []
        self.nume_coloane = []

        self.ui = MainWindowUI(self.db, self.ruleaza_verificarea)
        self.ui.btn_deschide_db.clicked.connect(self.deschide_fisier_sql)
        self.ui.combo_tabele.currentIndexChanged.connect(self.schimba_tabelul)

    def deschide_fisier_sql(self):
        fisier, _ = QFileDialog.getOpenFileName(self.ui, "Deschide Bază de Date", "", "SQLite DB (*.db *.sqlite)")
        if fisier:
            try:
                tabele = self.db.deschide_fisier(fisier)
                self.ui.combo_tabele.clear()
                if tabele:
                    self.ui.combo_tabele.addItems(tabele)
                    self.actualizeaza_date_tabel(tabele[0])
                    self.ui.afiseaza_mesaj("Succes", "Baza de date a fost încărcată cu succes!")
                else:
                    self.ui.afiseaza_mesaj("Atenție", "Baza de date nu conține niciun tabel.", este_eroare=True)
            except Exception as e:
                self.ui.afiseaza_mesaj("Eroare", f"Eroare la deschidere:\n{str(e)}", este_eroare=True)

    def schimba_tabelul(self):
        nume_tabel = self.ui.combo_tabele.currentText()
        if nume_tabel and not nume_tabel.startswith("--"):
            self.actualizeaza_date_tabel(nume_tabel)

    def actualizeaza_date_tabel(self, nume_tabel):
        self.date_tabel, self.nume_coloane = self.db.citeste_tabel(nume_tabel)
        self.ui.populeaza_tabel_si_liste(self.date_tabel, self.nume_coloane)

    def ruleaza_verificarea(self):
        if not self.date_tabel:
            self.ui.afiseaza_mesaj("Atenție", "Te rog încarcă o bază de date și selectează un tabel înainte de a verifica!", este_eroare=True)
            return

        indici_X, indici_Y = self.ui.obtine_selectii()

        if not indici_X or not indici_Y:
            self.ui.afiseaza_mesaj("Atenție", "Selectează cel puțin o coloană pentru X și una pentru Y!", este_eroare=True)
            return

        rezultat, mesaj = verifica_dependenta_functionala(
            self.date_tabel, self.nume_coloane, indici_X, indici_Y
        )

        if rezultat:
            self.ui.afiseaza_mesaj("Rezultat: TRUE", f"✅ {mesaj}")
        else:
            self.ui.afiseaza_mesaj("Rezultat: FALSE", f"❌ {mesaj}", este_eroare=True)

if __name__ == "__main__":
    app = QApplication(sys.argv)

    # FORȚĂM STILUL FUSION PENTRU A EVITA CONFLICTELE CU DARK MODE DIN LINUX
    app.setStyle("Fusion")
    app.setStyleSheet(STYLE_QSS)

    controller = AppController()
    controller.ui.show()

    sys.exit(app.exec())

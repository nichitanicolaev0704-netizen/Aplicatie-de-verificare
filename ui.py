
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout,
                             QHBoxLayout, QPushButton, QListWidget, QLabel,
                             QTableWidget, QTableWidgetItem, QMessageBox,
                             QAbstractItemView, QComboBox, QGroupBox)
from PyQt6.QtGui import QColor, QBrush

STYLE_QSS = """
QMainWindow {
    background-color: #f8f9fa;
}
QLabel {
    color: #212529;
    font-size: 13px;
    font-family: 'Segoe UI', Tahoma, sans-serif;
}
QGroupBox {
    font-weight: bold;
    border: 1px solid #ced4da;
    border-radius: 8px;
    margin-top: 10px;
    background-color: #ffffff;
    color: #212529;
    padding-top: 15px;
}
QGroupBox::title {
    subcontrol-origin: margin;
    left: 10px;
    padding: 0 5px;
    color: #495057;
}
QTableWidget {
    background-color: #ffffff;
    color: #212529;
    border: 1px solid #ced4da;
    border-radius: 6px;
    gridline-color: #e9ecef;
    font-size: 12px;
}
QHeaderView::section {
    background-color: #3b82f6;
    color: white;
    padding: 6px;
    border: none;
    font-weight: bold;
}
QListWidget {
    background-color: #ffffff;
    color: #212529;
    border: 1px solid #ced4da;
    border-radius: 6px;
    padding: 5px;
    font-size: 13px;
}
QListWidget::item:selected {
    background-color: #3b82f6;
    color: white;
    border-radius: 4px;
}
QPushButton {
    background-color: #10b981;
    color: white;
    border: none;
    padding: 10px 15px;
    font-size: 14px;
    font-weight: bold;
    border-radius: 6px;
}
QPushButton:hover {
    background-color: #059669;
}
QPushButton#btn_sql {
    background-color: #3b82f6;
}
QPushButton#btn_sql:hover {
    background-color: #2563eb;
}
QComboBox {
    background-color: white;
    color: #212529;
    border: 1px solid #ced4da;
    border-radius: 6px;
    padding: 5px;
    font-size: 13px;
}
"""

class MainWindowUI(QMainWindow):
    def __init__(self, db_manager, logic_callback):
        super().__init__()
        self.db = db_manager
        self.verifica_callback = logic_callback

        self.setWindowTitle("Verificator Dependențe Funcționale (Modular)")
        self.setGeometry(100, 100, 900, 650)
        self.init_ui()

    def init_ui(self):
        widget_central = QWidget()
        layout_principal = QVBoxLayout()
        layout_principal.setSpacing(12)
        layout_principal.setContentsMargins(15, 15, 15, 15)

        # SQL Section
        group_sql = QGroupBox("1. Sursa de Date (SQL)")
        layout_sql = QHBoxLayout()
        self.btn_deschide_db = QPushButton("📂 Încarcă Bază de Date SQLite (.db)")
        self.btn_deschide_db.setObjectName("btn_sql")
        self.combo_tabele = QComboBox()
        self.combo_tabele.addItem("-- Încarcă o bază de date mai întâi --")

        layout_sql.addWidget(self.btn_deschide_db, 2)
        layout_sql.addWidget(QLabel("Selectează Tabelul:"), 1)
        layout_sql.addWidget(self.combo_tabele, 2)
        group_sql.setLayout(layout_sql)
        layout_principal.addWidget(group_sql)

        # Table Section
        group_tabel = QGroupBox("2. Vizualizare Date din Tabel")
        layout_tabel = QVBoxLayout()
        self.tabel_ui = QTableWidget()
        layout_tabel.addWidget(self.tabel_ui)
        group_tabel.setLayout(layout_tabel)
        layout_principal.addWidget(group_tabel, 2)

        # Selection Section (X and Y)
        group_selectie = QGroupBox("3. Configurare Dependență Funcțională (X -> Y)")
        layout_selectie_H = QHBoxLayout()

        box_x = QVBoxLayout()
        box_x.addWidget(QLabel("<b>Determinant (X):</b>"))
        self.lista_X = QListWidget()
        self.lista_X.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        box_x.addWidget(self.lista_X)

        box_y = QVBoxLayout()
        box_y.addWidget(QLabel("<b>Determinat (Y):</b>"))
        self.lista_Y = QListWidget()
        self.lista_Y.setSelectionMode(QAbstractItemView.SelectionMode.MultiSelection)
        box_y.addWidget(self.lista_Y)

        layout_selectie_H.addLayout(box_x)
        layout_selectie_H.addLayout(box_y)
        group_selectie.setLayout(layout_selectie_H)
        layout_principal.addWidget(group_selectie, 1)

        # Verify Button
        self.btn_verifica = QPushButton("⚡ Verifică Valabilitatea Dependenței Funcționale")
        self.btn_verifica.clicked.connect(self.verifica_callback)
        layout_principal.addWidget(self.btn_verifica)

        widget_central.setLayout(layout_principal)
        self.setCentralWidget(widget_central)

    def populeaza_tabel_si_liste(self, date, coloane):
        self.tabel_ui.setRowCount(len(date))
        self.tabel_ui.setColumnCount(len(coloane))
        self.tabel_ui.setHorizontalHeaderLabels(coloane)

        for r, rand in enumerate(date):
            for c, val in enumerate(rand):
                item = QTableWidgetItem(str(val))
                # Forțăm culoarea textului pe negru vizibil, independent de tema Linux
                item.setForeground(QBrush(QColor("#212529")))
                self.tabel_ui.setItem(r, c, item)

        self.lista_X.clear()
        self.lista_Y.clear()
        for col in coloane:
            self.lista_X.addItem(col)
            self.lista_Y.addItem(col)

    def obtine_selectii(self):
        indici_X = [item.row() for item in self.lista_X.selectedIndexes()]
        indici_Y = [item.row() for item in self.lista_Y.selectedIndexes()]
        return indici_X, indici_Y

    def afiseaza_mesaj(self, titlu, text, este_eroare=False):
        if este_eroare:
            QMessageBox.critical(self, titlu, text)
        else:
            QMessageBox.information(self, titlu, text)

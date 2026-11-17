================================================================================
VERIFICATOR DE DEPENDENȚE FUNCȚIONALE (MODULAR PyQt6)
================================================================================

O aplicație desktop modernă, modulară, dezvoltată în Python (PyQt6), concepută 
pentru a analiza și verifica dependențele funcționale în baze de date SQLite.

--------------------------------------------------------------------------------
1. CE FACE ACEASTĂ APLICAȚIE?
--------------------------------------------------------------------------------
Aplicația oferă o interfață grafică curată și intuitivă (optimizată inclusiv 
pentru Linux prin stilul Fusion) care permite:
  * Încărcarea bazelor de date: Conectarea la orice fișier local SQLite 
    (.db, .sqlite).
  * Explorarea tabelelor: Vizualizarea automată a structurii și a rândurilor 
    conținute în tabelele selectate.
  * Configurarea dependențelor funcționale (X -> Y): Selectarea facilă a 
    coloanelor pentru determinant (X) și determinat (Y) prin intermediul 
    listelor multiple.
  * Validarea matematică/logică: Verificarea instantanee dacă dependența 
    funcțională este respectată în setul de date curent, afișând un mesaj clar 
    de succes sau eroare.

--------------------------------------------------------------------------------
2. ARHITECTURA PROIECTULUI (MODULARĂ)
--------------------------------------------------------------------------------
Proiectul este împărțit în module curate pentru o mentenanță ușoară:
  * main.py     - Controlerul principal care leagă interfața de logica bazei 
                  de date și pornește aplicația.
  * ui.py       - Gestionarea interfeței grafice (PyQt6), layout-uri, stiluri 
                  QSS și elemente vizuale.
  * logic.py    - Algoritmul de verificare a dependențelor funcționale.
  * database.py - Gestionarea conexiunilor și interogărilor SQLite.
  * .gitignore  - Exclude fișierele temporare, cache-ul (__pycache__) și 
                  bazele de date locale din controlul versiunilor.

--------------------------------------------------------------------------------
3. INSTALARE ȘI RULARE (MOD DE DEZVOLTARE)
--------------------------------------------------------------------------------
1. Clonează repository-ul:
   git clone https://github.com/nichitanicolaev0704-netizen/Aplicatie-de-verificare.git
   cd Aplicatie-de-verificare

2. Instalează dependențele (PyQt6):
   Asigură-te că ai Python 3 instalat, apoi rulează:
   pip install PyQt6

3. Pornește aplicația:
   python3 main.py

--------------------------------------------------------------------------------
4. TRANSFORMARE ÎN EXECUTABIL (.EXE WINDOWS / BINAR LINUX)
--------------------------------------------------------------------------------
Poți împacheta aplicația într-un singur fișier executabil independent folosind 
instrumentul PyInstaller.

Pasul 1: Instalarea PyInstaller
   pip install pyinstaller

Pasul 2: Generarea Executabilului
Navighează în folderul proiectului și rulează comanda de împachetare:

  * Pentru Windows (generează .exe):
    pyinstaller --noconsole --onefile main.py

  * Pentru Linux (generează binar standalone):
    pyinstaller --noconsole --onefile main.py

Notă: Parametrul "--noconsole" ascunde fereastra de terminal din fundal, 
lăsând vizibilă doar interfața grafică PyQt6, iar "--onefile" împachetează 
totul într-un singur fișier executabil.
După finalizare, vei găsi executabilul în folderul "dist/" generat automat.

--------------------------------------------------------------------------------
5. CREAREA UNEI SCURTĂTURI DE DESKTOP PE LINUX (OPȚIONAL)
--------------------------------------------------------------------------------
Dacă vrei ca aplicația să apară în meniul de aplicații din Linux sau pe desktop:

1. Creează un fișier text numit Verificator.desktop:
   nano ~/.local/share/applications/Verificator.desktop

2. Adaugă următorul conținut (înlocuind calea cu cea reală spre proiect):
   [Desktop Entry]
   Name=Verificator Dependențe Funcționale
   Exec=python3 /home/stires/project/main.py
   Terminal=false
   Type=Application
   Categories=Utility;Education;

3. Salvează fișierul și acordă-i permisiuni de execuție:
   chmod +x ~/.local/share/applications/Verificator.desktop
================================================================================

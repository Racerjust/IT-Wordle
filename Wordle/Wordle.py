import sqlite3
import random
import time
from getpass import getpass

class SQL:
    def first_time(self):
        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()

        cursor.execute("DROP TABLE IF EXISTS ITWoerter;")
        cursor.execute("DROP TABLE IF EXISTS eigene_Woerter;")
        cursor.execute("DROP TABLE IF EXISTS user")

        sql_command ="""CREATE TABLE IF NOT EXISTS ITWoerter (
            id INTEGER PRIMARY KEY,
            wort CHAR(5),
            L1 CHAR(1),
            L2 CHAR(1),
            L3 CHAR(1),
            L4 CHAR(1),
            L5 CHAR(1),
            erklärung VARCHAR(1000));"""

        cursor.execute(sql_command)
        connection.commit()
        #connection.close()

        
        #connection = sqlite3.connect("ITWordle.db")
        #cursor = connection.cursor()

        sql_command ="""CREATE TABLE IF NOT EXISTS eigene_Woerter (
            id INTEGER PRIMARY KEY,
            wort CHAR(5),
            L1 CHAR(1),
            L2 CHAR(1),
            L3 CHAR(1),
            L4 CHAR(1),
            L5 CHAR(1),
            erklärung VARCHAR(1000));"""

        cursor.execute(sql_command)
        connection.commit()
        
        sql_command = """CREATE TABLE IF NOT EXISTS user(
            id INTEGER PRIMARY KEY,
            benutzername VARCHAR(20),
            passwort VARCHAR(20));"""
        
        cursor.execute(sql_command)      
        connection.commit()
        connection.close() 

        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()

        sql_command ="""
        INSERT INTO ITWoerter (id, wort, L1, L2, L3, L4, L5, erklärung)
        VALUES 
            (NULL, 'kabel', 'k', 'a', 'b', 'e', 'l', 'Dient der physischen Verbindung von Geräten zur Daten- oder Stromübertragung.'),
            (NULL, 'taste', 't', 'a', 's', 't', 'e', 'Ein einzelnes Bedienelement auf einer Tastatur zur Eingabe.'),
            (NULL, 'druck', 'd', 'r', 'u', 'c', 'k', 'Bezieht sich auf den Vorgang der Ausgabe von Daten auf einem Drucker.'),
            (NULL, 'laser', 'l', 'a', 's', 'e', 'r', 'Technologie, die in Druckern oder optischen Laufwerken verwendet wird.'),
            (NULL, 'reset', 'r', 'e', 's', 'e', 't', 'Der Vorgang, ein System in seinen definierten Ausgangszustand zurückzusetzen.'),
            (NULL, 'strom', 's', 't', 'r', 'o', 'm', 'Die elektrische Energie, die für den Betrieb von Hardware notwendig ist.'),
            (NULL, 'audio', 'a', 'u', 'd', 'i', 'o', 'Bezeichnet Töne und Tonsignale, die digital verarbeitet werden.'),
            (NULL, 'video', 'v', 'i', 'd', 'e', 'o', 'Bezeichnet Bildsignale und Bewegtbilder, die digital verarbeitet werden.'),
            (NULL, 'board', 'b', 'o', 'a', 'r', 'd', 'Umgangssprachlich für "Mainboard" oder "Platine", die Hauptplatine eines Computers.'),
            (NULL, 'slots', 's', 'l', 'o', 't', 's', 'Physische Steckplätze auf dem Mainboard für Erweiterungskarten (z.B. PCIe).'),
            (NULL, 'power', 'p', 'o', 'w', 'e', 'r', '(Englisch für) Strom oder Leistung, oft zur Bezeichnung des Netzteils (PSU) verwendet.'),
            (NULL, 'mouse', 'm', 'o', 'u', 's', 'e', '(Englisch für) Maus, das gängige Eingabegerät zur Cursor-Steuerung.'),
            (NULL, 'cloud', 'c', 'l', 'o', 'u', 'd', 'Ein Netzwerk von entfernten Servern, das Dienste über das Internet bereitstellt.'),
            (NULL, 'modem', 'm', 'o', 'd', 'e', 'm', 'Ein Gerät, das Signale umwandelt, um Daten über Leitungen (z.B. DSL) zu senden.'),
            (NULL, 'proxy', 'p', 'r', 'o', 'x', 'y', 'Ein Server, der als Vermittler für Anfragen von Clients an andere Server fungiert.'),
            (NULL, 'trace', 't', 'r', 'a', 'c', 'e', '(Teil von Traceroute) Ein Befehl, um den Weg von Datenpaketen im Netzwerk zu verfolgen.'),
            (NULL, 'admin', 'a', 'd', 'm', 'i', 'n', 'Kurzform für den Administrator, der ein System oder Netzwerk verwaltet.'),
            (NULL, 'login', 'l', 'o', 'g', 'i', 'n', 'Der Vorgang der Authentifizierung an einem System mit Anmeldedaten.'),
            (NULL, 'frame', 'f', 'r', 'a', 'm', 'e', 'Ein Datenpaket auf der Sicherungsschicht (Schicht 2) des OSI-Modells.'),
            (NULL, 'route', 'r', 'o', 'u', 't', 'e', 'Der definierte Weg, den Datenpakete durch ein Netzwerk nehmen.'),
            (NULL, 'paket', 'p', 'a', 'k', 'e', 't', 'Eine formatierte Dateneinheit, die über ein Netzwerk gesendet wird.'),
            (NULL, 'ports', 'p', 'o', 'r', 't', 's', 'Logische Endpunkte einer Verbindung, die Diensten zugeordnet sind (z.B. Port 80 für HTTP)'),
            (NULL, 'hosts', 'h', 'o', 's', 't', 's', 'Geräte (wie Computer oder Server), die in ein Netzwerk eingebunden sind.'),
            (NULL, 'email', 'e', 'm', 'a', 'i', 'l', 'Elektronische Post, ein grundlegender Dienst in Netzwerken.'),
            (NULL, 'array', 'a', 'r', 'r', 'a', 'y', 'Eine Datenstruktur, die eine feste Anzahl von Elementen desselben Typs speichert.'),
            (NULL, 'debug', 'd', 'e', 'b', 'u', 'g', 'Der Prozess des Suchens, Findens und Behebens von Fehlern (Bugs) im Code.'),
            (NULL, 'float', 'f', 'l', 'o', 'a', 't', 'Ein Datentyp zur Speicherung von Gleitkommazahlen (z.B. 3.14).'),
            (NULL, 'logik', 'l', 'o', 'g', 'i', 'k', 'Die festgelegte Abfolge von Bedingungen und Anweisungen in einem Programm.'),
            (NULL, 'shell', 's', 'h', 'e', 'l', 'l', 'Eine textbasierte Benutzeroberfläche zur Interaktion mit dem Betriebssystem.'),
            (NULL, 'while', 'w', 'h', 'i', 'l', 'e', 'Ein Schlüsselwort, das eine Schleife einleitet, die läuft, solange eine Bedingung wahr ist.'),
            (NULL, 'error', 'e', 'r', 'r', 'o', 'r', '(Englisch für) Ein Fehler, der während der Programmausführung auftritt.'),
            (NULL, 'alias', 'a', 'l', 'i', 'a', 's', 'Ein alternativer, oft kürzerer Name für einen Befehl oder eine Ressource.'),
            (NULL, 'final', 'f', 'i', 'n', 'a', 'l', 'Ein Schlüsselwort (z.B. in Java), das eine Variable konstant oder eine Klasse unveränderbar macht.'),
            (NULL, 'catch', 'c', 'a', 't', 'c', 'h', '(Teil von Try-Catch) Ein Block zur Fehlerbehandlung, der einen ausgelösten "Error" abfängt.'),
            (NULL, 'break', 'b', 'r', 'e', 'a', 'k', 'Ein Befehl, um die Ausführung einer Schleife oder eines Switch-Blocks sofort zu beenden.'),
            (NULL, 'stack', 's', 't', 'a', 'c', 'k', 'Ein Last-In-First-Out (LIFO) Datenspeicher, der oft für Funktionsaufrufe genutzt wird'),
            (NULL, 'queue', 'q', 'u', 'e', 'u', 'e', 'Ein First-In-First-Out (FIFO) Datenspeicher, oft als Warteschlange verwendet.'),
            (NULL, 'build', 'b', 'u', 'i', 'l', 'd', 'Der Prozess, bei dem Quellcode in ein ausführbares Programm umgewandelt (kompiliert) wird.'),
            (NULL, 'merge', 'm', 'e', 'r', 'g', 'e', '(Englisch für) Das Zusammenführen von verschiedenen Entwicklungszweigen (z.B. in Git).'),
            (NULL, 'regex', 'r', 'e', 'g', 'e', 'x', 'Kurz für "Regular Expression", ein Muster zur Suche und Manipulation von Text.'),
            (NULL, 'batch', 'b', 'a', 't', 'c', 'h', '(Englisch für) Stapelverarbeitung, bei der mehrere Aufträge nacheinander abgearbeitet werden.'),
            (NULL, 'cache', 'c', 'a', 'c', 'h', 'e', 'Ein schneller Pufferspeicher, der häufig benötigte Daten für schnellen Zugriff bereithält.'),
            (NULL, 'macro', 'm', 'a', 'c', 'r', 'o', 'Eine aufgezeichnete Abfolge von Befehlen, die zur Automatisierung wiederholt abgespielt werden kann.'),
            (NULL, 'patch', 'p', 'a', 't', 'c', 'h', 'Eine kleine Software-Korrektur, die einen spezifischen Fehler oder eine Sicherheitslücke behebt.'),
            (NULL, 'datei', 'd', 'a', 't', 'e', 'i', 'Eine Sammlung von zusammengehörigen Daten, die unter einem Namen gespeichert ist.'),
            (NULL, 'daten', 'd', 'a', 't', 'e', 'n', 'Rohinformationen, die verarbeitet, gespeichert oder übertragen werden.'),
            (NULL, 'index', 'i', 'n', 'd', 'e', 'x', 'Eine Datenstruktur in Datenbanken, die den Suchzugriff auf Tabellenzeilen beschleunigt.'),
            (NULL, 'query', 'q', 'u', 'e', 'r', 'y', '(Englisch für) Eine spezifische Abfrage, um Daten aus einer Datenbank abzurufen oder zu ändern.'),
            (NULL, 'zeile', 'z', 'e', 'i', 'l', 'e', 'Ein einzelner Datensatz (auch Tupel genannt) in einer Datenbanktabelle.'),
            (NULL, 'tulpe', 't', 'u', 'l', 'p', 'e', 'Ein Synonym für "Zeile" oder "Datensatz" in einer relationalen Datenbank.');"""

        try:
            cursor.execute(sql_command)
            connection.commit()
            connection.close()
            print("Datenbank ist bereit.")
        except:
            print("Etwas ist Fehlgeschlagen.")
            
        sql_command = """INSERT INTO user (id, benutzername, passwort) VALUES (NULL, 'Admin', '1202')"""
        
        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()
        try:
            cursor.execute(sql_command)
            connection.commit()
            connection.close()
            print("Datenbank ist bereit.")
        except:
            print("Etwas ist Fehlgeschlagen.")
        
    def eigenes_wordle_alle_anzeigen(self):
        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM eigene_Woerter") 
        print("Alle Wörter:")
        result = cursor.fetchall() 
        for r in result:
            print(f"ID: {r[0]}, Wort: {r[1]}, Erklärung: {r[7]}")
        connection.close()
    
    def eigenes_wordle_neues_wort(self, pWort, pErklärung):
        pWort = pWort.lower()
        pBuchstaben = list(pWort)
        sql_command = f"""INSERT INTO eigene_Woerter (id, wort, L1, L2, L3, L4, L5, erklärung) 
        VALUES  (NULL, '{pWort}', '{pBuchstaben[0]}', '{pBuchstaben[1]}', '{pBuchstaben[2]}', '{pBuchstaben[3]}', '{pBuchstaben[4]}', '{pErklärung}');"""

        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()
        
        try:
            cursor.execute(sql_command)
            connection.commit()
            print("Neue Eigene Wörter Datenbank:")
            self.eigenes_wordle_alle_anzeigen()
        except sqlite3.Error as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            connection.rollback()
        
        connection.close()

    def eigenes_wordle_wort_verändern(self, pID, pWort, pErklärung):
        neues_wort = pWort.lower()
        pBuchstaben = list(pWort)
        neue_erklärung = pErklärung
        sql_command = f"UPDATE eigene_Woerter SET wort = ?, L1 = ?, L2 = ?, L3 = ?, L4 = ?, L5 = ?, erklärung = ? WHERE id = ?;"
        daten_fuer_update = (
            neues_wort,
            pBuchstaben[0],
            pBuchstaben[1],
            pBuchstaben[2],
            pBuchstaben[3],
            pBuchstaben[4],
            neue_erklärung,
            pID
        )

        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()
        try:
            cursor.execute(sql_command, daten_fuer_update)
            connection.commit()
            print("Neue Eigene Wörter Datenbank:")
            self.eigenes_wordle_alle_anzeigen()
        except sqlite3.Error as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            connection.rollback()
        
        connection.close()

    def eigenes_wordle_wort_löschen(self, pID):
        sql_command = """DELETE FROM eigene_Woerter WHERE id = ?;"""
        
        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()
        try:
            cursor.execute(sql_command, pID)
            connection.commit()
            print("Neue Eigene Wörter Datenbank:")
            self.eigenes_wordle_alle_anzeigen()
        except sqlite3.Error as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            connection.rollback()
        
        connection.close()
   
    def eigenes_wordle_ein_wort_anzeigen(self, pID):
        sql_command = """SELECT * FROM eigene_Woerter WHERE id = ?;"""
        
        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()
        try:
            cursor.execute(sql_command, pID)
            r = cursor.fetchone()
            print(f"ID: {r[0]}, Wort: {r[1]}, Erklärung: {r[7]}")
        except sqlite3.Error as e:
            print(f"Ein Fehler ist aufgetreten: {e}")
            connection.rollback()
        
        connection.close()      

    def get_user(self):
        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()
        
        cursor.execute("SELECT * FROM user")
        #Temp
        result = cursor.fetchone()
        return result

class Colors:
    # Definition einiger gängiger Farbcodes
    RED = '\033[91m'        # Farbe: Rot
    GREEN = '\033[92m'      # Farbe: Grün
    YELLOW = '\033[93m'     # Farbe: Gelb
    BLUE = '\033[94m'       # Farbe: Blau
    RESET = '\033[0m'       # Setzt alle Formatierungen zurück

class Wordle:
    def itWordle(self):
        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()

        #Zufähliges Wort aus der Datenbank ziehen
        zufällige_zahl = random.randint(0, 50)
        cursor.execute(f"SELECT * FROM ITWoerter WHERE id IS {zufällige_zahl}")
        aktueller_Datensatz = cursor.fetchone()

        #Parameter aus der Datenbank verarbeitbar machen
        wort = aktueller_Datensatz[1]
        L1 = aktueller_Datensatz[2]
        L2 = aktueller_Datensatz[3]
        L3 = aktueller_Datensatz[4]
        L4 = aktueller_Datensatz[5]
        L5 = aktueller_Datensatz[6]
        buchstaben = [L1, L2, L3, L4, L5]
        erklärung = aktueller_Datensatz[7]


        #print(f"Aktueller Datensatz: {aktueller_Datensatz}. Aktuelles Wort: {wort}. Buchstaben: {L1},{L2},{L3},{L4},{L5}. Erklärung: {erklärung}")


        print(f"Woerdle: [ ][ ][ ][ ][ ]")

        gewonnen = False

        for j in range(5):
            eingabe = ""
            while True:
                eingabe = input("Eingabe: ")
                if len(eingabe) == 5:
                    break
                else:
                    print(f"Fehler: Du hast {len(eingabe)} Zeichen eingegeben. Es müssen genau 5 sein.")

            pL1 = eingabe[0].lower()
            pL2 = eingabe[1].lower()
            pL3 = eingabe[2].lower()
            pL4 = eingabe[3].lower()
            pL5 = eingabe[4].lower()
            eingegbene_Buchstaben = [pL1, pL2, pL3, pL4, pL5]

            cL1 = ""
            cL2 = ""
            cL3 = ""
            cL4 = ""
            cL5 = ""
            farben_Buchstaben = [cL1, cL2, cL3, cL4, cL5]

            for i in range(len(eingegbene_Buchstaben)):
                if eingegbene_Buchstaben[i] == buchstaben[i]:
                    farben_Buchstaben[i] = Colors.GREEN
                elif eingegbene_Buchstaben[i] in buchstaben:
                    farben_Buchstaben[i] = Colors.YELLOW
                else:
                    farben_Buchstaben[i] = Colors.RED
            
            farb_check = 0
            for i in range(len(farben_Buchstaben)):
                if farben_Buchstaben[i] == Colors.GREEN:
                    farb_check += 1
            if farb_check == 5:
                gewonnen = True
                break

            print(f"Ausgabe: [{farben_Buchstaben[0]}{eingegbene_Buchstaben[0]}{Colors.RESET}][{farben_Buchstaben[1]}{eingegbene_Buchstaben[1]}{Colors.RESET}][{farben_Buchstaben[2]}{eingegbene_Buchstaben[2]}{Colors.RESET}][{farben_Buchstaben[3]}{eingegbene_Buchstaben[3]}{Colors.RESET}][{farben_Buchstaben[4]}{eingegbene_Buchstaben[4]}{Colors.RESET}]")

        if gewonnen:
            print(f"Das war das richtige Wort: [{farben_Buchstaben[0]}{eingegbene_Buchstaben[0]}{Colors.RESET}], [{farben_Buchstaben[1]}{eingegbene_Buchstaben[1]}{Colors.RESET}], [{farben_Buchstaben[2]}{eingegbene_Buchstaben[2]}{Colors.RESET}], [{farben_Buchstaben[3]}{eingegbene_Buchstaben[3]}{Colors.RESET}], [{farben_Buchstaben[4]}{eingegbene_Buchstaben[4]}{Colors.RESET}]")
            print(f"Hier eine erklärung zu dem Wort: {erklärung}")
        else:
            print(f"Leider hast waren deine eingaben alle nicht das Wort!")
            print(f"Das Wort wäre {Colors.BLUE}{wort}{Colors.RESET} gewesen.")
    
    def eigenes_Wordle(self):
        connection = sqlite3.connect("ITWordle.db")
        cursor = connection.cursor()

        sql_command = "SELECT MAX(id) FROM eigene_woerter;"
        cursor.execute(sql_command)
        max_id = cursor.fetchone()[0]
        #Zufähliges Wort aus der Datenbank ziehen
        zufällige_zahl = random.randint(0, max_id)
        cursor.execute(f"SELECT * FROM eigene_woerter WHERE id IS {zufällige_zahl}")
        aktueller_Datensatz = cursor.fetchone()

        #Parameter aus der Datenbank verarbeitbar machen
        wort = aktueller_Datensatz[1]
        L1 = aktueller_Datensatz[2]
        L2 = aktueller_Datensatz[3]
        L3 = aktueller_Datensatz[4]
        L4 = aktueller_Datensatz[5]
        L5 = aktueller_Datensatz[6]
        buchstaben = [L1, L2, L3, L4, L5]
        erklärung = aktueller_Datensatz[7]


        #print(f"Aktueller Datensatz: {aktueller_Datensatz}. Aktuelles Wort: {wort}. Buchstaben: {L1},{L2},{L3},{L4},{L5}. Erklärung: {erklärung}")


        print(f"Woerdle: [ ][ ][ ][ ][ ]")

        gewonnen = False

        for j in range(5):
            eingabe = ""
            while True:
                eingabe = input("Eingabe: ")
                if len(eingabe) == 5:
                    break
                else:
                    print(f"Fehler: Du hast {len(eingabe)} Zeichen eingegeben. Es müssen genau 5 sein.")

            pL1 = eingabe[0].lower()
            pL2 = eingabe[1].lower()
            pL3 = eingabe[2].lower()
            pL4 = eingabe[3].lower()
            pL5 = eingabe[4].lower()
            eingegbene_Buchstaben = [pL1, pL2, pL3, pL4, pL5]

            cL1 = ""
            cL2 = ""
            cL3 = ""
            cL4 = ""
            cL5 = ""
            farben_Buchstaben = [cL1, cL2, cL3, cL4, cL5]

            for i in range(len(eingegbene_Buchstaben)):
                if eingegbene_Buchstaben[i] == buchstaben[i]:
                    farben_Buchstaben[i] = Colors.GREEN
                elif eingegbene_Buchstaben[i] in buchstaben:
                    farben_Buchstaben[i] = Colors.YELLOW
                else:
                    farben_Buchstaben[i] = Colors.RED
            
            farb_check = 0
            for i in range(len(farben_Buchstaben)):
                if farben_Buchstaben[i] == Colors.GREEN:
                    farb_check += 1
            if farb_check == 5:
                gewonnen = True
                break

            print(f"Ausgabe: [{farben_Buchstaben[0]}{eingegbene_Buchstaben[0]}{Colors.RESET}][{farben_Buchstaben[1]}{eingegbene_Buchstaben[1]}{Colors.RESET}][{farben_Buchstaben[2]}{eingegbene_Buchstaben[2]}{Colors.RESET}][{farben_Buchstaben[3]}{eingegbene_Buchstaben[3]}{Colors.RESET}][{farben_Buchstaben[4]}{eingegbene_Buchstaben[4]}{Colors.RESET}]")

        if gewonnen:
            print(f"Das war das richtige Wort: [{farben_Buchstaben[0]}{eingegbene_Buchstaben[0]}{Colors.RESET}], [{farben_Buchstaben[1]}{eingegbene_Buchstaben[1]}{Colors.RESET}], [{farben_Buchstaben[2]}{eingegbene_Buchstaben[2]}{Colors.RESET}], [{farben_Buchstaben[3]}{eingegbene_Buchstaben[3]}{Colors.RESET}], [{farben_Buchstaben[4]}{eingegbene_Buchstaben[4]}{Colors.RESET}]")
            print(f"Hier eine erklärung zu dem Wort: {erklärung}")
        else:
            print(f"Leider hast waren deine eingaben alle nicht das Wort!")

class Verwaltung:

    def first_time(self):
        print(f"""=============================================================
Wird dieses Programm das erstemal auf dem gerät ausgeführt?:
{Colors.RED}(Wenn Sie Ja auswählern werden die Wörte im eigenen Wordle gelöscht){Colors.RESET}
              
JA (1):
NEIN (2):
              """)
        x = input("Eingabe: ")
        match x.lower():
            case "ja" | "1":
                SQL().first_time()
            case "nein" | "2":
                print("")
            case _:
                print("")
                print(f"{Colors.RED} Eingabe Ungültig!{Colors.RESET}")
                print("")
                time.sleep(5)
                self.first_time()
        
    def menu(self):
        print(f"""======================================================
                    IT-Wordle:
IT-Wordle (1):
Eigenes Wordle (2):
Einstellungen (3):
Beenden (4):
              """)
        x = input("Eingabe: ")
        match x.lower():
            case "it-wordle" | "itwordle" | "1":
                Wordle().itWordle()
                time.sleep(10)
                self.menu()

            case "eigenes Wordle" | "eigeneswordle" | "2":
                self.eigenes_Wordle_options()
                time.sleep(5)
                self.menu()

            case "einstellung" | "3":
                self.einstellung()
                time.sleep(5)
                self.menu()

            case "beenden" | "4":
                print("Programm wird Beendet!")
                exit

            case _:
                print("")
                print(f"{Colors.RED}Eingabe Ungültig!{Colors.RESET}")
                print("")
                time.sleep(5)
                self.menu()
    
    def eigenes_Wordle_options(self):
        print(f"""======================================================
                Eigenes Wordle:
Eigenes Wordle (1):
Verwaltung eigener Wörter (2):
Zurück (3):
              """)
        x = input("Eingabe: ")
        match x.lower():
            case "eigenes wordle" | "1":
                try:
                    Wordle().eigenes_Wordle()
                except:
                    print("")
                    print(f"{Colors.RED}Ein Fehler ist aufgetreten!{Colors.RESET}")
                    print("")
                    self.eigenes_Wordle_options()
                time.sleep(10)
                self.menu()
            
            case "verwaltung eigener wörter" | "verwaltung" | "2":
                self.verwaltung_eigener_wörter()
            
            case "zurück" | "back" | "3":
                self.menu()

            case _:
                print(f"{Colors.RED} Eingabe Ungültig! {Colors.RESET}")
                self.eigenes_Wordle_options()

    def verwaltung_eigener_wörter(self):
            print(f"""======================================================
                Verwaltung eigener Wörter:
Alle Wörter Anzeigen (1):
Neues Wort hinzufügen (2):
Wort verändern (3):
Wort löschen (4):
Zurück (5):
              """)
            x = input("Eingabe: ")
            match x.lower():
                case "alle wörter anzeigen" | "alle wörter" | "1":
                    SQL().eigenes_wordle_alle_anzeigen()
                    self.verwaltung_eigener_wörter()

                case "neues wort hinzufügen" | "neues wort" | "2":
                    wort = ""
                    while True:
                        wort = input("Gib das neue Wort ein (5 Buchstaben): ")
                        if len(wort) == 5:
                            break
                        else:
                            print(f"Fehler: Du hast {len(wort)} Zeichen eingegeben. Es müssen genau 5 sein.")
                    erklärung = input("Erklärung zum Wort Eingeben: ")
                    SQL().eigenes_wordle_neues_wort(wort, erklärung)
                    self.verwaltung_eigener_wörter()
                
                case "wort verändern" | "3":
                    SQL().eigenes_wordle_alle_anzeigen()
                    id = input("Gib die ID des Wortes ein das du verändern möchtest: ")
                    wort = ""
                    while True:
                        wort = input("Gib das 5Buchstaben-Wort ein (auch wenn unverändert): ")
                        if len(wort) == 5:
                            break
                        else:
                            print(f"Fehler: Du hast {len(wort)} Zeichen eingegeben. Es müssen genau 5 sein.")
                    erklärung = input("Gib die Erklärung ein (auch wenn unverändert): ")
                    SQL().eigenes_wordle_wort_verändern(id, wort, erklärung)
                    self.verwaltung_eigener_wörter()

                case "wort löschen" | "lösche" | "4":
                    user = input("Benutzername: ")
                    passwort = getpass("Passwort: ")
                    if self.sperre_admin(user, passwort):    
                        #SQL().eigenes_wordle_alle_anzeigen()
                        #id = input("Gib die ID des Wortes ein das du verändern möchtest: ")
                        #print("Ausgewähltes Wort: ")
                        #SQL().eigenes_wordle_ein_wort_anzeigen(id)
                        #check = input("Geben sie bitte BESTÄTIGEN ein wenn sie dieses Wort löschen möchten oder Abrechen um abzubrechen: ")
                        #while True:
                        #    if check == "BESTÄTIGEN":
                        #        SQL().eigenes_wordle_wort_löschen(id)
                        #        SQL().eigenes_wordle_alle_anzeigen()
                        #        break
                        #    elif check.lower() == "abrechen":
                        #        self.verwaltung_eigener_wörter()
                        #        break
                        print("Test Erfolgreich")
                    else:
                        print("Sie haben nicht die Berrechtigung diese Einstellung vorzunehmen! Die Funktion wird bald verfügbar sein.")
                    self.verwaltung_eigener_wörter()                    
                
                case "zurück" | "5":
                    self.eigenes_Wordle_options()
                case _:
                    print(f"{Colors.RED} Eingabe Ungültig! {Colors.RESET}")
                    self.verwaltung_eigener_wörter()

    def einstellung(self):
        user = input("Benutzername: ")
        passwort = getpass("Passwort: ")
        if self.sperre_admin(user, passwort):    
            print("Test Erfolgreich")
        else:
            print("Sie haben nicht die Berrechtigung diese Einstellung vorzunehmen! Die Funktion wird bald verfügbar sein.")
        self.verwaltung_eigener_wörter()
    
    def sperre_admin(self, pUser, pPasswort):
        account = SQL().get_user()
        if pUser == account[1] and pPasswort == account[2]:
            return True
        else:
            return False



v = Verwaltung()
v.first_time()
v.menu()
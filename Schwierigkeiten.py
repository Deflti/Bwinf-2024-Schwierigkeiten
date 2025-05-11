class Solution:
    def bestimme_schwierigkeiten(self, pDateipfad: str) -> None:
        with open(pDateipfad, "r") as datei:
            zeilen = datei.readlines()

        # Entferne Leerzeichen und Zeilenumbrüche
        zeilen = [zeilen[i].strip() for i in range(len(zeilen))]

        # Setzt die ersten Werte n, m und k auf die vorgegebenen Werte in Zeile 1 der Text Datei (m und n werden nicht genutzt)
        n, m, k = [int(x) for x in zeilen[0].split()]

        # Liste der anzuordnenden Aufgaben
        anzuordnende_aufgaben = zeilen[-1].split(" ")

        # Entferne die erste Zeile und die letzte Zeile (mit den guten Aufgaben)
        zeilen.pop(0)
        zeilen.pop(-1)

        # Schwierigkeit zuweisen: Start mit Schwierigkeit 1
        schwierigkeiten = {}

        # Initialisiere alle Aufgaben in der Schwierigkeitstabelle
        for zeile in zeilen:
            aufgaben = zeile.split(" < ")
            for aufgabe in aufgaben:
                if aufgabe not in schwierigkeiten:
                    schwierigkeiten[aufgabe] = 1  # Setze Standardwert 1

        # Iteriere 1-mal durch alle Klausuren, um die Schwierigkeitsränge zu korrigieren
        for zeile in zeilen:
            # Liste der Aufgaben
            aufgaben = zeile.split(" < ")
        
            # Laenge der Aufgaben
            laenge_aufgaben = len(aufgaben)
        
            # Vergleiche alle Aufgaben in der Zeile
            for i in range(laenge_aufgaben-1):
                # Aufgabe rechts soll schwieriger sein als Aufgabe links
                schwierigkeit_links = schwierigkeiten[aufgaben[i]]
                schwierigkeit_rechts = schwierigkeiten[aufgaben[i + 1]]
            
                # Setze die Schwierigkeit der rechten Aufgabe auf mindestens die der linken + 1
                if schwierigkeit_rechts <= schwierigkeit_links:
                    schwierigkeiten[aufgaben[i + 1]] = schwierigkeit_links + 1

        # Liste von benutzen Schluesseln
        benutzte_schluessel = []

        # findet einen Schluessel basierend auf dem Wert, der zum Schluessel gehört
        def finde_schluessel_durch_schwierigkeit(dict_obj, ziel_schwierigkeit):
            for schluessel, schwierigkeit in dict_obj.items():
                # Ueberprüft, ob die Schwierigkeit der Zielschwierigkeit entspricht, 
		        # der Schlüssel in den zuzuordnenden Aufgaben enthalten ist und 
		        # noch nicht verwendet wurde
                if schwierigkeit == ziel_schwierigkeit and schluessel in anzuordnende_aufgaben and schluessel not in benutzte_schluessel:
                    # Der Schluessel schluessel wird an die Liste benutzte_schluessel angehangen und anschließend zurueckgegeben
                    benutzte_schluessel.append(schluessel)
                    return schluessel
            # Es wird None zurueckgegeben, wenn die Zielschwierigkeit mit keinem der Schluessel uebereinstimmt
            return None

        # Eine Ranking Liste wird erstellt, welche Schwierigkeiten von den zuanordnen Aufgaben in die ranking Liste aufnimmt 
        ranking = [schwierigkeiten[anzuordnende_aufgaben[i]] for i in range(k)]

        # Ein String namens valides_ranking wird erstellt
        valide_Klausur: str = ""
  
        # Die ranking Liste wird sortiert, sodass die kleinste Zahl am Anfang der Liste steht 
        ranking.sort()

        # Bildet den String valide_Klausur, indem der schluessel durch den Wert von ranking[i] gefunden wird
        for i in range(k):
            if i != k - 1:
                valide_Klausur += finde_schluessel_durch_schwierigkeit(schwierigkeiten, ranking[i]) + "; "
            else:
                valide_Klausur += finde_schluessel_durch_schwierigkeit(schwierigkeiten, ranking[i])

        # Gibt das finale Schwierigkeitsranking aus
        print(f"Schwierigkeitsranking der Aufgaben: {sorted(schwierigkeiten.items(), key=lambda x: x[1])}")

        # Gibt eine valide Klausur aus
        print(f"Valide Anordnung: {valide_Klausur}")

if __name__ == "__main__":
    Solution().bestimme_schwierigkeiten("Eingabe.txt")
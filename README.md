# Schwierigkeitssortierung für Klausuraufgaben

## Projektbeschreibung

**Dua L. Graph**, eine Informatiklehrerin, möchte ihre Klausuraufgaben automatisiert nach Schwierigkeit sortieren. Über die Jahre hinweg hat sie aus früheren Prüfungen abgeleitet, welche Aufgaben leichter oder schwerer waren. Ziel dieses Projekts ist es, ein Programm bereitzustellen, das anhand solcher historischer Relationen (z. B. `A < B < C`) eine konsistente Schwierigkeitsskala berechnet und eine valide, konfliktfreie Anordnung für neue Klausuren erzeugt.

## Motivation

Manuelle Sortierung der Aufgaben ist fehleranfällig und zeitaufwendig – insbesondere, wenn Widersprüche zwischen verschiedenen Quellen auftreten. Dieses Tool analysiert alle verfügbaren Relationen und erstellt eine konsistente Reihenfolge von Aufgaben. Konflikte (z. B. `F < G` in einer Klausur, aber `G < F` in einer anderen) werden automatisch aufgelöst, indem die Reihenfolge der zuletzt betrachteten Klausur als maßgeblich angenommen wird.

## Funktionsweise

1. **Dateieingabe**  
   Die Eingabedatei (`Eingabe.txt`) enthält:
   - In der ersten Zeile: drei Ganzzahlen `n m k` (nur `k` ist relevant).
   - Dann mehrere Zeilen mit `<`-Relationen zwischen Aufgaben.
   - In der letzten Zeile: `k` Aufgaben, die in die neue Klausur aufgenommen werden sollen.

2. **Schwierigkeitsbestimmung**  
   - Jede Aufgabe startet mit Schwierigkeitswert 1.
   - Die Relationen der Form `A < B` werden interpretiert als „B ist schwieriger als A“.
   - Die Schwierigkeitswerte werden iterativ so angepasst, dass sie alle Bedingungen erfüllen.

3. **Konfliktauflösung**  
   - Gibt es widersprüchliche Anforderungen (Konflikte), wird die zuletzt gelesene Relation bevorzugt.

4. **Sortierung und Ausgabe**  
   - Aufgaben werden nach Schwierigkeitswert sortiert.
   - Die finale Klausur besteht aus den `k` gewünschten Aufgaben in dieser Reihenfolge.

## Beispielausgabe

```txt
16 26 5
A < B < C < D < E < J < I
B < C < E < D < I < H < K
S < G < H < I < J 
G < H < S < O
M < N < O < K
K < O < M
P < Q < R < F < N < M
S < F < P < N < K
F < T < U
V < W < T < Z
Y < X < Z < T
Z < W < T < V < T < U
K < W < Z < Y
A < B < D < E < W < Z < X < Y < U
R < Q < K < L
P < F < K < O < X < W
B W I N F
Schwierigkeitsranking der Aufgaben: [('A', 1), ('B', 2), ('G', 2), ('C', 3), ('R', 3), ('Q', 4), ('D', 6), ('E', 7), ('H', 8), ('I', 9), ('S', 9), ('J', 10), ('P', 11), ('N', 12), ('F', 12), ('K', 13), ('M', 13), ('O', 14), ('L', 14), ('V', 15), ('Z', 15), ('T', 16), ('X', 16), ('W', 17), ('Y', 17), ('U', 18)]
Valide Anordnung: B; I; N; F; W

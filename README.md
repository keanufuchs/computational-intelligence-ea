# TSP mit Evolutionären Algorithmen

Dieses Projekt implementiert einen evolutionären Algorithmus zur Lösung des **Traveling Salesman Problems (TSP)** am Beispiel von 6 Städten im Rheinland.

## Inhalt

Das Jupyter Notebook `tsp_evolutionary_algorithm.ipynb` enthält:

1. **Einleitung**: Das TSP als kombinatorisches Optimierungsproblem
2. **Kodierung**: Permutationsdarstellung (Genotyp vs. Phänotyp)
3. **Fitness-Funktion**: Pfadlänge als Gütemaß
4. **Selektionsmethoden**: Tournament Selection und Elitismus
5. **Variationsoperatoren**: Invertierende Mutation und Order Crossover
6. **Evolutionärer Zyklus**: Kompletter EA mit Animation
7. **Statistische Auswertung**: 30 Testläufe mit Boxplots und Konvergenzgrafiken

## Installation

```bash
pip install -r requirements.txt
```

## Ausführung

```bash
jupyter notebook tsp_evolutionary_algorithm.ipynb
```

## Verwendete Städte

- Köln
- Bonn
- Düsseldorf
- Aachen
- Wuppertal
- Leverkusen

## Lizenz

Dieses Projekt wurde für Lehr- und Präsentationszwecke erstellt.


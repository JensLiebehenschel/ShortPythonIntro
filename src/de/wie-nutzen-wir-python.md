# Wie nutzen wir Python?
(Klicken Sie [hier](https://jensliebehenschel.github.io/ShortPythonIntro/en/how-do-we-use-python.html) für die englische Version dieser Seite)

## Not very "pythonic"

Als Beschreibung der Python-Programme in dieser Einführung werden Sie eventuell die Bezeichnung "Not very pythonic" hören.
Dies bedeutet, dass die Programme so geschrieben sind, dass sie die Stärken von Python nicht völlig ausnutzen und dementsprechend sich "das Leben schwerer machen". Dies ist erforderlich, um die Konzepte zu behandeln, ohne sich auf den Luxus von Python zu verlassen.

Um dies an einem Beispiel klar zu machen:
In Python gibt es in der Standardbibliothek die Funktion <code>sort()</code>.
Diese Methode sortiert automatisch eine gegebene Liste.
Bei Algorithmen und Datenstrukturen werden verschiedene Sortieralgorithmen behandelt, um verschiedene Entwurfsprinzipien für Algorithmen zu veranschaulichen. 
Somit können wir die <code>sort()</code>-Funktion nicht nutzen.

Theoretisch könnte also jeder Sortieralgorithmus durch die Zeile 
```Python
listen_name.sort()
```
ersetzen werden und das Gleiche erzielen.
Ziel ist vielmehr eine Funktion wie <code>sort()</code> selbst schreiben zu können,
sowohl um die Konzepte zu verstehen, als auch um Analysen (beispielsweise der Laufzeit) durchführen zu können.

Sortieren ist nicht der einzige Aspekt, welcher in Python niederschwellig bereitgestellt wird.
So wird etwa die Datenstruktur "Hashing" in Python als sogenannte "Dictionaries" umgesetzt.

## Als Python Entwickler geht man anders vor als es beim Lernen gewollt ist

Da etwa die <code>sort()</code> Funktion der Python Standardbibliothek zusätzlich in C++, also einer schnelleren Programmiersprache als Python selbst, geschrieben ist, kann man in Python nicht wirklich effizienter und schneller sortieren als die Funktion <code>sort()</code> zu benutzen.

Daher sollte man als Python-Entwickler in der Regel nie einen eigenen Algorithmus zum Sortieren schreiben, sondern sich auf die <code>sort()</code> Funktion verlassen.
Gleiches gilt auch für das Finden des größten Wertes einer Liste.
Dort ist es ebenfalls am effizientesten, die Funktion <code>max()</code> zu benutzen, anstatt es manuell mit einer Schleife zu lösen.

Hier geht es jedoch nicht darum, Python-Entwicklung zu lernen, sondern um das Verständnis von den jeweiligen Algorithmen und Datenstrukturen.
Deshalb "Not very pythonic"!
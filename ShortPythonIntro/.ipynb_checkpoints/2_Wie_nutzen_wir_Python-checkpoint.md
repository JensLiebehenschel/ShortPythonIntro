# Wie nutzen wir Python?

## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

## Not very "pythonic"

Als Beschreibung der Python-Codes in diesem Modul werden Sie eventuell die Bezeichnung "Not very pythonic" hören.
Dies bedeutet, dass die Programme so geschrieben sind, dass sie die Stärken von Python nicht völlig ausnutzen und dementsprechend sich "das Leben schwerer machen", um die behandelten Konzepte beizubringen, ohne sich auf den Luxus von Python zu verlassen.

Um an einem Beispiel klar zu machen, worum es hier geht:
In Python gibt es in der Standardbibliothek die Funktion <code>sort()</code>.
Diese Methode sortiert automatisch eine gegebene Liste.
Sie sollen nun aber lernen wie man mit verschiedenen Algorithmen eben diese Sortierung selbst machen kann.

Sie könnten theoretisch in jedem Python-Code dieser Veranstaltung, den gesamten Sortieralgorithmus durch die Zeile 
```Python
ArrayNameHier.sort()
```
ersetzen und das Gleiche erzielen.
Ist wie gesagt, jedoch nicht Sinn der Sache.
Ziel ist es also eine Funktion wie <code>sort()</code> selbst schreiben zu können.
Zumindest vom Resultat her.

## Als Python Entwickler geht man anders vor als es in AlgDat gewollt ist

Da etwa die <code>sort()</code> Funktion der Python Standardbibliothek zusätzlich in C++, also einer schnelleren Programmiersprache als Python selbst, geschrieben ist, kann man in Python nicht wirklich effizienter und schneller sortieren als die Funktion <code>sort()</code> zu benutzen.

Daher sollte man als Python-Entwickler in der Regel nie einen eigenen Algorithmus zum sortieren schreiben, sondern sich auf die <code>sort()</code> Funktion verlassen.
Gleiches gilt auch etwa für das finden des höchsten Wertes in einer Liste.
Dort ist es ebenfalls am effizientesten, die Funktion <code>max()</code> zu benutzen, anstatt es manuell mit einer Schleife zu lösen.

Hier geht es jedoch nicht darum zu lernen, ein Python-Entwickler zu werden, sondern um das Verständnis der Algorithmen.
Deshalb "Not very pythonic"!
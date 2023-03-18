# Output und Input

## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

## Ausgabe
Wie auch in anderen Programmiersprachen, ist die Ein- und Ausgabe in einem Terminalfenster essenziell. Zumindest für die meisten Programme im Kontext des Studiums.

Um in Python etwas in ein Terminalfenster ausgeben zu können, wird die Funktion <code>print()</code> benutzt.
```Python
# Einen Namen ausgeben
name = "Max Mustermann"
print(name)
# Max Mustermann
```
Die <code>print()</code> Funktion kann auch mehrere Parameter entgegennehmen.
In diesem Fall werden die gegebenen Parameter mit einem Leerzeichen dazwischen konkateniert.
```Python
# Ein etwas komplexeres print()
name1 = "Max Mustermann"
name2 = "John Doe"
print(name1, "ist mit", name2, "befreundet.")
# Max Mustermann ist mit John Doe befreundet.
```
Am Ende der <code>print()</code> Funktion, wird automatisch ein Zeilenumbruch hinzugefügt.
Sprich der Input
```Python
print(1)
print(2)
print(3)
```
führt zum Output
```Python
1
2
3
```
anstatt zum Output
```Python
123
```


## Eingabe
Wie man in Python vom Standardinput aus einem Terminal einlesen kann, wird in dieser Einführung nicht behandelt.
Stattdessen wäre es erstmal am einfachsten, bestimmte Werte zu hardcoden.

Wenn man nun die Funktion <code>foo(x)</code> testen möchte, so kann man davor einfach x einen Wert zuweisen und dann die Funktion aufrufen.
```Python
x = 5
foo(x)

# oder gleich

foo(5)
```
An Interessierte, verweise ich auf die englischsprachige <a href="https://docs.python.org/3/library/functions.html" target="_blank">Python Referenz</a>, welche über die in Python eingebauten Funktionen informiert.

Alternativ können Sie auch in der Suchmaschine ihrer Wahl danach suchen.
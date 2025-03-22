# Input und Output

## Ausgabe
Wie auch in anderen Programmiersprachen, ist die Ein- und Ausgabe in einem Terminalfenster essenziell. Zumindest für die meisten einfachen Programme.

Um in Python etwas in ein Terminalfenster ausgeben zu können, wird die Funktion <code>print()</code> benutzt.
```Python
name = "Max Mustermann"
print(name)
# --> "Max Mustermann"
```
Die <code>print()</code> Funktion kann auch mehrere Parameter entgegennehmen.
In diesem Fall werden die gegebenen Parameter mit einem Leerzeichen dazwischen konkateniert.
```Python
name1 = "Max Mustermann"
name2 = "John Doe"
print(name1, "ist mit", name2, "befreundet.")
# --> "Max Mustermann ist mit John Doe befreundet."
```
Am Ende der <code>print()</code> Funktion, wird automatisch ein Zeilenumbruch hinzugefügt.
Sprich die folgenden Zeilen
```Python
print(1)
print(2)
print(3)
```
führen zum Ausgabe
```Python
1
2
3
```
statt zu
```Python
123
```


## Eingabe
Wie man in Python von der Standardeingabe aus einem Terminal einlesen kann, wird in dieser Einführung nicht behandelt.
Stattdessen ist es angemessen, bestimmte Werte ins Programm zu schreiben.

Wenn man nun die Funktion <code>foo(x)</code> testen möchte, kann man davor einfach <code>x</code> einen Wert zuweisen und dann die Funktion aufrufen.
```Python
x = 5
foo(x)

# oder gleich

foo(5)
```
An Interessierte, verweisen wir auf die englischsprachige <a href="https://docs.python.org/3/library/functions.html" target="_blank">Python Referenz</a>, welche über die in Python eingebauten Funktionen informiert.

Alternativ können Sie auch in der Suchmaschine ihrer Wahl danach suchen.
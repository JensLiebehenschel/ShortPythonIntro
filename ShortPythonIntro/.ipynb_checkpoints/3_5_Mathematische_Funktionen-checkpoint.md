# Bibliotheken und Mathematische Funktionen

## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

## Importieren einer Bibliothek

Python hat eine enorme Auswahl an Bibliotheken.
Seien es nun Bibliotheken um Grafiken zu erstellen oder Bibliotheken für Machine Learning.

Von Interesse für dieses Modul, sind jedoch mathematische Bibliotheken.
Mit diesen Bibliotheken können wir etwa Funktion verwenden, um eine Quadratwurzel zu ziehen oder einen Logarithmus zu berechnen.

Um diese hilfreichen Funktionen nutzen zu können, muss man diese Bibliotheken erst importieren.
Funktioniert von der Logik genauso wie das importieren von Bilbiotheken in C.
Also gibt es ein Keyword gefolgt vom Bibliothekennamen, daraufhin kann man diese Bibliothek dann nutzen.

in C:
```C
#include <Bibliotheksname.h>
```

in Python wird das Keyword <code>import</code> genutzt:
```Python
import Bibliotheksname
```

Konkret um auf die Funktionen für die Quadratwurzel und die Logarithmen, muss man die Bibliothek <code>math</code> importieren.

Also braucht man die Zeile
```Python
import math
```
bevor man diese Funktionen nutzen kann.


## Funktionen der math Bibliothek

Nun haben wir die math Bibliothek importiert.

Um auf diese zuzugreifen, müssen wir vor den Funktionen einen Präfix von <code>Bibliotheksname.</code> hinzufügen, damit wir ausdrücken, dass wir die Funktion dieser Bibliothek meinen.

Konkret wäre der Präfix hier also <code>math.</code>

Die Quadratwurzel von 25 könnte man also wie folgt berechnen:
```Python
result = math.sqrt(25)
# 5
```

Um den 10-er Logarithmus von x zu berechnen, kann man die Funktion <code>math.log10(x)</code> nutzen
```Python
result = math.log10(100)
# 2
```

Weitere Funktionen wie etwa trigonometrische Funktionen können bei bedarf bei der englischsprachigen <a href="https://docs.python.org/3/library/math.html" target="_blank">Python Referenz</a> nachgelesen werden.
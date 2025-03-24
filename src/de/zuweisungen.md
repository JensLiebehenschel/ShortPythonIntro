# Zuweisungen
(Klicken Sie [hier](https://jensliebehenschel.github.io/ShortPythonIntro/en/assignments-in-python.html) für die englische Version dieser Seite)

## Der Zuweisungsoperator

Wie Sie bereits gesehen haben, ist in Python wie auch in anderen Programmiersprachen <code>&equals;</code> der normale Zuweisungsoperator. Dessen Funktion sollte bekannt sein.

In Python hat dieser jedoch zusätzliche Funktionalität.
Normalerweise hat der Zuweisungsoperator einen Operanden auf der linken Seite und einen Operanden auf der rechten Seite,
also:
```Python
a = b
```

In Python gibt es diese Einschränkung nicht. Es müssen jediglich auf beiden Seiten gleich viele Operanden sein. Somit ist es möglich mit einem Zuweisungsoperator eine Mehrfachzuweisung durchzuführen.
Die Operanden müssen durch Kommata getrennt sein.

Beispiel:
```Python
# a soll den Wert 5 haben und b soll den Wert 10 haben
a,b = 5,10
```
Oder allgemeiner geschrieben:
```Python
variable1, variable2, ... = wert_für_variable1, wert_für_variable2, ...
```

Wenn beide Seiten nicht gleich lang sind, funktioniert es nicht, wie hier:
```Python
a,b = 10
a,b = 5,10,15
# --> ValueError: too many values to unpack (expected 2)
```
Wenn man a und b den Wert 10 zuweisen möchte, kann man das wie folgt machen:
```Python
a,b = 10,10
```

## Aufgabe

Operanden der rechten Seite können ja sowohl konkrete Werte aber auch Variablen sein.

Was wäre nun bei:
```Python
a = 5
b = 10

a,b = b,a

# Welchen Wert wird a haben?
# Welchen Wert wird b haben?
# Ist das eine unerlaubte Operation, 
# welche zu einem Fehler führt?
```

:::{admonition} Lösung
:class: dropdown

Antwort: a ist 10, b ist 5

Es wurde also ein Swap durchgeführt.

Man kann sich das vorstellen wie einen Shortcut für:

```Python
temp = a
a = b
b = temp

# Gleichzeitiges Tauschen von drei oder mehr Variablen ist ebenfalls möglich.
# Der Tausch von zwei Variablen wird jedoch praktisch gesehen häufiger benötigt.
```

Allgemeiner formuliert:
Zunächst werden alle Operanden auf der rechten Seite komplett ausgewertet und 
danach den Variablen auf der linken Seite zugewiesen.

:::
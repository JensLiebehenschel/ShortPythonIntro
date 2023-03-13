# Zuweisungen

## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

## Der Zuweisungsoperator

Wie auch in anderen Programmiersprachen ist <code>&equals;</code> der normale Zuweisungsoperator. Dessen Funktion sollte bekannt sein.

In Python hat dieser jedoch zusätzliche Funktionalität.
Normalerweise hat der Zuweisungsoperator einen Operanden auf der linken Seite und einen Operanden auf der rechten Seite.

also der Fall:
```Python
a = b
```

In Python gibt es diese Einschränkung nicht. Es müssen jediglich auf beiden Seiten gleich viele Operanden sein. Somit ist es möglich mit einem Zuweisungsoperator eine mehrfachuuweisung durchzuführen.
Die Operanden müssen durch Kommata getrennt sein.

Beispiel:
```Python
# a soll den Wert 5 haben und b soll den Wert 10 haben
a,b = 5,10
```
allgemeiner geschrieben:
```Python
variable1, variable2, ... = wert_für_variable1, wert_für_variable2, ...
```

Wenn beide Seiten nicht gleich lang sind, funktioniert es nicht.\
Ungültig:
```Python
a,b = 10
```
Wenn man a als auch b, 10 zuweisen möchte, muss man es wie folgt machen:
```Python
a,b = 10,10
```
anderherum ist 
```Python
a,b = 5,10,15 
```
ebenfalls ungültig.

## Aufgabe

Operanden der rechten Seite können ja sowohl konkrete Werte aber auch Variablen sein.

Was wäre nun bei:
```Python
a = 5
b = 10

a,b = b,a

# a?
# b?
# unerlaubte Operation?
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

# Gleichzeitiges Tauschen von drei oder mehr Variablen is ebenfalls möglich.
# Der Tausch von zwei Variablen wird jedoch praktisch gesehen häufiger benötigt.
```

:::
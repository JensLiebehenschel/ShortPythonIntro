# Tupel
(Klicken Sie [hier](https://jensliebehenschel.github.io/ShortPythonIntro/en/tuples.html) für die englische Version dieser Seite)

Ein Tupel in Python ist eine Datenstruktur, worin man eine Sequenz von Elementen speichern kann.
Somit ist die Funktionalität fast identisch zu einer Liste.

## Syntax
Die Syntax für Tupel ist sehr ähnlich zu Listen. Der einzige Unterschied ist, dass anstatt eckiger Klammern, runde Klammern genutzt werden. Sonst ist die Erstellung identisch.
```py
liste = [1, 2, 3]
tupel = (1, 2, 3)
```

Das einzige was man beachten muss sind Tupel mit genau einem Element. Leere Tupel sind zwar nicht wirklich sinnvoll, was man gleich verstehen wird, aber von der Syntax her ist ein leeres Tupel einfach nur eine öffnende und schließende runde Klammer.
```py
leer = ()
```

Tupel mit genau einem Element sind etwas spezieller, denn diese benötigen unbedingt ein Komma nach dem Element. Man kann sich den Grund logisch erschließen, wenn man eine Rechnung vor Augen hat. Klammern um eine einzelne Zahl sollten keine Auswirkung auf die Rechnung haben. Wenn man jetzt aber eine Zahl in runden Klammern als ein Tupel betrachtet, würde dies bei Rechnungen zu Problemen führen, dass aus Zahlen auf einmal Tupel werden.
```py
print( (5) )
# --> Zahl 5

print( (5,) )
# --> Tupel mit der Zahl 5

print( 1 + (5) )
# --> Zahl 6
# Sollte 6 sein anstatt 1 + "Tupel mit dem Element 5"
```

## Listen vs. Tupel
Es gibt nur einen fundamentalen Unterschied zwischen Listen und Tupeln. Listen sind veränderlich (mutable) und Tupel sind unveränderlich (immutable). Das heißt, dass nach Erstellung der Liste, diese noch nachträglich verändert werden kann. Zum Beispiel kann man mit <code>liste.append(4)</code> nach der Erstellung der Liste noch den Wert <code>4</code> an das Ende der Liste einfügen. 
```py
liste = [1, 2, 3]
liste.append(4)
print(liste)
# --> [1, 2, 3, 4]
```

Bei Tupeln ist dies nicht möglich. Sobald ein Tupelobjekt erstellt wurde, kann es nicht mehr verändert werden. 
```py
tupel = (1, 2, 3)
tupel.append(4)
print(tupel)
# --> AttributeError: 'tuple' object has no attribute 'append'

tupel[0] = 0
# --> TypeError: 'tuple' object does not support item assignment
```

Falls man etwas ergänzen möchte, muss ein neues Tupelobjekt erstellt werden.
Man kann z.B. mit dem <code>+</code> Operator, zwei Tupel konkatenieren und das Resultat in einem neuen Tupel speichern.
```py
tupel = (1, 2, 3)

neues_tupel = tupel + (4,)
print(neues_tupel)
# --> (1, 2, 3, 4)
```

Wenn man z.B. eine Liste zu einem Tupel umwandeln will, kann man diese mit <code>tuple()</code> zu einem Tupel casten. 
```py
liste = [1, 2, 3]

tupel = tuple(liste)
print(type(tupel))
# --> <class 'tuple'>
```

Ein möglicher Grund wieso man sowas machen wollen würde, wäre zum Beispiel um das Tupel dann als Schlüssel in einem Dictionary nutzen zu können.
Da Tupel unveränderlich sind, ist das möglich. Da Listen jedoch nicht unveränderlich sind, wäre das mit einer Liste nicht möglich.

```py
liste = [1, 2, 3]
tupel = (1, 2, 3)

{liste: True}
# --> TypeError: unhashable type: 'list'

{tupel: True}
# --> {(1, 2, 3): True}
```

## Wo findet man Tupel sonst noch?
In Python ist es möglich, dass eine Funktion mehrere Rückgabewerte hat. Interessant zu wissen ist, dass dies als eine Rückgabe eines Tupels umgesetzt wird.
```py
def beispiel():
    return 1, True, "Ok"

ergebnis = beispiel()
print(type(ergebnis))
# --> <class 'tuple'>

tupel = (1, True, "Ok")
entspricht_dem_tupel = ergebnis == tupel
print(entspricht_dem_tupel)
# --> True
```

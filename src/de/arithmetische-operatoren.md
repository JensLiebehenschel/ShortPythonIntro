# Arithmetische Operatoren
(Klicken Sie [hier](https://jensliebehenschel.github.io/ShortPythonIntro/en/arithmetic-operators.html) für die englische Version dieser Seite)

In Python hat man natürlich die klassischen Grundrechenarten wie <code>+</code>, <code>-</code>, <code>*</code> und <code>/</code>.

```Python
x = 5+5
print(x)
# --> 10

x = 3*5
print(x)
# --> 15
```

Ein gängiger Shortcut in Programmiersprachen wie C oder Java, um einen Wert um 1 zu erhöhen, ist der Operator <code>++</code>.

```C
i++;
```
ist das Gleiche wie
```C 
i = i + 1;
```
In Python ist dies **nicht** möglich.

Das ist nicht so tragisch, da man sowieso viel seltener einen Wert um 1 erhöht im Vergleich zu anderen Programmiersprachen.
Das wird sich auch später bei den Schleifen zeigen.

Als Alternative in Python soll 
```Python
i += 1 
```
genutzt werden, welches ebenfalls äquivalent zu 
```Python
i = i + 1
```
ist.
Das funktioniert analog für Minus, also <code>x -= 1</code> zu ersetzen ist.

Allgemein werden die Operatoren <code>+=, &#045;=, \*=</code> und <code>/=</code> so genutzt:
```Python
x RECHENOPERATION= n

# ist äquivalent zu

x = x RECHENOPERATION n
```

Beispiel:
```Python
x += 5

# ist äquivalent zu

x = x + 5
```

Es gibt auch die noch relativ übliche Modulo-Operation mit dem Prozentzeichen (<code>%</code>).
Kurze Auffrischung: 
Das Ergebnis von <code>a % b</code> (a modulo b bzw. a mod b) ist der Divisionsrest bei <code>a/b</code>.
```Python
x = 8 % 3
print(x)
# --> 2
```

Des Weiteren gibt es die Integer Division mit dem Operator <code>//</code>
Diese Operation berechnet den normalen Quotienten <code>c = a/b</code>, jedoch wird <code>c</code>, falls <code>c</code> nicht bereits ganzzahlig ist, auf den nächstkleineren Integerwert abgerundet.
Der Rest wird sozusagen abgeschnitten.

Man kann 
```Python
a // b 
```
aber auch umschreiben zu 
```Python
math.floor(a/b)
```
Beispiel:
```Python
x = 5 // 2
print(x)
# --> 2

import math
x = math.floor(5/2)
print(x)
# --> 2
```

<code>math.floor()</code> ist eine Funktion der Python math library, welche einen Input bekommt und diesen auf den nächsten Integer Wert abrundet.
Wie man Bibliotheken nutzt, wird später erklärt.


Zu guter Letzt, gibt es den Power-Operator, um Werte mit Exponenten auszurechnen.
Dafür werden zwei aufeinanderfolgende Sterne benutzt(<code>\*\*</code>).

Zum Beispiel berechnet mit <code>2 \*\* 5</code> den Wert 2<sup>5</sup> (2 hoch 5).
```Python
x = 3 ** 3
print(x)
# --> 27
```

Für die letzten drei Operatoren gibt es ebenfalls die Operatoren <code>%=</code>, <code>//=</code> und <code>\*\*=</code>.
```Python
x = 5
x //= 5
```
ist äquivalent zu:
```Python
x = 5
x = x // 5
```


## Mathematische Operatoren im nicht mathematischen Kontext

Eigentlich arithmetische Operatoren können je nach Kontext auch etwas anderes bedeuten. 
Wenn es um zwei Zahlen geht, dann handelt es sich um eine Rechnung. Was wäre nun aber die Summe von zwei Strings?

Eine Summe von zwei Strings ist meist nicht sinnvoll, deshalb hat etwa der Operator <code>+</code> bei Objekten, welche keine Zahlen sind,
verschiedene Bedeutungen.

Um bei dem Beispiel von den zwei Strings zu bleiben, lässt sich die Funktionsweise hier beobachten:

```Python
a = "Hello"
b = "World!"

print(a + b)
# --> "HelloWorld!"
```

Es fand also eine Konkatenierung statt. Der zweite String wurde an das Ende des ersten Strings angehängt.
Um es mit einem Leerzeichen zwischen "Hello" und "World!" schöner aussehen zu lassen, kann man erst ein Leerzeichen an das Ende des ersten Strings konkatenieren, bevor man den zweiten String anhängt:

```Python
a = "Hello"
b = "World!"

print(a + " " + b)
# --> "Hello World!"
```

Oft bedeutet der Operator <code>+</code> außerhalb von Rechnungen Konkatenierung. Gegebenenfalls muss man aber nachlesen, was ein jeweiliger Operator in einem gegebenen Kontext macht.

# Arithmetische Operatoren

## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

In Python hat man natürlich die klassischen Grundrechenarten wie <code>+, -, *</code> und <code>/</code>

```Python
x = 5+5
print(x)
# 10

x = 3*5
print(x)
# 15
```

Ein gängiger Shortcut in Programmiersprachen wie C oder Java, um einen Wert um 1 zu inkrementieren, wäre der <code>++</code> Operator.

Somit ist 
```C
i++;
```
das Gleiche wie
```C 
i = i + 1;
```
In Python ist dies **nicht** möglich.

Das ist in Python nicht so tragisch, da man sowieso viel seltener einen Wert um 1 inkrementiert im Vergleich zu anderen Programmiersprachen.
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
Die Idee ist analog für den <code>x&#045;&#045;</code> Ausdruck, welcher ebenfalls durch <code>x -= 1</code> zu ersetzen ist.

Allgemein werden die Operatoren <code>+=, &#045;=, \*= und /=</code> so genutzt:
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

Es gibt auch die noch relativ übliche Modulo Operation mit dem Prozentzeichen(%).
Kurze Auffrischung: 
Das Ergebnis von <code>a % b</code> (a modulo b bzw. a mod b) ist der Rest, der bei der Division <code>a/b</code> übrig bleibt.
```Python
x = 8 % 3
print(x)
# 2
```

Des Weiteren gibt es die Integer Division mit dem Operator <code>//</code>
Diese Operation berechnet den normalen Quotienten <code>c = a/b</code>, jedoch wird c, falls c nicht bereits ganzzahlig ist, auf den nächstkleineren Integerwert abgerundet.
Der Rest wird sozusagen ignoriert.

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
# 2

import math
x = math.floor(5/2)
print(x)
# 2
```

<code>math.floor()</code> ist eine Funktion der Python math library, welche einen Input bekommt und diesen auf den nächsten Integer Wert abrundet.
Wie man Bibliotheken nutzt, wird später erklärt.


Zu guter Letzt, gibt es den Power operator, um werte mit Exponenten auszurechnen.
Dafür werden zwei aufeinanderfolgende Sterne benutzt(<code>\*\*</code>)

Somit berechnet man mit <code>2 \*\* 5</code> den Wert 2<sup>5</sup> (2 hoch 5)
```Python
x = 3 ** 3
print(x)
# 27
```

## Mathematische Operatoren im nicht mathematischen Kontext

Eigentlich arithmetische Operatoren können je nach Kontext auch etwas anderes bedeuten. 
Wenn es um zwei Zahlen geht, dann handelt es sich um eine Rechnung. Was wäre nun aber die Summe von zwei Strings?

Eine Summe von zwei Strings ergibt nicht wirklich Sinn, deshalb hat etwa der <code>+</code> operator bei Objekten, welche nicht einfache numerische Zahlen sind,
verschiedene Bedeutungen.

Um bei dem Beispiel von den zwei Strings zu bleiben, lässt sich die Funktionsweise hier beobachten:

```Python
a = "Hello"
b = "World!"

print(a + b)
# HelloWorld!
```

Es fand also eine Konkatenierung statt. Der zweite String wurde an das Ende des ersten Strings angehängt.
Um es mit einem Leerzeichen zwischen "Hello" und "World!" schöner aussehen zu lassen, kann man erst ein Leerzeichen an das Ende des ersten Strings konkatenieren, bevor man den zweiten String anhängt:

```Python
a = "Hello"
b = "World!"

print(a + " " + b)
# Hello World!
```

Es ist nicht ganz willkürlich. Man kann ungefähr sagen, dass außerhalb von Rechnungen, <code>+</code> allgemein für Konkatenierung steht.

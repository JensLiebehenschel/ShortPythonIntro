# Arithmetische Operationen

## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

In Python hat man natürlich die klassischen Grundrechenarten wie +, -, * und /

```Python
5+5
# 10

3*5
# 15
```

Ein gängiger Shortcut in Programmiersprachen wie C oder Java, um einen Wert um 1 zu inkrementieren, wäre der "++" Operator.

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
Die Idee ist analog für den x\-\- Ausdruck, welcher ebenfalls durch x -= 1 zu ersetzen ist.

Allgemein werden die Operatoren +=, \-=, \*= und /= so genutzt:
```Python
x RECHENOPERATION= n

# ist äquivalent zu

x = x RECHENOPERATION n

# Beispiel:
x += 5 

# ist äquivalent zu

x = x + 5 
```

Es gibt auch die noch relativ übliche Modulo Operation mit dem Prozentzeichen(%).
Kurze Auffrischung: 
Das Ergebnis von a % b (a modulo b bzw. a mod b) ist der Rest, der bei der Division a/b übrig bleibt.
```Python
8 % 3
# 2
```

Des Weiteren gibt es die Integer Division mit dem Operator //
Diese Operation berechnet den normalen Quotienten c = a/b, jedoch wird c, falls c nicht bereits ganzzahlig ist, auf den nächstkleineren Integerwert abgerundet.
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
5 // 2
# 2

math.floor(5/2)
# 2
```

math.floor() ist eine Funktion der Python Math library, welche einen Input bekommt und diesen auf den nächsten Integer Wert abrundet.
Wie man Bibliotheken nutzt, wird später erklärt.


Zu guter Letzt, gibt es den Power operator, um werte mit Exponenten auszurechnen.
Dafür werden zwei aufeinanderfolgende Sterne benutzt(\*\*)

Somit berechnet man mit 2 \*\* 5 den Wert 2^5 (2 hoch 5)
```Python
3 ** 3
# 27
```

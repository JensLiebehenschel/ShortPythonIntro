# Klassen

**Klassen sind in dem Modul AlgDat nur bei Bäumen von Relevanz. Und da wird eher weniger auf den Python-Code eingegangen. Entscheiden Sie für sich selbst, ob Sie sich dennoch damit auseinandersetzen wollen.**

Python als objektorientierte Programmiersprache unterstützt natürlich das Konzept von Klassen.

Auf Vererbung und sonstiges wird hier nicht eingegangen.
Es geht nur darum, die Syntax von Klassenerstellung und Methoden zu verstehen,
da dies notwendig ist, wenn man Binärbäume programmieren möchte.

Zum Definieren einer Klasse wird das Keyword <code>class</code> gefolgt vom Klassennamen genutzt.
Daraufhin kann man noch leere runde Klammern setzten und man beendet die Zeile mit einem Doppelpunkt.
```Python
class meineKlasse:
    <Klassendefinition>
```
und
```Python
class meineKlasse():
    <Klassendefinition>
```
führen also auf das Gleiche hinaus.
Die Klammern nach dem Klassennamen können für Vererbung genutzt werden.

Nach dem Doppelpunkt folgt ein eingerückter Codeblock. Dort wird die Funktionalität der Klasse definiert.
Hier unterscheidet man zwischen Klassenattributen und Instanzattributen.

## Attribute

Kurzgesagt: Klassenattribute sind für alle Objekte einer Klasse gleich und können unabhängig von einem Objekt abgerufen werden.

Im Rahmen von AlgDat wird das nicht gebraucht. Es soll hier nur erwähnt sein.
```Python
class meineKlasse:
	klassen_id = 2 # Klassenattribut
```

Viel Interessanter hier sind Instanzattribute.
Also jene Attribute, welche sich von Instanz zu Instanz bzw. von Objekt zu Objekt unterscheiden.
Diese werden in der Regel im Konstruktor der Klasse deklariert und initialisiert.

Ein Attribut in Python muss genauso wie eine herkömmliche Variable auch, initialisiert sein.

Eine Deklaration ohne Initialisierung wie
```C
int i;
```
ist in Python also nicht möglich.

Ist im Endeffekt auch nicht schlimm, da man jedem Wert, den man nicht initialisieren möchte, einen Nullwert geben kann.
In Python mit dem Keyword <code>None</code>.

Einer Variable mit dem Wert <code>None</code> kann im Nachhinein alles zugewiesen werden. 
Seien es Integer, Strings oder gar Instanzen einer Klasse. Dynamic Typing macht dies möglich.

## Methoden und Konstruktor

Methoden werden in dem eingerückten Block der Klasse mit dem Keyword <code>def</code> erstellt.
Wie der Konstruktor auszusehen hat, ist in Python genau definiert.
<!--&#95; ist der HTML code für einen underscore-->
Im Gegensatz zu anderen Programmiersprachen, bei denen der Konstruktor den Namen der Klasse trägt, muss der Konstruktor in Python den Namen <code>&#95;&#95;init&#95;&#95;</code> haben. Wenn man ein Objekt dieser Klasse erstellt, wird der Konstruktor automatisch aufgerufen. Der Konstruktor kann natürlich auch Parameter erhalten. Diese können ebenfalls Defaultwerte enthalten. Es gelten die gleichen Regeln wie für normale Funktionen.

Für den Konstruktor und andere Methoden gilt, dass selbst bei Methoden ohne Parameter, ein Parameter hinzuzufügen ist.
Der erste Parameter, der an eine Methode übergeben wird, ist die Instanz der Klasse. Das passiert automatisch und man kann es nicht verhindern.

Laut Konvention bezeichnet man diesen Parameter als <code>self</code>. Man könnte ihn auch anders nennen.
Um Attribute einer Instanz zu erzeugen, muss die Instanz mit <code>self</code> oder wie auch immer man es nennen möchte, angesprochen werden.
Um auf Attribute oder Funktionen einer Klasse zuzugreifen, wird der Punktoperator genutzt.

Beispiel einer Klasse mit Konstruktor:
```Python
class meineKlasse:
	def __init__(self, a_input, b_input):
		self.a = a_input
		self.b = b_input
		self.c = None  # None ist das Python Äquivalent zu NULL

meine_instanz = meineKlasse(1,2)  # Konstruktor Aufruf mit Parametern
print(meine_instanz.a)
# 1
print(meine_instanz.b)
# 2
print(meine_instanz.c)
# None
```

Nun ein Beispiel mit einem Konstruktor, einer Methode und einer lokalen Variable im Konstruktor:
```Python
class meineKlasse:
	def __init__(self, a_input, b_input):
		self.a = a_input
		self.b = b_input
		self.c = None
		d = 5 	# Kein "self." davor, also lokale Variable und kein Attribut. Der Wert existiert nur im Konstruktor

	def berechne_c(self, faktor_von_a):
		self.c = self.a * faktor_von_a + self.b  # Formel: c = a * faktor + b
		self.e = 8  # Das Attribut e kann auch außerhalb des Konstruktors noch hinzugefügt werden


meine_instanz = meineKlasse(1,2)
print(meine_instanz.a)
# 1
print(meine_instanz.b)
# 2
print(meine_instanz.c)
# None

meine_instanz.berechne_c(3)
print(meine_instanz.c)
# 5

print(meine_instanz.e)
# 8

print(meine_instanz.d)
# AttributeError: 'meineKlasse' object has no attribute 'd'
# --> d ist kein Attribut der Klasse, sondern war nur eine lokale Variable im Konstruktor
```

Nicht vergessen, dass vor jedem Attribut einer Instanz innerhalb einer Methode das Präfix <code>self.</code> geschrieben werden muss, ansonsten ist es ein Parameter oder eine lokale Variable.
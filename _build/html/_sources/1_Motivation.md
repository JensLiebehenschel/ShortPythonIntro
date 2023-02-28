# Motivation

## Wieso Python?

Dies soll eine Einführung in die Programmiersprache Python sein.
Python ist eine "General-purpose programming language", welche sich durch einige Eigenschaften für die Veranstaltung "Algorithmen und Datenstrukturen", fortgehend als "AlgDat" bezeichnet, eignet.

## Wieso genau Python?

In dem Modul AlgDat geht es wie der Name bereits sagt, um Algorithmen.
Also um Vorschriften von Schritten zum Lösen von Problemen.
Diese Lösungen sollen allgemein von Programmierern genutzt werden können.
Unabhängig von der vorliegenden Programmiersprache.
Daher führt man das Konzept von "Pseudocode" ein, um Programmiersprachen-neutral Schritte zum Lösen eines Problems zu formulieren.

Dies hat zwar den Nachteil, dass man diesen Pseudocode nicht einfach in den bevorzugten Texteditor eingeben kann und ein gültiges Programm, geschweige denn die richtige Antwort bekommt.

Der Vorteil ist jedoch, dass man von diesem Punkt aus die Übersetzung in andere Programmiersprachen leichter unternehmen kann, als wenn statt Pseudocode ein Quellcode einer anderen Programmiersprache vorliegen würde.
Der noch größere Vorteil ist, dass man sich nicht mit den Einzelheiten einer bestimmten Programmiersprache beschäftigen muss.

Die Lesenden haben wahrscheinlich bereits einen Kurs in der Programmiersprache C besucht.
Hierbei gibt es das Konzept von Pointern.
Es gibt jedoch Programmiersprachen wie etwa Java (3. Semester), welche keine Pointer in ihrer Sprache haben.
Wäre es nun also sinnvoll, dass sich ein Java-Entwickler mit Pointern auseinandersetzten muss um zu verstehen wie der Sortieralgorithmus in einem gegeben C-Quellcode funktioniert?

Die Antwort ist wahrscheinlich ein "Nein".

Anderes Beispiel: Ist es für einen Algorithmus in der Regel relevant ob man Integer-Werte oder Gleitkommazahlen sortieren möchte?
Für ihren C-code, absolut. Für das Verständnis der Lösungsschritte, eher von geringerer Bedeutung.


## Python
Hier kommt nun Python ins Spiel.
Python ist nämlich die Brücke zwischen den Vorteilen von Pseudocode und den Vorteilen von bereits gegebenem Quellcode.

Im Vergleich zu Sprachen wie C, handelt es sich bei Python um eine dynamisch-typisierte Programmiersprache.
Das bedeutet, dass der Datentyp von Variablen nicht angegeben werden muss.
Speichert man unter einer Variable den Wert 5 ab, dann kann Python sich denken, dass es als Integer interpretiert werden soll.
Dividiert man den Wert nun durch 2, so interpretiert Python diese Variable mit dem Ergebnis 2.5 nun als eine Gleitkommazahl (float/double). 
Eine C-Variable welche zu beginn mit << int x = 5; >> deklariert & initialisiert wurde, würde nun << x == 2.5 >> FALSE angeben, da der Integer-Datentyp keine Informationen über Nachkommastellen hat.
Um sowas muss man sich in Python keine Gedanken machen.

Somit kann man in Python sehr einfach, sehr komplexe Strukturen erstellen. 
Wie wäre es mit einem Array, welches innerhalb von einem Index ein Array mit 5 weiteren geschachtelten Arrays enthält. Also ein Array in einem Array, in einem Array, ...
Nun könnte das letzte der geschachtelten Arrays eine Zeichenkette oder Zahlen enthalten. 
In C müsste man einige Zeit überlegen wie man das machen würde.
In Python fügt man es einfach in ein Array ein und gut ist es. 
Python wird schon herausfinden um was es sich hier handelt.

Allgemein ist Pythons Absicht, so natürlich wie möglich zu klingen.
Daher orientiert sich Python stark an gesprochenem Englisch.
Beispiele, wo dies der Fall ist, werden in späteren Kapiteln erläutert.

## Python use cases?
Aufgrund von Vereinfachungen wie diesen und weiteren, welche später vorgestellt werden, wird Python manchmal als "Ausführbarer Pseudocode" bezeichnet.
Es ist also fast so bequem wie Pseudocode, jedoch vollständig ausführbar und funktionial.
Die klaren Einsparnisse liegen jedoch definitiv bei der Schnelligkeit von Python.
Für Anwendungen, welche auf dem Computer eines Kunden laufen sollen, eignet es sich also in der Regel nicht.
In AlgDat geht es ja um Konzepte und nicht darum ein effizientes Softwareprodukt bei einem Kunden zu liefern.

Python ist also wunderbar um eine Idee eines Algorithmus zu testen und dafür zu sorgen, dass dieser funktioniert. 
Darauffolgend kann man diesen nun in eine schnellere Programmiersprache wie C umschreiben, womit man sich wiederum doch um die Details Gedanken machen muss.
Zumindest muss man sich jetzt "nur" um die Details Gedanken machen, anstatt zu überlegen, wie die Vorgehensweise des Algorithmus überhaupt funktionieren soll.
Python ist somit ideal für das Bauen eines Prototyps.

Python ist allgemein eine sehr beliebte Programmiersprache. 
Je nach Statistik, kann man sagen, dass Python häufig zu den Top 3 der beliebtesten Programmiersprachen der Welt gehört.

Des weiteren ist Python die go-to Programmiersprache für künstliche Intelligenz und zu einem großen Teil auch für Data Science.
Webseiten können mit Hilfe des "Django" Frameworks ebenfalls in Python programmiert werden.
Die investierte Zeit, sollte sich also lohnen.



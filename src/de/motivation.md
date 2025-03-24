# Motivation
(Klicken Sie [hier](https://jensliebehenschel.github.io/ShortPythonIntro/en/motivation.html) für die englische Version dieser Seite)

## Wieso Python?

Dies soll eine Einführung in die Programmiersprache Python sein.
Python ist eine "General-purpose programming language", welche sich durch einige Eigenschaften für das Verstehen von Algorithmen und Datenstrukturen eignet.

## Noch mehr Details? Gerne, dann hier einfach weiterlesen!

## Wieso genau Python?

Bei Algorithmen und Datenstrukturen geht es um Schritte zum Lösen von Problemen und Organisation von Daten.
Diese Lösungen sollen allgemein in der Software-Entwicklung genutzt werden können, und zwar
unabhängig von einer Programmiersprache.
Daher verwendet man oft "Pseudocode", um Programmiersprachen-neutral Schritte zum Lösen eines Problems oder der Organisation von Daten zu formulieren.

Dies hat zwar den Nachteil, dass man Pseudocode nicht einfach in einen Texteditor eingeben und das Programm ausführen lassen kann, und somit auch keine Ausgabe bekommt.

Der Vorteil ist jedoch, dass man von diesem Punkt aus die Übersetzung in andere Programmiersprachen leichter unternehmen kann, als wenn statt Pseudocode ein Quellcode einer anderen Programmiersprache vorliegen würde.
Der noch größere Vorteil ist, dass man sich nicht mit den Einzelheiten einer bestimmten Programmiersprache beschäftigen muss.

Die Lesenden haben wahrscheinlich bereits zumindest etwas Erfahrung Programmiersprache C.
Hierbei gibt es das Konzept von Pointern.
Es gibt jedoch Programmiersprachen wie etwa Java oder auch Python, welche keine Pointer in ihrer Sprache haben, da diese wegabstrahiert wurden.
Wäre es nun also sinnvoll, dass sich ein Java-Entwickler mit Pointern auseinandersetzten muss um zu verstehen wie der Sortieralgorithmus in einem gegeben C-Quellcode funktioniert?
Die Antwort ist sicherlich: Nein.

Ein anderes Beispiel: Ist es für einen Algorithmus in der Regel relevant ob man Integer-Werte oder Gleitkommazahlen sortieren möchte?
Für C-Code, absolut. Für das Verständnis der Lösungsschritte eher von geringerer Bedeutung.


## Python
Hier kommt nun Python ins Spiel.
Python ist nämlich die Brücke zwischen den Vorteilen von Pseudocode und den Vorteilen von bereits gegebenem Quellcode.

Im Vergleich zu Sprachen wie C handelt es sich bei Python um eine dynamisch-typisierte Programmiersprache.
Das bedeutet, dass der Datentyp von Variablen nicht angegeben werden muss.
Speichert man unter einer Variable den Wert <code>5</code> ab, dann kann Python sich denken, dass es als Integer interpretiert werden soll.
Dividiert man den Wert nun durch <code>2</code>, so interpretiert Python diese Variable mit dem Ergebnis <code>2.5</code> nun als eine Gleitkommazahl. 
Eine Variable in C, welche zu Beginn mit 
```C
int x = 5;
```
deklariert und initialisiert wurde, würde nun 
```C
printf("%d", x/2==2.5);
// --> 0 (False)
```
angeben, dass <code>5</code> geteilt durch <code>2</code> nicht <code>2.5</code> ist, da der Integer-Datentyp keine Informationen über Nachkommastellen hat.
Um sowas muss man sich in Python keine Gedanken machen.

Somit kann man in Python sehr einfach sehr komplexe Strukturen erstellen. 
Wie wäre es mit einem Array, welches innerhalb von einem Index ein Array mit 5 weiteren geschachtelten Arrays enthält. Also ein Array in einem Array, in einem Array, ...
Nun könnte das letzte der geschachtelten Arrays eine Zeichenkette oder Zahlen enthalten. 
In C müsste man einige Zeit überlegen wie man das machen würde.
In Python fügt man es einfach in ein Array ein und gut ist es. 
Python wird schon herausfinden um was es sich hier handelt.
Die Struktur kann sogar zur Laufzeit geändert werden.

Allgemein ist Pythons Absicht, so natürlich wie möglich zu klingen.
Daher orientiert sich Python stark an gesprochenem Englisch.
Beispiele, wo dies der Fall ist, werden in späteren Kapiteln erläutert.

## Python use cases?
Aufgrund von Vereinfachungen wie diesen und weiteren, welche später vorgestellt werden, wird Python manchmal als "Ausführbarer Pseudocode" bezeichnet.
Es ist also fast so bequem wie Pseudocode, jedoch vollständig ausführbar.
Ein Nachteil von Python im Vergleich zu C ist jedoch definitiv die Performance.
Für manche rechenintensiven Anwendungen ist Python weniger geeignet.
Bei Algorithmen und Datenstrukturen handelt es sich aber um die Effizienz von den Konzepten, und nicht um die Erstellung eines hochperformaten Software-Produkts.

Python ist also wunderbar, um eine Idee eines Algorithmus zu testen und dafür zu sorgen, dass dieser funktioniert. 
Darauffolgend kann man diesen nun in eine schnellere Programmiersprache wie C umschreiben, womit man sich wiederum doch um die Details Gedanken machen muss.
Zumindest muss man sich jetzt "nur" um die Details Gedanken machen, anstatt zu überlegen, wie der Algorithmus überhaupt funktionieren soll.
Python ist somit ideal für das Bauen von Prototypen.

Python ist eine sehr beliebte Programmiersprache. 
Je nach Statistik, kann man sagen, dass Python häufig zu den Top 3 der beliebtesten Programmiersprachen der Welt gehört.

Des Weiteren ist Python die Programmiersprache für künstliche Intelligenz und für Data Science.
Webseiten können mit Hilfe des "Django" Frameworks ebenfalls in Python programmiert werden.

Die investierte Zeit, Python zu lernen, sollte sich also lohnen.

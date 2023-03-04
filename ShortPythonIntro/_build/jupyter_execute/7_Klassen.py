#!/usr/bin/env python
# coding: utf-8

# # Klassen

# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

# ## Klassen sind in dem Modul AlgDat nur bei Bäumen von Relevanz. Und da wird eher weniger auf den Python code eingegangen. Entscheiden Sie für sich selbst, ob Sie sich trotzdessen damit auseinandersetzen wollen.

# Python als objektorientierte Programmiersprache unterstützt natürlich das Konzept von Klassen.
# 
# Auf Vererbung und sonstiges wird hier nicht eingegangen.
# Es geht nur darum, die Syntax von Klassenerstellung und Methoden zu verstehen,
# da es nahezu notwendig ist, wenn man Binärbäume programmieren möchte.
# 
# Zum definieren einer Klasse wird das keyword <code>class</code> gefolgt vom Klassennamen genutzt.
# Daraufhin kann man wenn man möchte noch leere runde Klammern setzten und die Zeile mit einem Doppelpunkt beenden.
# ```Python
# class meineKlasse:
#     <Klassendefinition>
# ```
# und
# ```Python
# class meineKlasse():
#     <Klassendefinition>
# ```
# führen also auf das Gleiche hinaus.
# Die Klammern nach dem Klassennamen können für Vererbung genutzt werden.
# 
# Nach dem Doppelpunkt kommt ein Indentierungsblock und dort wird die Funktionalität der Klasse definiert.
# Hier unterscheidet man zwischen Klassenattributen und Instanzattributen.
# 
# Kurzgesagt: Klassenattribute sind für alle Objekte einer Klasse gleich und können unabhängig von einem Objekt abgerufen werden.
# 
# Im Rahmen von AlgDat wird das nicht gebraucht. Ich will es hier nur an der Stelle erwähnt haben.
# ```Python
# class meineKlasse:
# 	klassen_id = 2 # Klassenattribut
# ```
# 
# Viel Interessanter hier sind Instanzattribute.
# Also jene attribute, welche sich von Instanz zu Instanz bzw. von Objekt zu Objekt unterscheiden.
# Diese werden in der Regel im Konstruktor der Klasse deklariert und initialisiert.
# 
# Ein Attribut in Python muss genauso wie eine herkömmliche Variable auch, initialisiert sein.
# 
# Eine Deklaration ohne Initialisation wie
# ```C
# int i;
# ```
# ist in Python also nicht möglich.
# 
# Ist im Endeffekt auch nicht schlimm, da man jedem Wert, den man nicht initialisieren möchte einen Nullwert geben kann.
# In Python wäre dies das Keyword <code>None</code>
# 
# Einer Variable mit dem Wert <code>None</code> kann im Nachhinein alles zugewiesen werden. 
# Seien es Integer, Strings oder gar Instanzen einer Klasse. Dynamic Typing macht es möglich.
# 
# 
# Methoden werden im den Indentierungsblock der Klasse mit dem Keyword <code>def</code> erstellt.
# Wie der Konstruktor auszusehen hat, ist in Python genau definiert.
# <!--&#95; ist der HTML code für eien underscore-->
# Im Gegensatz zu anderen Programmiersprachen, wo der Konstruktor den Namen der Klasse hat, muss der Konstruktor in Python den Namen <code>&#95;&#95;init&#95;&#95;</code> haben. Ist einfach so definiert. Der Konstruktor kann natürlich Parameter erhalten.
# 
# Für den Konstruktor als auch für andere Methoden gilt, dass selbst bei Methoden ohne Parameter, ein Parameter hinzuzufügen ist.
# Der erste Parameter, der an eine Methode übergeben wird, ist die Instanz der Klasse. Das passiert automatisch und man kann es nicht verhindern.
# 
# Laut konvention bezeichnet man diesen Parameter als <code>self</code>. Man kann es wenn man wirklich möchte aber auch anders nennen.
# Um Attribute einer Instanz zu erzeugen, muss die Instanz mit <code>self</code> oder wie auch immer man es nennen möchte, angesprochen werden.
# Um auf Attribute oder Funktionen einer Klasse zuzugreifen, wird der Punktoperator genutzt.
# 
# Beispiel einer Klasse mit Konstruktor:
# ```Python
# class meineKlasse:
# 	def __init__(self, a_input, b_input):
# 		self.a = a_input
# 		self.b = b_input
# 		self.c = None 		# None ist das Python Äquivalent zu NULL
# 
# meine_instanz = meineKlasse(1,2)
# print(meine_instanz.a)
# # 1
# print(meine_instanz.b)
# # 2
# print(meine_instanz.c)
# # None
# ```
# 
# Nun ein Beispiel mit einem Konstruktor, einer Methode und einer lokalen Variable im Konstruktor:
# ```Python
# class meineKlasse:
# 	def __init__(self, a_input, b_input):
# 		self.a = a_input
# 		self.b = b_input
# 		self.c = None
# 		d = 5 	# Kein "self." davor, also lokale Variable und kein Attribut. Der Wert existiert nur im Konstruktor
# 
# 	def berechne_c(self, faktor_von_a):
# 		self.c = self.a * faktor_von_a + self.b # Formel: c = a * faktor + b
# 		self.e = 8		# Das attribut e kann auch außerhalb des Konstruktors noch hinzugefügt werden.
# 
# 
# meine_instanz = meineKlasse(1,2)
# print(meine_instanz.a)
# # 1
# print(meine_instanz.b)
# # 2
# print(meine_instanz.c)
# # None
# 
# meine_instanz.berechne_c(3)
# print(meine_instanz.c)
# # 5
# 
# print(meine_instanz.e)
# # 8
# 
# print(meine_instanz.d)
# # AttributeError: 'meineKlasse' object has no attribute 'd'
# # --> d ist kein Attribut der Klasse, sondern war nur eine lokale Variable im Konstruktor
# ```
# 
# Nicht vergessen, dass bei jedem Attribut einer Klasse innerhalb einer Methode der Präfix <code>self.</code> geschrieben werden soll.

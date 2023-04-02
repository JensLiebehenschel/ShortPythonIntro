#!/usr/bin/env python
# coding: utf-8

# # Funktionen

# Erstmal vorweg: Es gibt in Python keine Main-Funktion wie in C.
# Der Inhalt der Main-Funktion wird im globalen Bereich geschrieben und ausgeführt.
# Wenn man im Arbeitsleben Python-Code schreibt, ist dies unerwünscht und wird anders gehandhabt.
# Das ist für diese Einführung jedoch nicht von Bedeutung.
# 
# ## Erstellen einer Funktion
# 
# Um eine Funktion zu definieren, wird das Keyword <code>def</code> benutzt.
# 
# Anschließend wird der Funktion ein Name zugewiesen und in runden Klammern gibt man die Parameter an.
# 
# Man beendet den Funktionskopf nun mit einem Doppelpunkt, nach welchem man die nächste Zeile einrückt und dann den eigentlichen Inhalt der Funktion angibt.
# 
# Beispiel:
# ```Python
# def ich_printe_falschherum(input_string):
#     result = ""
#     for i in range(1, len(input_string)+1):
#         result += input_string[-i] # Der "+"-operator bei Strings konkateniert
#     print(result)
# 
# ich_printe_falschherum("Hello World!")
# # !dlroW olleH
# ```
# Verallgemeinert:
# ```Python
# def funktions_name(parameter1, parameter2, ...):
# 	<Funktionsrumpf>
# ```
# 
# Es ist ebenfalls möglich Defaultwerte für Parameter anzugeben. Dafür weist man den Parametern bereits einen Wert zu. Sobald ein Defaultwert angegeben wurde, müssen alle Werte rechts davon ebenfalls Defaultwerte haben
# Beispiel:
# ```Python
# def summe_von_bis_zu_vier_zahlen(a, b, c=0, d=0):
#     return a + b + c + d
# 
# print(summe_von_bis_zu_vier_zahlen(1,2))
# # 3
# 
# print(summe_von_bis_zu_vier_zahlen(1,2,3))
# # 6
# 
# print(summe_von_bis_zu_vier_zahlen(1,2,3,4))
# # 10    
# ```
# 
# ## Rückgabewerte
# 
# Mit dem Keyword <code>return</code> kann man angeben, was die Funktion zurückgeben soll.
# Die Besonderheit von Python liegt darin, dass man mehrere Werte zurückgeben kann.
# 
# Angenommen eine Funktion erhält einen String aus ausschließlich Kleinbuchstaben und soll berechnen, wie viele Vokale und wie viele Konsonanten in dem String vorkommen.
# Zusätzlich soll die Funktion zurückgeben, ob es weniger Vokale als Konsonanten gibt (in Form eines Wahrheitswertes).
# In anderen Programmiersprachen müsste man eine Datenstruktur erstellen, um sowohl zwei Integer Werte als auch einen Wahrheitswert zurückgeben zu können. In Python gibt man einfach alle drei zurück, jeweils durch Komma getrennt.
# 
# ```Python
# def vokale_und_konsonanten(input_string):
# 	anzahl_vokale = 0
# 	anzahl_konsonanten = 0
# 	for buchstabe in input_string: 	# Man kann über einen String genauso iterieren wie über eine Liste
# 		if buchstabe in ["a", "e", "i", "o", "u"]:
# 			anzahl_vokale += 1
# 		else:
# 			anzahl_konsonanten += 1
# 	return anzahl_vokale, anzahl_konsonanten, anzahl_vokale < anzahl_konsonanten
# 
# 
# anzahl_vokale, anzahl_konsonanten, es_kommen_mehr_konsonanten_vor = vokale_und_konsonanten("algdat")
# print(anzahl_vokale)
# # 2
# print(anzahl_konsonanten)
# # 4
# print(es_kommen_mehr_konsonanten_vor)
# # True
# ```
# 
# Da kann man wieder auf die Mehrfachzuweisung schließen.
# Da die Funktion drei Werte zurückgibt und man drei Variablen auf der linken Seite hat, haben beide Seiten des Zuweisungsoperators gleich viele Operanden. Also ist dies eine gültige Zuweisung.
# 
# ## Rekursion
# 
# Rekursion funktioniert in Python genauso wie in anderen Programmiersprachen auch. Eine Funktion ruft sich selbst auf.
# Als Beispiel die rekursive Berechnung der n-ten Fibonacci-Zahl.
# ```Python
# def fib_rek(n):
#     if n <= 1:
#         return n
#     else:
#         return fib_rek(n-1) + fib_rek(n-2)
#         
#         
# print(fib_rek(6))
# # 8
# ```

# ## Aufgabe

# Erstellen Sie eine Funktion, welche einen positiven Integerwert als Argument erhält und <code>True</code> zurückgibt, falls der Wert eine gerade Zahl ist. Ansonsten soll <code>False</code> zurück gegeben werden. Testen Sie die Funktion für ein paar Zahlen ihrer Wahl. Sie müssen **nicht** sicherstellen, dass wirklich eine positive Ganzzahl eingegeben wurde. Gehen Sie davon aus, dass nichts anderes eingegeben wird. Sie können auch gerne versuchen, mehrere Lösungen zu finden.

# In[1]:


# Hier können Sie ihren Versuch schreiben...


# :::{admonition} Lösung
# :class: dropdown
# 
# Die wohl gängigste Lösung mit Modulo:
# ```Python
# def is_even_ordinary(value):
#     if value % 2 == 0:
#         return True
#     else:
#         return False
# ```
# 
# Eine kompaktere Lösung mit Modulo:
# ```Python
# def is_even_ordinary_improved(value):
#     return value % 2 == 0
# ```
# 
# Rekursive Lösung. <code>0</code> ist als gerade Zahl und  <code>1</code> als ungerade Zahl bekannt. Wenn der Wert ungleich <code>0</code> oder <code>1</code> ist, 
# wird die Funktion rekursiv für den um zwei veringerten Wert aufgerufen bis der Wert entweder <code>0</code> oder <code>1</code> ist. Die Subtraktion mit <code>2</code> sorgt dafür, 
# dass der Wert gerade oder ungerade im nächsten rekursiven Aufruf bleibt.
# ```Python
# def is_even_rek(value):
#     if value == 0:
#         return True
#     elif value == 1:
#         return False
#     else:
#         return is_even(value-2)
# ```
# 
# Idee: Ob eine Zahl gerade oder ungerade ist, hängt nur von der letzten Ziffer ab.
# Deswegen konvertieren wir die Zahl in einen String und betrachten nur die letzte Ziffer.
# Wir casten die letzte Ziffer zurück in eine Zahl und gucken ob die letzte Ziffer in der Liste der bereits bekannten einziffrigen geraden Zahlen enthalten ist.
# ```Python
# def is_even_last_digit(value):
#     return int(str(value)[-1]) in [0, 2, 4, 6, 8]
# ```
# 
# In Python kann man auch ebenfalls auf Bitebene arbeiten. 
# Bei dem <code>&</code> Operator handelt sich um bitweises und.
# Da die Bitfolge <code>1</code> äquivalent ist zu <code>...00001</code>,
# ist die Länge des linken Wertes egal. 
# Alles bis auf das letzte Bit wird bei der Operation zu <code>0</code>,
# womit nur das letzte Bit etwas anderes als <code>0</code> sein kann.
# Das Ergebnis ist also immer 1 Bit lang.
# Bei einer ungeraden Zahl ist das letzte Bit <code>1</code> und die Operation würde den Wert <code>1</code> zurückgeben.
# Bei einer geraden Zahl wäre das letzte Bit <code>0</code> und somit würde der Wert <code>0</code> zurückgegeben werden.
# <code>0</code> und <code>1</code> können zu Booleans gecasted werden.
# <code>1</code> wird beim casten als <code>True</code> und <code>0</code> als <code>False</code> interpretiert.
# Momentan sind <code>True</code> und <code>False</code> falsch herum sind, da wir ja <code>True</code> haben wollen, wenn der Wert gerade ist,
# somit müssen wir den Boolean lediglich mit einem <code>not</code> negieren.
# ```Python
# def is_even_bitewise_and(value):
#     return not bool(value & 1)
# ```
# 
# Es gibt viele Möglichkeiten, diese Aufgabe zu lösen.
# Hier handelt es sich lediglich um Beispiele und manche Lösungen sind praktischer als andere.
# Hier soll lediglich die Vielfalt an möglichen Ansätzen gezeigt werden.
# 
# :::

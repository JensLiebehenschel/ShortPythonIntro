#!/usr/bin/env python
# coding: utf-8

# # Funktionen

# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

# Erstmal vorweg: Es gibt in Python keine Main Funktion wie in C.
# Der Inhalt der Main Funktion wird im globalen Bereich geschrieben und ausgeführt.
# Wenn man im Arbeitsleben Python schreibt, ist dies unerwünscht und es wird anders gehandhabt.
# Das ist für diese Einführung jedoch nicht von Bedeutung.
# 
# ## Erstellen einer Funktion
# 
# um eine Funktion zu definieren, wird das keyword <code>def</code> benutzt.
# 
# anschließend wird der Funktion ein Name zugewiesen und in runden Klammern gibt man die Parameter der Funktion an.
# 
# Man beendet den Funktionkopf nun mit einem Doppelpunkt, nach welchem man die nächste Zeile indentiert und dann den eigentlichen Inhalt der Funktion angibt.
# 
# Beispiel:
# ```Python
# def ich_printe_falschherum(input_string):
#     result = ""
#     for i in range(1, len(input_string)+1):
#         result += input_string[-i] # Der "+"-operator bei Strings konkatiniert
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
# ## Rückgabewerte
# 
# Mit dem <code>return</code> keyword kann man angeben, was die Funktion zurückgeben soll.
# Die Besonderheit von Python liegt darin, dass man mehrere Werte innerhalb von einem Return zurückgeben kann.
# 
# Angenommen ich will eine Funktion schreiben, welche einen String aus ausschließlich Kleinbuchstaben als input bekommt und sagen soll wieviele Vokale und wieviele Konsonanten in dem String vorkommen.
# Zusätzlich soll die Funktion zurückgeben ob es mehr Vokale oder mehr Konsonanten gibt (in Form eines Wahrheitswertes).
# In anderen Programmiersprachen müsste ich eine Datenstruktur erstellen um sowohl zwei Integer Werte als auch einen Wahrheitswert zurückgeben zu können. In Python gibt man einfach alle drei, durch jeweils ein Komma getrennt, zurück.
# 
# ```Python
# def vokale_und_konsonanten(input_string):
# 	anzahl_vokale = 0
# 	anzahl_konsonanten = 0
# 	for buchstabe in input_string: 			# Man kann durch einen String genauso iterieren wie durch eine List auch
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
# Für die Rekursion wird das Beispiel von rekursivem Fibonacci gezeigt.
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

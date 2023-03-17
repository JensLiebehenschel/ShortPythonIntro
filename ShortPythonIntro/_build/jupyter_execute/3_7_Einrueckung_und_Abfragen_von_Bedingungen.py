#!/usr/bin/env python
# coding: utf-8

# # Einrückung und Abfragen von Bedingungen

# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

# Eine weitere Besonderheit, welche Python stark von anderen Programmiersprachen unterscheidet, sind die {geschweiften Klammern}
# 
# Oder besser gesagt, ihr **Fehlen**.
# 
# In den meisten Programmiersprachen werden geschweifte Klammern benutzt um Codeblöcke zu trennen.
# 
# Option 1:
# ```C
# if (Bedingung) {
# 	<Dieser Codeblock wird nur ausgeführt, wenn die Bedingung wahr ist>
# }
# <Dieser Code wird unabhängig von der Bedingung ausgeführt>
# ```
# hierbei ist es auch genauso möglich, den Code wie folgt umzuschreiben
# 
# Option 2:
# ```C
# if (Bedingung) {
# <Dieser Codeblock wird nur ausgeführt, wenn die Bedingung wahr ist>
# }
# <Dieser Code wird unabhängig von der Bedingung ausgeführt>
# ```
# oder
# 
# Option 3:
# ```C
# if (Bedingung) {<Dieser Codeblock wird nur ausgeführt, wenn die Bedingung wahr ist>}
# <Dieser Code wird unabhängig von der Bedingung ausgeführt>
# ```
# Frage:\
# Welche der drei Optionen ist am übersichtlichsten?\
# Antwort:\
# Option 1 ist von den drei Optionen, die übersichtlichste, da man den Codeblock der Abfrage von dem weiteren Code leicht unterscheiden kann ohne auf geschweifte Klammern achten zu müssen.
# 
# <a href="https://cs50.readthedocs.io/style/c/#indentation" target="_blank">C Style Guides</a> sagen ebenfalls Option 1.
# 
# 
# Fast so als könne man die geschweiften Klammern auch weglassen?
# Python sagt: Ja.
# Geschweifte Klammern in Python werden nicht verwendet um Codeblöcke zu trennen.
# In Python werden geschweifte Klammern ausschließlich benutzt um sogenannte Dictionaries zu nutzen.
# Was ein Dictionary ist, wird man im Modul AlgDat später kennenlernen.
# Dort lernt man es als "Hashmap" oder allgemein als "Hashing" kennen
# Das wird hier an der Stelle nicht weiter erklärt.
# 
# 
# Wie unterscheidet man Codeblöcke in Python nun genau?
# Durch Einrücken, englisch: "Indentation". 
# Also Leerzeichen und Tabs.
# 
# 
# Also wäre Option 1 in Python-artige Syntax wie folgt umgewandelt:
# 
# ```Python
# if (Bedingung) 
# 	<Dieser Codeblock wird nur ausgeführt, wenn die Bedingung wahr ist>
# 
# <Dieser Code wird unabhängig von der Bedingung ausgeführt>
# ```
# 
# Nun bräuchte man einen Weg die Bedingung von dem Codeblock selbst zu unterscheiden.
# Eine intuitive Lösung wäre ein Doppelpunkt.
# Dies ist eine relativ natürliche Art eine Bedingung auzudrücken.
# ```
# if (this is so): # then do
# 	<that>
# <Proceed here afterwards, no matter if "that" has been done or not>
# ```
# Fast wie ein Merkzettel.
# ```Python
# wenn dies so ist:
# 	mache das
# 	und das
# 	und noch Weiteres
# ```
# Im Gegensatz zu anderen Programmiersprachen sind Klammern innerhalb von Bedingungen ebenfalls optional.
# ```Python
# if (x ist wahr):
# 	<mach etwas>
# 
# if x ist wahr:
# 	<mach etwas>
# ```
# 
# Klammern werden nur benötigt, wenn eine Bedinung mehr als eine Zeile lang ist.
# ```Python
# # Richtig:
# if (x ist wahr
# 	und y ist wahr):
# 		mach etwas
# 
# # Falsch:
# if x ist wahr
# 	und y ist wahr:
# 		mach etwas
# 
# ```
# Hiermit hätten wir auch bereits geklärt wie bedingte Abfrage Funktioniert
# ```Python
# if BEDINGUNG:
# 	<DAZUGEHÖRIGER CODEBLOCK>
# <REST DES PROGRAMMS>
# ```
# 
# Man muss mit Einrücken konsequent sein und korrekt einrücken. Jedes Leerzeichen bzw. jeder Tab zählt.
# Jeder Teil eines Codeblocks muss gleich weit eingerückt sein.
# ```Python
# # Falsch:
# if x ist wahr:
# 	mach das
# 	 und mach das
#    und das hier auch 
# 
# # Richtig:
# if x ist wahr:
#     mach das
#     und mach das
#     und das hier auch
# ```
# Für den Codeblock, welcher ausgeführt wird wenn die Bedingung der Abfrage nicht wahr zurückgibt, wird das Keyword <code>else</code> benutzt.
# Will man ein <code>else-if</code> erstellen, so kann man das eingebaut Python Keyword <code>elif</code> nutzen.
# Das Funktioniert folgendermaßen:
# ```Python
# if x == 1:
# 	print("x ist 1")
# elif x == 2:
# 	print("x ist 2")
# else:
# 	print("x ist weder 1 noch 2")
# ```

# ## Aufgabe

# Ein etwas komplexeres Beispiel erst in C:
# ```C
# if (x ist wahr) {
#     if (y ist wahr) {
#         if (z ist wahr) {
#             <Codeblock_1>
#         }
#     }
#     else {
#         <Codeblock_2>
#     }
# }
# else {
#     <Codeblock_3>
# }
# <Rest des Programms...>
# ```
# Jetzt Sind Sie an der Reihe. Versuchen Sie das obige Beispiel von C in Python umzuschreiben.
# Sie können <code>if x ist wahr</code> als Ersatz für <code>if (x ist wahr)</code> nutzen. Analog für y und z.
# 
# Sie können den Platz unten zum Schreiben nutzen. Das Ausführen des Codes wird ihnen jedoch nichts bringen, da es sich hier nicht um funktionierenden Python code handelt.

# In[1]:


# Hier können Sie ihren Versuch schreiben...


# :::{admonition} Lösung
# :class: dropdown
# 
# ```Python
# if x ist wahr:
#     if y ist wahr:
#         if z ist wahr:
#             <Codeblock_1>
#     else:
#         <Codeblock_2>
# else:
#  	<Codeblock_3>
# <Rest des Programms...>
#  ```
# Hierbei ist es auch wichtig, dass <code>&lt;Rest des Programms...&gt;</code> nicht eingerückt ist. Hätte es eine Einrückung von einem Tab, so könnte man denken, dass der Rest des Programms noch zu <code>&lt;Codeblock_3&gt;</code> gehört.
# 
# :::

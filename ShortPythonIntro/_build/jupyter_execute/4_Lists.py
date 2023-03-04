#!/usr/bin/env python
# coding: utf-8

# # Lists
# 
# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**
# 
# Die am meisten benutzte Datenstruktur ist das Array.
# Python nennt es jedoch nicht ein "Array", sondern eine "List".
# Von der Idee her sind sie identisch. Man hat eine Datenstruktur worin man Daten speichern möchte.
# 
# Viele andere Programmiersprachen benutzen geschweifte Klammern wie bei Codeblocks, um Arrays zu befüllen.
# 
# Ein Beispiel aus C:
# ```C
# int arr[] = {1, 2, 3, 4, 5};
# ```
# In Python werden eckige Klammern genutzt um Lists zu symbolisieren.
# ```Python
# arr = [1, 2, 3, 4, 5]
# ```
# Bei dem vorherigen Python Beispiel, wird nirgendwo gesagt, dass es sich bei dieser List um eine Integer List handelt.
# 
# Das liegt wieder am Dynamic Typing.
# Nur handelt es sich hier nicht einmal um ein Integerarray.
# 
# Man könnte nämlich einen anderen Datentypen als einen Integer einfügen.
# 
# Beispiel:
# ```Python
# arr = [1, 2, 3, 4, 5, "Hello World!"]
# ```
# In den meisten anderen Programmiersprachen wäre das so einfach nicht möglich.
# Es liegt auch nicht daran, dass die Ziffern 1 bis 5 zu Strings übersetzt werden.
# Es gibt in der obigen List mehrere verschiedene Datentypen.
# Dies kann mit der Funktion <code>type()</code> überprüft werden, welche wir bereits beim Testen von Dynamic Typing in einem früheren Kapitel kennen gelernt haben.
# 
# Nochmal eine kurze Erinnerung:
# Die Funktion <code>type(objekt)</code> erhält ein Objekt als Parameter. Dabei kann es sich um Datentypen wie einen Integer oder eine List oder sonst was handeln.
# Ja, Python behandelt Datentypen wie Objekte.
# 
# Als Output gibt die Funktion zurück, um welche Klasse es sich bei diesem Objekt handelt.
# 
# Rufen wir jetzt diese Funktionen auf, sehen wir folgendes.
# Wir benutzen wie üblicherweise auch, eckige Klammern mit einem Index dazwischen, um auf einen bestimmten (bei 0 anfangenden) Index einer List zuzugreifen.
# ```Python
# print(type(arr[0]))
# # <class 'int'>
# # --> Objekt am Index 0 ist ein Integer
# 
# print(type(arr[5]))
# # <class 'str'>
# # --> Objekt am Index 5 ist ein String
# ```
# Somit handelt es unüberraschender Weise bei <code>1</code> um einen Integer und bei
# <code>"Hello World!"</code> um einen String.
# 
# 
# ## Negative Indizes ##
# 
# Python verfügt über einen praktischen Shortcut um auf n-t letzte Element in einer List zuzugreifen.
# 
# Und zwar mit der Syntax: <code>arr[-n]</code>
# 
# Also mit einem negativen Index.
# 
# <code>arr[-1]</code> greift auf das letzte Element zu, <code>arr[-2]</code> greift auf das vorletzte Element zu und so weiter.
# 
# Dabei sollte man beim Programmieren beachten, dass negative Indizes in Python gültig sind und nicht zwingend zu einem Fehler führen.
# 
# 
# ## Length funktion ##
# 
# Um die Länge eines Arrays herauszufinden, benutzt man die <code>len()</code> funktion
# ```Python
# arr = [1, 2, 3, 4, 5]
# print(len(arr))
# # 5
# ```
# 
# ## Append ##
# 
# Um einen Wert zu einer bereits existierenden Liste hinzuzufügen, kann die sehr hilfreiche <code>append()</code> funktion genutzt werden.
# 
# ```Python
# arr = [1, 2, 3, 4, 5]
# print(arr)
# # [1, 2, 3, 4, 5]
# print(len(arr))
# # 5
# 
# arr.append(6)
# print(arr)
# # [1, 2, 3, 4, 5, 6]
# print(len(arr))
# # 6
# ```
# Man kann soviel appenden wie man möchte, da eine List eine dynamische Datenstruktur ist.
# Im Gegensatz zu Arrays in C, muss man nicht wissen wie lang die List höchstens sein darf.
# 
# Es ist auch möglich eine leere List zu erstellen, die man anscheließend mit append befüllt.
# 
# Eine leere Liste wird wie folgt initialisiert:
# ```Python
# arr = []
# ```
# 
# ## Slicing ##
# 
# Das Konzept von Slicing wird genutzt, um eine Sublist einer Liste zu nehmen.
# Also eine Teilmenge einer bereits existierenden Liste. Beim Slicing geht es lediglich um die Position der Elemente.
# 
# Um eine Untermenge abhängig von einer Bedinung zu nehmen, wie etwa
# "alle Werte aus x, welche größer als 5 sind", benutzt man sogenannte List Comprehension.
# Für diese Einführung ist dies jedoch viel zu fortgeschritten.
# Interessierte können selbst danach recherchieren.
# 
# 
# Zurück zum Slicing. Hierbei geht es beispielsweise darum, eine Sublist bestehend aus allen Elementen ab Index a oder allen Elementen bis ausschließlich Index b oder einer Kombination davon, zu erstellen.
# 
# Hierfür wird folgende Syntax benutzt
# ```Python
# arr[a:b]
# ```
# Man gibt links vom Doppelpunkt an, ab welchem Index gestarten werden soll und rechts vom Doppelpunkt an, ab welchem Index aufgehört werden soll.
# Will man eine der beiden Seiten unverändert lassen, so kann man jene Seite vom Doppelpunkt leer lassen.
# 
# 
# Hierbei gibt es die drei Optionen:
# 
# Case A:
# Liste bis exklusive Index <code>b</code>.
# Man gibt hier also mit <code>b</code> den ersten Index an, welcher bereits NICHT zur Sublist gehören soll:\
# <code>arr[:b]</code>
# ```Python
# arr = [1, 2, 3, 4, 5]
# #index 0  1  2  3  4
# print(arr[:3])
# # [1, 2, 3]
# ```
# Das obere Beispiel wäre identisch zu <code>arr[0:3]</code>. 
# Da man hier die Linke Seite des Doppelpunktes frei lässt, weiß Python, dass man die Sublist beim Anfang der originalen Liste starten lassen möchte.
# Es wäre ebenfalls identisch zu <code>arr[:-2]</code>, da man mit dem Index <code>-2</code>, auf das vorletzte Element zugreift, welches das Element an Index <code>3</code> ist.
# 
# 
# Case B:
# Liste ab inklusive Index <code>a</code>:\
# <code>arr[a:]</code>
# ```Python
# arr = [1, 2, 3, 4, 5]
# #index 0  1  2  3  4
# print(arr[2:])
# # [3, 4, 5]
# ```
# <code>arr[2:]</code> entspricht <code>arr[2:len(arr)]</code>, 
# da die Länge einer List der erste Index ist, welcher nicht mehr Teil der Liste ist.
# Wenn der höchste Index <code>4</code> wäre, würde man also sagen:
# bis exklusive Index <code>5</code>.
# 
# 
# Case C:
# Liste ab inklusive Index <code>a</code> und bis exklusive Index <code>b</code>:\
# <code>arr[a:b]</code>
# ```Python
# arr = [1, 2, 3, 4, 5]
# #index 0  1  2  3  4
# print(arr[1:3])
# # [2, 3]
# ```
# Ab Index <code>2</code> bis exklusive Index <code>3</code>
# 
# Um die originale List mit einer Sublist zu überschreiben, kann den Zuweisungsoperator nutzen.
# 
# ```Python
# arr1 = arr[:-1]   # entfernt das letzte Element
# arr2 = arr[1:]    # entfernt das erste Element
# arr3 = arr[2:-2]  # entfernt die ersten zwei und die letzten zwei Elemente
# ```

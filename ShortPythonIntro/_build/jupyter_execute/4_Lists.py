#!/usr/bin/env python
# coding: utf-8

# # Lists
# 
# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

# ## Lists allgemein

# Die am meisten benutzte Datenstruktur ist das Array.
# Python nennt es jedoch nicht ein "Array", sondern eine "List".
# Von der Idee her sind sie identisch. Man hat eine Datenstruktur worin man Daten speichern möchte.
# 
# Viele andere Programmiersprachen benutzen geschweifte Klammern wie bei Codeblocks, um Arrays zu befüllen.
# 
# Ein Beispiel aus C:
# ```C
# int ArrayNameHier[] = {1, 2, 3, 4, 5};
# ```
# In Python werden eckige Klammern genutzt um Lists zu symbolisieren.
# ```Python
# ListNameHier = [1, 2, 3, 4, 5]
# ```
# Bei dem vorherigen Python Beispiel, wird nirgendwo gesagt, dass es sich bei dieser List um eine Integer List handelt.
# 
# Das liegt wieder am Dynamic Typing.
# Nur handelt es sich hier nicht einmal intern um eine Integer List.
# 
# Man könnte nämlich einen anderen Datentypen als einen Integer einfügen.
# 
# Beispiel:
# ```Python
# my_list = [1, 2, 3, 4, 5, "Hello World!"]
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
# print(type(my_list[0]))
# # <class 'int'>
# # --> Objekt am Index 0 ist ein Integer
# 
# print(type(my_list[5]))
# # <class 'str'>
# # --> Objekt am Index 5 ist ein String
# ```
# Somit handelt es unüberraschender Weise bei <code>1</code> um einen Integer und bei
# <code>"Hello World!"</code> um einen String.
# 
# ## Listen umkehren
# 
# Will man etwa die Liste 
# ```Python
# nums = [1, 2, 3, 4, 5]
# ```
# umkehren, sodass die Liste bei <code>5</code> anfängt und bei <code>1</code> endet, so kann man dafür die Funktion <code>reverse()</code> nutzen. 
# Hierbei handelt es sich um eine ähnliche Funktion wie <code>sort()</code>, welche statt zu Sortieren, die Liste umkehrt.
# 
# ```Python
# nums = [1, 2, 3, 4, 5]
# 
# print(nums)
# # [1, 2, 3, 4, 5]
# 
# nums.reverse()
# 
# print(nums)
# # [5, 4, 3, 2, 1]
# ```
# ## Schnelle Listen initialisation
# 
# Wenn man eine Liste mit einer bestimmten Anzahl von einem einzigen Wert initialisieren möchte, z.B.: Eine Liste mit 10 nullen, so kann man es entweder <code>append()</code> arbeiten und 10 mal eine null an die Liste anhängen:
# ```Python
# nums = []
# for i in range(0, 10):  # Diese Schleife läuft 10 mal
#     nums.append(0)
#     
# print(nums)
# # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ```
# 
# Alternativ gibt es für genau soetwas einen Shortcut in Python. Die Syntax funktioniert so:
# ```Python
# LIST_NAME = [WERT] * WIE_OFT_DER_WERT_VORKOMMEN_SOLL
# ```
# 
# für das obige Beispiel also:
# 
# ```Python
# nums = [0] * 10
# 
# print(nums)
# # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ```
# 
# 
# ## Negative Indizes
# 
# Python verfügt über einen praktischen Shortcut um auf k-t letzte Element in einer List (hier namens "nums") zuzugreifen.
# 
# Und zwar mit der Syntax: <code>nums[-k]</code>
# 
# Also mit einem negativen Index.
# 
# <code>nums[-1]</code> greift auf das letzte Element zu, <code>nums[-2]</code> greift auf das vorletzte Element zu und so weiter.
# 
# Dabei sollte man beim Programmieren beachten, dass negative Indizes in Python gültig sind und nicht zwingend zu einem Fehler führen.
# 
# 
# ## Length funktion
# 
# Um die Länge eines Arrays herauszufinden, benutzt man die <code>len()</code> funktion
# ```Python
# nums = [1, 2, 3, 4, 5]
# print(len(nums))
# # 5
# ```
# 
# ## Append
# 
# Um einen Wert zu einer bereits existierenden Liste hinzuzufügen, kann die sehr hilfreiche <code>append()</code> funktion genutzt werden.
# 
# ```Python
# nums = [1, 2, 3, 4, 5]
# print(nums)
# # [1, 2, 3, 4, 5]
# print(len(nums))
# # 5
# 
# nums.append(6)
# print(nums)
# # [1, 2, 3, 4, 5, 6]
# print(len(nums))
# # 6
# ```
# Man kann soviel appenden wie man möchte, da eine List eine dynamische Datenstruktur ist.
# Im Gegensatz zu Arrays in C, muss man nicht wissen wie lang die List höchstens sein darf.
# 
# Es ist auch möglich eine leere List zu erstellen, die man anscheließend mit append befüllt.
# 
# Eine leere Liste wird wie folgt initialisiert:
# ```Python
# nums = []
# ```
# 
# ## Slicing
# 
# Das Konzept von Slicing wird genutzt, um eine Sublist einer Liste zu nehmen.
# Also eine Teilmenge einer bereits existierenden Liste. Beim Slicing geht es lediglich um die Position der Elemente.
# 
# Um eine Untermenge abhängig von einer Bedinung zu nehmen, wie etwa
# "alle Werte aus nums, welche größer als 5 sind", benutzt man sogenannte List Comprehension.
# Für diese Einführung ist dies jedoch viel zu fortgeschritten.
# Interessierte können selbst danach recherchieren.
# 
# 
# Zurück zum Slicing. Hierbei geht es beispielsweise darum, eine Sublist bestehend aus allen Elementen ab Index a oder allen Elementen bis ausschließlich Index b oder einer Kombination davon, zu erstellen.
# 
# Hierfür wird folgende Syntax benutzt
# ```Python
# nums[a:b]
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
# <code>nums[:b]</code>
# ```Python
# nums = [1, 2, 3, 4, 5]
# #index 0  1  2  3  4
# print(nums[:3])
# # [1, 2, 3]
# ```
# Das obere Beispiel wäre identisch zu <code>nums[0:3]</code>. 
# Da man hier die Linke Seite des Doppelpunktes frei lässt, weiß Python, dass man die Sublist beim Anfang der originalen Liste starten lassen möchte.
# Es wäre ebenfalls identisch zu <code>nums[:-2]</code>, da man mit dem Index <code>-2</code>, auf das vorletzte Element zugreift, welches das Element an Index <code>3</code> ist.
# 
# 
# Case B:
# Liste ab inklusive Index <code>a</code>:\
# <code>nums[a:]</code>
# ```Python
# nums = [1, 2, 3, 4, 5]
# #index 0  1  2  3  4
# print(nums[2:])
# # [3, 4, 5]
# ```
# <code>nums[2:]</code> entspricht <code>nums[2:len(nums)]</code>, 
# da die Länge einer List der erste Index ist, welcher nicht mehr Teil der Liste ist.
# Wenn der höchste Index <code>4</code> wäre, würde man also sagen:
# bis exklusive Index <code>5</code>.
# 
# 
# Case C:
# Liste ab inklusive Index <code>a</code> und bis exklusive Index <code>b</code>:\
# <code>nums[a:b]</code>
# ```Python
# nums = [1, 2, 3, 4, 5]
# #index 0  1  2  3  4
# print(nums[1:3])
# # [2, 3]
# ```
# Ab Index <code>2</code> bis exklusive Index <code>3</code>
# 
# Um die originale List mit einer Sublist zu überschreiben, kann den Zuweisungsoperator nutzen.
# 
# ```Python
# nums = nums[:-1]   # entfernt das letzte Element
# nums = nums[1:]    # entfernt das erste Element
# nums = nums[2:-2]  # entfernt die ersten zwei und die letzten zwei Elemente
# ```

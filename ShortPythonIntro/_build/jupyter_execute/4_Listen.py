#!/usr/bin/env python
# coding: utf-8

# # Listen

# ## Listen allgemein

# Eine häufig benutzte Datenstruktur ist das "Array".
# In Python gibt es eine "Liste".
# Von der Idee her sind sie identisch. Man hat eine lineare Datenstruktur, in der man Daten speichern kann.
# 
# Viele andere Programmiersprachen benutzen geschweifte Klammern wie bei Codeblöcken, um Arrays zu befüllen.
# 
# Ein Beispiel aus C:
# ```C
# int ArrayNameHier[] = {1, 2, 3, 4, 5};
# ```
# In Python werden eckige Klammern genutzt, um Listen zu symbolisieren.
# ```Python
# ListenNameHier = [1, 2, 3, 4, 5]
# ```
# Im vorherigen Python-Beispiel wird nirgendwo gesagt, dass es sich bei dieser Liste um eine Integer-Liste handelt.
# 
# Das liegt wieder am Dynamic Typing.
# Nur handelt es sich hier nicht einmal intern um eine Integer-Liste.
# Man könnte nämlich einen anderen Datentypen als einen Integer einfügen.
# 
# Beispiel:
# ```Python
# my_list = [1, 2, 3, 4, 5, "Hello World!"]
# ```
# In den meisten anderen Programmiersprachen wäre das so einfach nicht möglich.
# Es liegt auch nicht daran, dass die Ziffern 1 bis 5 zu Strings übersetzt werden.
# Es gibt in der obigen Liste zwei verschiedene Datentypen.
# Dies kann mit der Funktion <code>type()</code> überprüft werden, welche wir bereits beim Testen von Dynamic Typing in einem früheren Kapitel kennen gelernt haben.
# 
# Nochmal eine kurze Erinnerung:
# Die Funktion <code>type(objekt)</code> gibt (als Klasse <code>class</code>) den Datentyp von <code>objekt</code> zurück, also zum Beispiel Integer, String oder Liste.
# 
# Rufen wir jetzt diese Funktionen auf, sehen wir folgendes.
# Wir benutzen wie üblich eckige Klammern mit einem Index dazwischen, um auf einen bestimmten (bei 0 anfangenden) Index einer Liste zuzugreifen.
# ```Python
# print(type(my_list[0]))
# # <class 'int'>
# # --> Objekt am Index 0 ist ein Integer
# 
# print(type(my_list[5]))
# # <class 'str'>
# # --> Objekt am Index 5 ist ein String
# ```
# Somit handelt es bei <code>1</code> um einen Integer und bei
# <code>"Hello World!"</code> um einen String.
# 
# ## Listen umkehren
# 
# Möchte man die Liste 
# ```Python
# nums = [1, 2, 3, 4, 5]
# ```
# umkehren, so dass die Liste bei <code>5</code> anfängt und bei <code>1</code> endet, dann kann man dafür die Funktion <code>reverse()</code> nutzen. 
# Hierbei handelt es sich um eine ähnliche Funktion wie <code>sort()</code>, welche die Liste umkehrt.
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
# ## Schnelle Initialisierung von Listen
# 
# Wenn man eine Liste mit einer bestimmten Anzahl von einem einzigen Wert initialisieren möchte, zum Beispiel eine Liste mit 10 Nullen, so kann man entweder mit <code>append()</code> arbeiten und 10 Mal eine Null an die Liste anhängen:
# ```Python
# nums = []
# for i in range(0, 10):  # Diese Schleife läuft 10 Mal
#     nums.append(0)
#     
# print(nums)
# # [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]
# ```
# 
# Alternativ gibt es für genau so etwas einen Shortcut in Python mit folgender Syntax:
# ```Python
# LISTEN_NAME = [WERT] * WIE_OFT_DER_WERT_VORKOMMEN_SOLL
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
# Python verfügt über einen praktischen Shortcut, um auf das k-letzte Element in einer Liste (hier namens "nums") zuzugreifen.
# 
# Und zwar mit der Syntax: <code>nums[-k]</code>
# 
# Also mit einem negativen Index.
# 
# <code>nums[-1]</code> greift auf das letzte Element zu, <code>nums[-2]</code> auf das vorletzte Element, und so weiter.
# 
# Dabei sollte man beim Programmieren beachten, dass negative Indizes in Python gültig sind und nicht zwingend zu einem Fehler führen.
# 
# 
# ## Länge einer Liste
# 
# Um die Länge einer Liste herauszufinden, benutzt man die <code>len()</code> Funktion genauso wie man auch die Länge eines Strings herausfinden kann.
# ```Python
# nums = [1, 2, 3, 4, 5]
# print(len(nums))
# # 5
# ```
# 
# ## Append
# 
# Um einen Wert zu einer bereits existierenden Liste hinzuzufügen, kann die sehr hilfreiche <code>append()</code>-Funktion genutzt werden.
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
# Man kann soviel hinzufügen, wie man möchte, da eine Liste eine dynamische Datenstruktur ist.
# Im Gegensatz zu Arrays in C muss man nicht wissen, wie lang die Liste ist.
# 
# Es ist auch möglich eine leere Liste zu erstellen, die man anschließend mit <code>append()</code> befüllt.
# 
# Eine leere Liste wird wie folgt initialisiert:
# ```Python
# nums = []
# ```
# 
# ## Listen konkatenieren
# 
# Um zwei Listen zu konkatenieren, kann man den Operator <code>+</code> nutzen. Wie auch bei Strings <code>+</code> bei Listen ebenfalls für eine Konkatenierung. Man kann diesen Operator so nutzen:
# ```Python
# a = [1, 2, 3]
# b = [4, 5, 6]
# 
# print(a + b)
# # [1, 2, 3, 4, 5, 6]
# ```
# 
# ## Slicing
# 
# Das Konzept von Slicing wird genutzt, um aus einer Liste eine zusammenhängende Teilliste zu erhalten.
# Dazu werden zwei Indices angegeben.
# 
# Um eine Untermenge abhängig von einer Bedingung zu erhalten, wie etwa
# "alle Werte aus nums, welche größer als 5 sind", benutzt man sogenannte List Comprehension.
# Für diese Einführung ist dies jedoch viel zu fortgeschritten.
# Interessierte können selbst danach recherchieren.
# 
# Zurück zum Slicing. Hierbei geht es beispielsweise darum, eine Teilliste, bestehend aus allen Elementen ab Index a oder allen Elementen bis ausschließlich Index b oder auch einer Kombination davon, zu erstellen.
# 
# Hierfür wird folgende Syntax benutzt
# ```Python
# nums[a:b]
# ```
# Man gibt links vom Doppelpunkt an, ab welchem Index gestartet werden soll und rechts vom Doppelpunkt, ab welchem Index aufgehört werden soll.
# Will man eine der beiden Seiten unverändert lassen, so kann man jene Seite vom Doppelpunkt leer lassen.
# 
# 
# Hierbei gibt es die drei Optionen:
# 
# Fall A:
# Liste bis (und exklusiv) Index <code>b</code>.
# Man gibt hier also mit <code>b</code> den ersten Index an, welcher bereits **nicht** zur Unterliste gehören soll:\
# <code>nums[:b]</code>
# ```Python
# nums = [1, 2, 3, 4, 5]
# #index 0  1  2  3  4
# print(nums[:3])
# # [1, 2, 3]
# ```
# Das obere Beispiel wäre identisch zu <code>nums[0:3]</code>. 
# Da man hier die linke Seite des Doppelpunktes frei lässt, weiß Python, dass man die Teilliste beim Anfang der originalen Liste starten lassen möchte.
# Es wäre ebenfalls identisch zu <code>nums[:-2]</code>, da man mit dem Index <code>-2</code>, auf das vorletzte Element zugreift, welches das Element an Index <code>3</code> ist.
# 
# 
# Fall B:
# Liste ab (und inklusiv) Index <code>a</code>:\
# <code>nums[a:]</code>
# ```Python
# nums = [1, 2, 3, 4, 5]
# #index 0  1  2  3  4
# print(nums[2:])
# # [3, 4, 5]
# ```
# <code>nums[2:]</code> entspricht <code>nums[2:len(nums)]</code>, 
# da die Länge einer Liste der erste Index ist, welcher nicht mehr Teil der Liste ist.
# Wenn der höchste Index <code>4</code> wäre, würde man also sagen:
# bis exklusiv Index <code>5</code>.
# 
# 
# Fall C:
# Liste ab (und inklusiv) Index <code>a</code> und bis (und exklusiv) Index <code>b</code>:\
# <code>nums[a:b]</code>
# ```Python
# nums = [1, 2, 3, 4, 5]
# #index 0  1  2  3  4
# print(nums[1:3])
# # [2, 3]
# ```
# Ab Index <code>1</code> bis (und exklusiv) Index <code>3</code>
# 
# Um die originale Liste mit einer neuen Teilliste zu überschreiben, kann man den Zuweisungsoperator nutzen.
# 
# ```Python
# nums = nums[:-1]   # entfernt das letzte Element
# nums = nums[1:]    # entfernt das erste Element
# nums = nums[2:-2]  # entfernt die ersten zwei und die letzten zwei Elemente
# ```
# 
# ## Löschen in einer Liste
# 
# Um bestimmte Elemente in einer Liste zu löschen, gibt es drei Möglichkeiten.
# 
# Möglichkeit 1:
# 
# Wenn die zu löschenden Werte am Anfang oder am Ende der Liste stehen, so kann man diese mit Slicing entfernen. Löschen des ersten Elementes in einer Liste:
# ```Python
# nums = nums[1:]
# ```
# Der Vorteil liegt darin, dass man mit einer Operation gleich mehrere Elemente löschen kann. So kann man etwa mit <code>nums = nums[3:]</code> gleich die ersten drei Elemente löschen.
# 
# Möglichkeit 2:
# 
# Zum Löschen eines bestimmten Elements, kann man das Keyword <code>del</code> nutzen. Die Syntax sieht so aus:
# ```Python
# del nums[zu_löschender_index]
# ```
# 
# Möglichkeit 3:
# 
# Wenn man nur das erste Element der Liste löschen möchte, so kann man die Funktion <code>pop()</code> nutzen:
# ```Python
# nums.pop()
# ```
# Man kann es sich vorstellen als die umgekehrte Funktion zu <code>append()</code>, die am Ende der Liste einfügt.

# ## Aufgabe

# Gegeben seien die Listen <code>a</code>, <code>b</code>, <code>c</code> und <code>d</code>. Ihre Aufgabe ist es nun, dafür zu sorgen, dass bei dem Aufruf <code>print(nums)</code> die angegebene Ausgabe erscheint.
# 
# Sie dürfen nur Slicing und Konkatenierung benutzen.

# Um klarer zu machen, was gemacht werden soll, hier ein willkürliches Beispiel:
# ```Python
# # Ausgabe soll sein: [1, 2, 3, 4, 5, 6, 7, 8, 9]
# 
# a = [0, 0, 5, 6, 0]
# b = [1, 2, 3, 4, 0, 0, 0]
# c = [0, 0, 7, 8, 9]
# 
# 
# # Eine mögliche Lösung könnte sein:
# nums = b[:4] + a[2:4] + c[2:]
# 
# 
# print(nums)
# # [1, 2, 3, 4, 5, 6, 7, 8, 9]
# ```

# In[1]:


# Hier können Sie ihren Versuch schreiben...
# Ausgabe soll sein: [64, 7, 4, 7, 6, 34, 1, 2, 3, 6, 2]

a = [6, 34, 12, 1, 3]
b = [62, 7, 5, 3, 6, 2]
c = [1, 2, 3]
d = [9, 64, 7, 4, 7, 4]


nums = ...


print(nums)
# --> Die Ausgabe soll sein:
# [64, 7, 4, 7, 6, 34, 1, 2, 3, 6, 2]


# :::{admonition} Lösung
# :class: dropdown
# 
# ```Python
# a = [6, 34, 12, 1, 3]
# b = [62, 7, 5, 3, 6, 2]
# c = [1, 2, 3]
# d = [9, 64, 7, 4, 7, 4]
# 
# 
# # Option 1:
# nums = d[1:5] + a[:2] + c + b[4:]
# 
# # Option 2 mit negativen Indizes:
# nums = d[1:-1] + a[:-3] + c + b[-2:]
# 
# # Eine Kombination von den beiden Optionen ist auch möglich.
# 
# print(nums)
# # [64, 7, 4, 7, 6, 34, 1, 2, 3, 6, 2]
# ```
# 
# Es ist ebenfalls möglich, jedes benötigte Element einzeln zu konkatenieren. <code>a[1:2]</code> ist äquivalent zu <code>a[1]</code>.
# (Von Index <code>1</code> bis (und exklusive) Index <code>2</code> --> nur Index <code>1</code>.)
# 
# Da es sich technisch gesehen immer noch um Slicing handelt, 
# würde es jedoch nicht gegen die Regeln verstoßen. <code>a[1]</code> hingegen schon.
# Also könnte man oben <code>[64, 7, 4, 7]</code> auch durch <code>d[1:2] + d[2:3] + d[3:4] + d[4:5]</code> erhalten. 
# 
# Das ist aber definitiv mühsamer.
# Noch ein weiterer Grund, wieso Slicing hier einiges an Arbeit sparen kann.
# 
# :::

#!/usr/bin/env python
# coding: utf-8

# # Weitere Aufgaben

# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

# ## FizzBuzz

# Eine sehr beliebte Aufgabe für Einsteiger einer Programmiersprache, ist das FizzBuzz Problem.
# 
# Das Problem sieht wie folgt aus:
# 
# - Es sollen die Zahlen 1 bis inklusive 100 untereinander ausgegeben werden.
# 
# - Hierbei sollen jedoch Zahlen, welche durch 3 teilbar sind, durch den String <code>"Fizz"</code> ersetzt werden.
# 
# - Zahlen, welche durch 5 teilbar sind, sollen durch den String <code>"Buzz"</code> ersetzt werden.
# 
# - Wenn eine Zahl durch 3 als auch durch 5 teilbar ist, soll die Zahl durch den String <code>"FizzBuzz"</code> ersetzt werden
# 
# 
# Der Output soll so aussehen:

# ```
# Output    (Zahl)
# 
# 1         1
# 2         2
# Fizz      3
# 4         4
# Buzz      5
# Fizz      6
# 7         7
# 8         8
# Fizz      9
# Buzz      10
# 11        11
# Fizz      12
# 13        13
# 14        14
# FizzBuzz  15
# 16        16
# ...       ...
# 98        98
# Fizz      99
# Buzz      100
# ```
# 
# Die Zahlen rechts sind nur zur Veranschaulichung da. Sie müssen diese nicht ausgeben lassen!

# ### Ihre Antwort

# In[1]:


# Hier können Sie das FizzBuzz Problem lösen


# :::{admonition} Lösung für FizzBuzz
# :class: dropdown
# 
# ```Python
# for number in range(1, 101):
#     if number % 3 == 0 and number % 5 == 0:
#         print("FizzBuzz")
#     elif number % 3 == 0:
#         print("Fizz")
#     elif number % 5 == 0:
#         print("Buzz")
#     else:
#         print(number)
# ```
# 
# Erklärung der obigen Lösung: 
# 
# <code>range(1, 101)</code>, da es bei <code>1</code> starten soll und bis inklusive <code>100</code> gehen soll. (Inklusive <code>100</code> --> Exklusive <code>101</code> --> <code>range(1, 101)</code>)
# 
# Zahl ist durch <code>n</code> teilbar --> <code>zahl % n == 0</code>.
# 
# Sprich: Es gibt keinen Rest bei der Division <code>zahl / n</code>.
# 
# Es gibt viele Lösungen für diese bekannte Programmieraufgabe. Man könnte etwa mit Strings arbeiten und bei bedarf Fizz und Buzz konkatenieren.
# Alternativ könnte man auch mit Lambdas arbeiten, das ist hier definitiv aber nicht von Relevanz.
# 
# :::

# ## Palindrome

# Ein Palindrom ist ein Wort, welches egal ob von links nach rechts oder von rechts nach links gelesen, identisch ist. 
# 
# Sprich: Man kann das Wort in der Mitte des Wortes spiegeln und es verändert sich nichts.
# 
# Beispiele: Radar, Rentner
# 
# ```
# Wort:   R A D A R
# Index:  0 1 2 3 4
# 
# Wort:   R A D A R
# Index:  4 3 2 1 0
# ```
# 
# Egal ob man "Radar" von links nach rechts oder von rechts nach links liest, verändert sich das Wort nicht. Groß- und Kleinschreibung soll ignoriert werden.

# Ihre Aufgabe ist es nun eine Funktion zu schreiben, welche ein Wort als Input erhält und zurückggibt ob es sich um ein Palindrom handelt oder nicht.
# Wenn es sich um ein Palindrom handelt, wird <code>True</code> zurückgegeben. Ansonsten <code>False</code>.
# Um es zu vereinfachen, gehen Sie davon aus, dass wirklich nur ein Wort angegeben wird. Also keine Leerzeichen, usw. Zusätzlich wird das Wort nur in Kleinbuchstaben angegeben. Statt "Radar" würde also etwa "radar" eingegeben werden.

# In[2]:


# Hier können Sie das Palindrom Problem lösen


# :::{admonition} Lösung für Palindrome
# :class: dropdown
# 
# Die wahrscheinlich einfachste Variante. Man kehrt den String einfach um. Wenn der umgekehrte String dem eigentlichen String gleicht, so handelt es sich um ein Palindrom.
# Um den String umzukehren, erstellt man einen leeren String und konkateniert alle Buchstaben des eigentlichen Strings, jedoch fängt man von hinten an. Deswegen <code>reversed(range())</code>.
# Man muss konkatenieren anstatt eine Indexzuweisung zu machen, da Strings in Python <code>immutable</code> sind und somit man nicht einen bestimmten Buchstaben an einem beliebigen Index verändern kann. 
# 
# ```Python
# def palindrom_string_reversal(string):
#     reversed_string = ""
#     for index in reversed(range(0, len(string))):
#         reversed_string += string[index]
#     return string == reversed_string
# 
# ```
# 
# Bei einer anderen Variante, muss man den String gar nicht umkehren. Alle Vergleiche werden im selben String durchgeführt.
# Hier guckt man ob der erste Buchstabe von links dem ersten Buchstaben von rechts gleicht. Dann guckt man ob der zweite Buchstabe von links dem zweiten Buchstaben von rechts gleicht. Dies macht man bis man in der Mitte angekommen ist. Wenn man dort ankommt und man keine Stelle gefunden hat, wo auf beiden Seiten nicht das gleiche steht, so handelt es sich um ein Palindrom. Wenn man irgendwo einen Widerspruch findet, wird sich gemerkt, dass es kein Palindrom ist und der Vergleich wird abgebrochen, da ein Widerspruch ausreicht, damit es kein Palindrom ist.
# 
# Erklärung des Codes:
# "es_ist_ein_palindrom" wird auf <code>True</code> gesetzt, da man am Anfang davon ausgeht, dass es sich um ein Palindrom handelt.
# Für die Zählervariable wird der Bereich <code>range(0, len(string) // 2)</code> genutzt. Mit <code>len(string)</code> erhält man die Länge des Wortes. Mit dem <code>//</code> Operator, führt man eine Division durch und rundet das Ergebnis auf den nächstkleineren Integerwert. Man kann durch ausprobieren überprüfen, dass die Zählervariable bei einer geraden Wortlänge bei dem linken der beiden mittleren Buchstaben endet und bei Worten mit ungerader Wortlänge, endet die Zählervariable links von dem mittleren Buchstaben, da der mittlere Buchstabe selbst nicht überprüft werden muss, da dieser genau in der Mitte ist und eine Spiegelung nichts an diesem Buchstaben ändern kann.
# 
# Um sowohl auf einen linken als auch auf einen rechten Buchstaben zuzugreifen, benutzt man die Indizes <code>index</code> und <code>-(index+1)</code>. Mit dem Index <code>-1</code> greift man auf das erste Element von rechts zu. Da Indizes aber bei <code>0</code> starten, muss man auf den negativen Index <code>1</code> addieren.
# 
# Die in Verbindung stehenden Paare wäre also die Indizes <code>{0, -1}, {1, -2}, {2, -3}, {3, -4}, ...</code>
# Allgemein: <code>{index, -(index+1)}</code>. So kommt man auf die Formel. 
# 
# Wenn es nun eine Stelle gibt, welche die Voraussetzung für ein Palindrom verletzt, so wird "es_ist_ein_palindrom" auf <code>False</code> gesetzt. Optional um Zeit zu sparen, kann man mit <code>break</code> die For-Schleife beenden, da bereits gezeigt wurde, dass es sich nicht um ein Palindrom handelt. Somit sind weitere Vergleiche nutzlos.
# 
# Schließlich gibt man zuück ob es sich ein Palindrom handelt oder nicht.
# 
# ```Python
# def palindrom_check_from_both_sides(string):
#     es_ist_ein_palindrom = True
#     for index in range(0, len(string) // 2):
#         if string[index] != string[-(index+1)]:
#             es_ist_ein_palindrom = False
#             break
#     return es_ist_ein_palindrom
# ```
# 
# :::

# In[ ]:





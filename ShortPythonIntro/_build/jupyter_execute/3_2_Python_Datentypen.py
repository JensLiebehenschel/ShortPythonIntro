#!/usr/bin/env python
# coding: utf-8

# # Datentypen

# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

# ## Dynamic Typing
# 
# Python hat alle gängigen Datentypen die man aus anderen Programmiersprachen kennt. Seien es Integer, Gleitkommazahlen oder Strings.
# Der Unterschied in Python ist, dass sich der Programmierer in der Regel nicht um Datentypen kümmern muss.
# Der Grund dafür liegt in Pythons "Dynamic Typing"
# Hier nochmal die Erklärung.
# Beim Dynamic Typing, kümmert sich einfach gesagt, der Python Interpreter um Datentypen und der Programmierer muss diese nicht konkret angeben.
# 
# Dies macht es sehr einfach mit Python zu arbeiten, da man weniger tippen muss und sich nicht überlegen zu braucht, ob eine bestimmte Variable immer ein Integer bleibt, oder ob es nicht doch ein Szenario gibt, in welchem daraus eine Gleitkommazahl werden könnte.
# Wenn man eine Zahl jedoch in einem bestimmten Datentyp haben will, so kann man Typecasting machen und somit den Typen explizit angeben. Dieser kann sich dann aber trotzdem noch ändern, wenn man der Variable einen neuen Wert zuweist.

# ```Python
# x = 5
# x = str(x)
# 
# # Bei isinstance(x, datentyp) handelt es es sich um eine Funktion, 
# # welche überprüft ob das Objekt x vom angegebenen Datentypen ist 
# # und gibt im Fall einer Übereinstimmung "True" zurück. Ansonsten "False".
# 
# # Überprüfen ob x ein String ist
# isinstance(x, str)
# # Gibt True zurück. Die Variable x ist ein String
# 
# # Überprüfen ob x ein Integer ist
# isinstance(x, int)
# #--> Gibt False zurück. Die Variable x ist kein Integer
# ```

# ## Hinweis zu Semikola
# 
# Wie vom aufmerksamen Leser bereits bemerkt, hat keines dieser Statements ein Semikolon am Ende. Dies ist kein Fehler.
# Semikolons werden am Ende einer Zeile nicht benötigt.
# Der einzige Nutzen von Semikolons ist das ausführen von mehreren Statements in der selben Zeile.\
# Beispiel:

# ```Python
# x = 5; print(x)
# ```

# ## Hinweis zu Strings
# 
# In Python können Strings entweder mit normalen Anführungszeichen oder mit einfachen Anführungszeichen angegeben werden.
# Man kann auch innerhalb eines Programms beides benutzen, jedoch kann man nicht beides innerhalb von einem String benutzen.

# Gültig:
# ```Python
# "Text"
# 'Text'
# ```
# 
# Ungültig:
# ```Python
# "Text'
# 'Text"
# ```

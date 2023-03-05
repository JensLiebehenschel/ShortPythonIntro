#!/usr/bin/env python
# coding: utf-8

# # Logische Ausdrücke

# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

# ## Der Boolean Datentyp

# Nun geht es um logische Ausdrücke.
# 
# In Python gibt es den Datentyp Boolean.
# Dieser kann zwei Werte haben: Wahr und Falsch
# 
# auf Englisch True und False.
# 
# <code>True</code> und <code>False</code> sind hierbei keine Strings, sondern keywords.
# Man muss mit der Groß- und Kleinschreibung aufpassen, denn es ist nur korrekt, wenn der Anfangsbuchstabe groß ist und der Rest klein.
# ```Python
# Korrekt:
# x = True
# y = False
# 
# Falsch:
# x = true
# y = false
# x = TRUE
# y = FALSE
# x = tRuE
# y = fAlSe
# ```
# Benutzt man einen Editor mit Python Syntax Highlighting oder gar Autocompletion, wird man anhand der Hervorhebung wie beim Beispiel oben, erkennen, ob man es richtig geschrieben hat oder nicht. Zumindest bis man sich daran sowieso gewöhnt hat.

# ## Logische Ausdrücke

# Der Vergleichsoperator, welcher auf Gleichteit prüft ist wie fast überall auch ein <code>&equals;&equals;</code>.
# ```Python
# x = 5
# y = 5
# 
# wahrheitsert = x == y
# print(wahrheitswert)
# # True
# ```
# Vergleiche von konkreten Werten sind mit <code>&gt;,&lt;,&gt;&equals;,&lt;&equals;</code> ebenfalls möglich.
# 
# Um einen booleschen Ausdruck zu negieren, benutzt man in C ein Ausrufezeichen:
# ```C
# int x = 5;
# int y = 5;
# 
# printf("%d", !(x == y));
# // 0 bzw. False
# ```
# In Python gibt es dafür das keyword <code>not</code>.
# Das oben geschriebene Beispiel in Python wäre also
# ```Python
# x = 5
# y = 5
# 
# print(not (x == y))
# # False
# ```
# 
# Die gleiche Vorgehensweise bei "logischem und" als auch beim "logischem oder".
# 
# Da wird <code>&amp;&amp;</code> durch das keyword <code>and</code>, und <code>||</code> durch das keyword <code>or</code> ersetzt.
# 
# ```C
# int x = 5;
# int y = 5;
# int z = 3;
# 
# printf("%d", (x == y) && (x == z || !(y < z)))
# // 1 bzw. True
# ```
# Python:
# ```Python
# x = 5
# y = 5
# z = 3
# 
# print((x == y) and (x == z or not (y < z)))
# # True
# ```

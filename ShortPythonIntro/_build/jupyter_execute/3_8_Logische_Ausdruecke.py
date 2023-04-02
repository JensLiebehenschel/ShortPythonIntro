#!/usr/bin/env python
# coding: utf-8

# # Logische Ausdrücke

# ## Der Datentyp Boolean

# Nun geht es um logische Ausdrücke.
# 
# In Python gibt es den Datentyp Boolean.
# Dieser kann zwei Werte annehmen: Wahr und Falsch, auf Englisch True und False.
# 
# <code>True</code> und <code>False</code> sind in Python Keywords.
# Der Anfangsbuchstabe muss groß geschrieben sein und der Rest klein.
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
# Benutzt man einen Editor mit Python Syntax Highlighting oder gar Autocompletion, wird man anhand der Hervorhebung wie beim Beispiel oben, erkennen, ob man es richtig geschrieben hat oder nicht.

# ## Logische Ausdrücke

# Der Vergleichsoperator, welcher auf Gleichheit prüft, ist wie in fast allen Programmiersprachen auch <code>&equals;&equals;</code>.
# Auf Ungleichheit prüft der Operator <code>!&equals;</code>.
# ```Python
# x = 5
# y = 5
# 
# print(x == y)
# # True
# 
# print(x != y)
# # False
# ```
# Um zu prüfen, ob eine Variable einen Nullwert hat, kann man entweder die obigen Vergleichsoperatoren oder das Keyword <code>is</code> nutzen:
# ```Python
# x = None
# 
# print(x == None)
# # True
# 
# print(x != None)
# # False
# 
# print(x is None)
# # True
# 
# print(x is not None)
# # False
# 
# # Alternativ:
# print(not x is None)
# # False
# ```
# 
# 
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
# Die gleiche Vorgehensweise gilt beim "logischen Und" und beim "logischen Oder".
# 
# Die entsprechenden Keywords sind <code>and</code> und <code>or</code>.
# 
# ```C
# int x = 1; // bzw. True
# int y = 0; // bzw. False
# int z = 1; // bzw. True
# 
# printf("%d", x && z);
# // 1 bzw. True
# 
# printf("%d", x && y);
# // 0 bzw. False
# 
# printf("%d", x || y);
# // 1 bzw. True
# ```
# Python:
# ```Python
# x = True
# y = False
# z = True
# 
# print(x and z)
# # True
# 
# print(x and y)
# # False
# 
# print(x or y)
# # True
# ```

# ## Aufgabe

# Gegeben ist ein logischer Ausdruck. Übersetzen Sie diesen Ausdruck in Python-Code. Damit Sie den Code ausführen können und somit Syntaxfehler vom Interpreter erhalten, nutzen Sie dafür die konkreten Werte $x=5$, $y=5$, $z=3$, $t=True$ und $f=False$.
# Durch eben diese konkreten Werte entstehen Tautologien. Es sollen **keine** Vereinfachungen durchgeführt werden.

# <font size="12">$ausdruck = $</font>
# 
# <font size="12">$(x=y \land ((x=z \lor \neg(y < z)) \lor$</font>  
# 
# <font size="12">$\neg((\neg t \lor f) \land (t \land \neg (x < z)))))$</font>

# Wenn Sie alternativ nicht den obigen Ausdruck nutzen möchten, können Sie auch den unten stehenden C-Code in Python-Code übersetzen. 
# Der C-Code unten und der Ausdruck oben sind äquivalent.

# :::{admonition} Äquivalenter C-Code als optionale Hilfe
# :class: dropdown
# 
# ```C
# // Äquivalenter C-Code
# int x = 5;
# int y = 5;
# int z = 3;
# int t = 1;
# int f = 0;
# 
# printf("%d", 
#     x==y && ( (x == z || !(y < z)) || !((!t || f) && (t && !(x < z)))) 
# );
# ```
# 
# :::

# ### Ihre Antwort

# In[1]:


# Hier können Sie ihren Versuch schreiben...
# Ersetzen Sie hierfür die drei Punkte unten durch Ihren Code.
x = 5
y = 5
z = 3
t = True
f = False

print(
    ...
)


# :::{admonition} Lösung
# :class: dropdown
# 
# Hier ist die Musterlösung. Sie können natürlich auch mehr Klammern nutzen, um nicht auf Bindungsstärke der Operatoren achten zu müssen.
# 
# ```Python
# x = 5
# y = 5
# z = 3
# t = True
# f = False
# 
# print( 
#     x == y and ( (x == z or not (y < z)) or not ((not t or f) and (t and not (x < z))))
# )
# # True
# ```
# 
# :::

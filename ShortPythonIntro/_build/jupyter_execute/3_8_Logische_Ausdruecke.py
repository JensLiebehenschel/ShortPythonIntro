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

# # Aufgabe

# Gegeben ist ein logischer Ausdruck. Übersetzen Sie diesen Ausdruck in Python code. Damit Sie den Code ausführen und somit auf Syntaxfehler vom Interpreter achten können, nutzen Sie dafür die konkreten Werte $x=5,\:y=5,\:z=3,\:t=True,\:f=False$.
# Durch eben diese konkreten Werte entstehen Tautologien. Es sollen **keine** vereinfachungen durchgeführt werden. 

# <font size="12">$ausdruck = $</font>
# 
# <font size="12">$(x=y \land ((x=z \lor \neg(y < z)) \lor$</font>  
# 
# <font size="12">$\neg((\neg t \lor f) \land (t \land \neg (x < z)))))$</font>

# Wenn Sie alternativ nicht den obigen Ausdruck nutzen möchten, können Sie auch den unten stehenden C-code in Python code übersetzen. 
# Der C-code unten und der Ausdruck oben sind äquivalent.

# ## Äquivalenter C-code als optionale Hilfe

# ```{toggle}
# ```C
# // Äquivalenter C-code
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

# ## Ihre Antwort

# In[1]:


# Hier können Sie ihren Versuch schreiben...
# Ersetzen Sie hierfür den String mit Ihrem Code.
x = 5
y = 5
z = 3
t = True
f = False

print(
    "Warten auf Ausdruck..."
)


# # Lösung

# ```{toggle}
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

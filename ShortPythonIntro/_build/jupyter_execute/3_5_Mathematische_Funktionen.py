#!/usr/bin/env python
# coding: utf-8

# # Bibliotheken und Mathematische Funktionen
# 
# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**
# 
# ## Importieren einer Bibliothek
# 
# Python hat eine enorme Auswahl an Bibliotheken.
# Seien es nun Bibliotheken um Grafiken zu erstellen oder Bibliotheken für Machine Learning.
# 
# Von Interesse für dieses Modul, sind jedoch mathematische Bibliotheken.
# Mit diesen Bibliotheken kann man etwa Funktion verwenden, um eine Quadratwurzel zu ziehen oder einen Logarithmus zu berechnen.
# 
# Um diese hilfreichen Funktionen nutzen zu können, muss man diese Bibliotheken erst importieren.
# Funktioniert von der Logik genauso wie das importieren von Bilbiotheken in C.
# Also gibt es ein Keyword gefolgt vom Bibliothekennamen, daraufhin kann man diese Bibliothek dann nutzen.
# 
# in C:
# ```C
# #include <Bibliotheksname.h>
# ```
# 
# in Python wird das Keyword <code>import</code> genutzt:
# ```Python
# import Bibliotheksname
# ```
# 
# Konkret um auf die Funktionen für die Quadratwurzel und die Logarithmen, muss man die Bibliothek <code>math</code> importieren.
# 
# Also braucht man die Zeile
# ```Python
# import math
# ```
# bevor man diese Funktionen nutzen kann.
# 
# 
# ## Funktionen der math Bibliothek
# 
# Nun haben wir die math Bibliothek importiert.
# 
# Um auf diese zuzugreifen, müssen wir vor den Funktionen einen Präfix von <code>Bibliotheksname.</code> hinzufügen, damit wir ausdrücken, dass wir die Funktion dieser Bibliothek meinen.
# 
# Konkret wäre der Präfix hier also <code>math.</code>
# 
# Die Quadratwurzel von 25 könnte man also wie folgt berechnen:
# ```Python
# x = math.sqrt(25)
# print(x)
# # 5
# ```
# 
# Um den 10-er Logarithmus von x zu berechnen, kann man die Funktion <code>math.log10(x)</code> nutzen
# ```Python
# x = math.log10(100)
# print(x)
# # 2
# ```
# 
# Weitere Funktionen wie etwa trigonometrische Funktionen können bei bedarf in der englischsprachigen <a href="https://docs.python.org/3/library/math.html" target="_blank">Python Referenz</a> nachgelesen werden.

# # Aufgabe
# 
# Hier ist die Gleichung für die Dichtefunktion der <a href="https://de.wikipedia.org/wiki/Normalverteilung" target="_blank">Normalverteilung</a>. Die Normalverteilung ist auch als "gaußsche Glockenkurve" bekannt.
# Es geht hier nicht darum, diese Formel zu verstehen. Den ersten Kontakt mit dieser Formel werden Sie im 3. Semester in Statistik haben und dort benutzt man Programme, welche Werte für diesen Ausdruck berechnen.
# Ich habe diese Formel ausgesucht, da man hier testen kann ob man mathematische Operatoren und Funktionen verstanden hat.
# Es geht nur darum, diese Formel in Code umzuschreiben und das Ergebnis zu berechnen für die konkreten Werte $ \mu =3 ,\: \sigma = 5 \:und\: x=4$.

# <font size="14">$f(x\:|\:\mu,\sigma^2)=\frac{1}{\sigma\sqrt{2\pi}}e^{-\frac{1}{2}(\frac{x-\mu}{\sigma})^2}$</font>

# Um Ihnen das Leben leichter zu machen, habe ich im Folgenden, die Formel umgeschrieben indem ich u.a alle griechischen Buchstaben (bis auf <code>pi</code>) einen anderen Namen gegeben habe. 
# Als Variablennamen sollen Sie nun die Ausdrücke der unten stehenden Gleichung verwenden.

# <font size="14">$result=\frac{1}{sigma\cdot\sqrt{2\cdot\pi}}\cdot e^{-\frac{1}{2}\cdot(\frac{x-mu}{sigma})^2}$</font>

# Den Wert für $\pi$ können Sie mit <code>math.pi</code> aufrufen.
# Den Wert für $e$ können Sie mit <code>math.e</code> aufrufen. Denken Sie an Klammersetzung.
# 
# Also zum Beispiel: 
# 
# ```Python
# result = (a + b + c
#          + d + e)
# ```
# 
# Viel Erfolg!

# In[1]:


# Hier können Sie ihren Versuch schreiben...
# Ersetzen sie hierfür "..." mit ihrem Code.
# Das Ergebnis der Formel soll geprinted werden.
# Bräuchten Sie vielleicht eine Bibliothek?

mu = 3
sigma = 5
x = 4
print(
    ...
)


# :::{admonition} Show solution
# :class: dropdown
# 
# ```Python
# import math
# mu = 3
# sigma = 5
# x = 4
# print(
#     (1/(sigma * math.sqrt(2*math.pi))) 
#     * math.e ** (-(1/2) * ((x-mu)/sigma) ** 2)
# )
# # 0.07820853879509118
# ```
# 
# Dies ist nur eine Musterlösung. 
# Sie können die Formel natürlich auch anders aufschreiben. 
# Solange das Ergebnis stimmt, ist Ihre Lösung sehr wahrscheinlich ebenfalls korrekt.
# 
# :::

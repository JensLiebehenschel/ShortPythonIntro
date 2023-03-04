#!/usr/bin/env python
# coding: utf-8

# # Schleifen

# ## **DIESE PYTHON EINFÜHRUNG IST WORK-IN-PROGRESS. ES KÖNNEN NOCH ÄNDERUNGEN VORGENOMMEN WERDEN.**

# Gängige Schleifen gibt es in Python ebenfalls mit den aus anderen Programmiersprachen bekannten Keywords <code>for</code> und <code>while</code>
# 
# Hier unterscheidet Python sich von den C-ähnlichen Programmiersprachen.
# Nicht von Idee her, aber von Syntax.
# 
# 
# ## For-Schleife
# 
# Etwa soll in C mit einer for-loop ein Codeblock so oft ausgeführt werden, wie es verschiedene Werte für die Zählervariable gibt. 
# Im AlgDat modul werden üblicherweise einbuchstabige Namen für die Zählervariablen gewählt.
# Das wären größtenteils <code>i</code> und <code>j</code>.
# 
# Python geht bei Schleifen wie folgt vor:
# Als Input in die schleife erhält man keine Formel und Bedinung, mit welcher diese Zählervariablen berechnet werden sollen, sondern übergibt man ein 
# "iterable" object.
# Also ein Array-artiges Object, wo man auf Basis von Indizes unterscheidet.
# 
# In C würde man eine <code>For-Schleife</code> startend bei <code>0</code> mit Schrittweite <code>1</code> also so erstellen:
# ```C
# for (int i = 0; i < wert_für_i_welcher_nicht_mehr_dazugehören_soll; i++) {
# 	<Codeblock>
# }
# ```
# Mit der Formel könnte man die einzelnen Werte für <code>i</code> berechnen.
# Man fängt bei <code>0</code> an und inkrementiert um <code>1</code>, bis der Wert erreicht wird, wo die Bedingung in der Mitte nicht mehr den Wahrheitswert <code>wahr</code> zurückgibt.
# 
# 
# In Python würde man hingegeben die Werte <code>0</code> bis zum Grenzwert in Form einer List übergeben.
# 
# Folgendes Beispiel in C:
# ```C
# for (int i = 0; i < 5; i++) {
# 	<Codeblock>
# }
# ```
# würde man in Python folgendermaßen erstellen:
# ```Python
# for i in [0, 1, 2, 3, 4]:
# 	<Codeblock>
# ```
# Das Keyword <code>in</code> sagt hier, dass der jeweils aktuelle Wert der List <code>[0, 1, 2, 3, 4]</code> als <code>i</code> anzusprechen sei.
# 
# Das Keyword kann nebenbei ebenfalls sehr einfach genutzt werden um festzustellen ob ein Wert in einer Liste enthalten ist.
# 
# ```Python
# x = [1,2,3,4,5]
# print(3 in x)
# # True
# # --> da 3 in x enthalten ist.
# ```
# 
# Man will natürlich nicht jeden Index einzeln schreiben, deshalb gibt es die sogenannte <code>range()</code> funktion.
# Diese erhält unter anderem zwei Zahlen als Parameter.
# Der erste ist die Zahl von wo aus gestartet werden soll.
# Die zweite Zahl ist die Zahl, welche nicht mehr dazugehören soll.
# Standardmäßig beträgt die Schrittweite <code>1</code>.
# ```Python
# range(0, n)
# ```
# gibt also eine iterable Datenstruktur mit den Zahlen <code>0</code> bis <code>n-1</code> zurück.
# Technisch gesehen ist es was anderes als eine List von <code>0</code> bis <code>n-1</code>.
# Man kann es aber mit <code>list(range(0, n))</code> zu eben einer Liste von <code>0</code> bis <code>n-1</code> casten.
# Für die For-Schleife ist dieser Cast jedoch nicht nötig.
# 
# Eine praktischere Variante des oberen Python codes wäre also
# ```Python
# for i in range(0, 5):
# 	<Codeblock>
# ```
# Jetzt kommt man zu dem sehr angenehmen Teil von Python wenn es darum geht über eine List zu iterieren.
# Beim iterieren will man meistens logisch gesehen für jeden Eintrag in einer List, den Codeblock mit diesem Objekt ausführen.
# Anstatt dabei jetzt mit Indexen zu arbeiten, kann man auch direkt durch die List iterieren, so wie man es intuitiv machen würde.
# 
# Aussehen würde es so:
# ```Python
# for person in personen:
# 	<mach etwas mit person>
# ```
# Man kann es sich so vorstellen, als ob <code>person</code> ein shortcut wäre für <code>personen[i]</code>, wo <code>i</code> der jeweils aktuelle Index des Objekts ist.
# 
# Wenn man aber explizit mit indizes arbeiten möchte, hält Python einen davon natürlich nicht ab, wie gewohnt mit Indizes zu arbeiten.
# Das würde dann so aussehen:
# ```Python
# for i in range(0, len(personen)):
# 	<mach etwas mit personen[i]>
# ```
# Da in <code>range(0, len(personen))</code>, die Werte von <code>0</code> bis <code>len(personen)-1</code> vertreten sind, werden alle Indizes der List abgedeckt.
# 
# 
# ## While-Schleife
# 
# Hier wird ein Codeblock so oft ausgeführt, bis die Bedinung nicht mehr gilt.
# ```Python
# while bedingung:
# 	<Codeblock>
# ```
# Bspw.:
# ```Python
# while n > 0:
# 	n -= 1
# ```
# Man beachte, dass es in C zwei Arten von while loops gibt.
# Die normale While-Schleife`
# ```C
# while(bedingung) {
# 	<Codeblock>
# }
# ```
# und die Do-while-Schleife
# ```C
# do {
# 	<Codeblock>
# } 
# while(bedingung)
# ```
# 
# Bei letzterem wird die Bedingung erst nach Ausführen des Codeblocks überprüft.
# Diese Option gibt es nicht in Python.
# Will man dieses Verhalten in Python imitieren, so muss man mit einer Infinite loop und bedingten <code>breaks</code> als Workaround arbeiten.
# 
# ```Python
# while True: # Infinite loop
# 	if not bedingung:
# 		break
# 	<Codeblock>
# ```
# Do-while-Schleifen werden eher seltener benutzt, deshalb wird man ihr Fehlen in Python eher weniger spüren, vor allem da es wie gezeigt, auch Workarounds gibt. Dieser Workaround muss in der AlgDat Veranstaltung meines Wissens nach, ein mal angewandt werden bei dem source code vom Quicksort mit Hoare Partition

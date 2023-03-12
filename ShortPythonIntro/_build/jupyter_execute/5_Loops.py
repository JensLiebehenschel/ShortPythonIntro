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
# Im Modul AlgDat werden üblicherweise einbuchstabige Namen für die Zählervariablen gewählt.
# Das wären größtenteils <code>i</code> und <code>j</code>.
# 
# Python geht bei Schleifen wie folgt vor:
# Als Input in die Schleife erhält man keine Formel und Bedinung, mit welcher diese Zählervariablen berechnet werden sollen, sondern übergibt man ein 
# "iterable" object.
# Also ein Array-artiges Object, wo man auf Basis von Indizes unterscheidet.
# 
# In C würde man eine <code>For-Schleife</code> startend bei <code>0</code> mit Schrittweite <code>1</code> so erstellen:
# ```C
# for (int i = 0; i < wert_für_i_welcher_nicht_mehr_dazugehören_soll; i++) {
# 	<Codeblock>
# }
# ```
# Mit der Formel könnte man die einzelnen Werte für <code>i</code> berechnen.
# Man fängt bei <code>i = 0</code> an und inkrementiert um <code>1</code>, bis der Wert erreicht wird, wo die Bedingung in der Mitte nicht mehr den Wahrheitswert <code>wahr</code> zurückgibt.
# 
# 
# In Python würde man hingegeben naiv die Werte <code>0</code> bis zum Grenzwert in Form einer List übergeben.
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
# ### Die angenehmste Methode ist die range() Funktion
# 
# Man will natürlich nicht jeden Index einzeln schreiben, deshalb gibt es die sogenannte <code>range()</code> funktion.
# Diese erhält unter anderem zwei Zahlen als Parameter.
# Die erste ist die Zahl von wo aus gestartet werden soll.
# Die zweite ist die Zahl, welche nicht mehr dazugehören soll.
# Standardmäßig beträgt die Schrittweite <code>1</code>.
# Man kann jedoch auch als dritten Parameter die Schrittweite angeben. 
# Die kann sowohl positiv als auch negativ sein, bei negativen Schrittweiten muss man jedoch darauf aufpassen, dass das erste Argument größer ist als das zweite Argument.
# 
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
# 
# Will man nun eine absteigende For-Schleife von <code>10</code> bis inklusive <code>3</code> mit Schrittweite <code>1</code>, dann kann man dies so machen:
# 
# ```Python
# for i in range(10, 2, -1):
#     <Mache etwas mit i>
# ```
# Die For-Schleife startet bei <code>10</code> und geht bis exklusive <code>2</code>.
# Da wird die Schleife bis inklusive <code>3</code> haben wollen, geben wir den Wert an der bereits **nicht** dazugehören soll, also die Zahl <code>2</code>.
# Die <code>-1</code> als drittes Argument gibt an, dass die Schrittweite <code>-1</code> betragen soll.
# 
# Alternativ kann man die range von <code>3</code> bis inklusive <code>10</code> (bis exklusive <code>11</code>) nehmen und diese mit der <code>reversed()</code> Funktion umdrehen:
# ```Python
# for i in reversed(range(3, 11)):
#     <Mache etwas mit i>
# ```
# 
# ### Iterieren durch ein iterierbares Objekt
# 
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
# Da in <code>range(0, len(personen))</code>, die Werte von <code>0</code> bis <code>len(personen)-1</code> vertreten sind, werden alle Indizes der List <code>personen</code> abgedeckt.
# 
# 
# ## While-Schleife
# 
# Hier wird ein Codeblock so oft ausgeführt, bis die Bedinung nicht mehr gilt.
# ```Python
# while bedingung:
# 	<Codeblock>
# ```
# Beispiel:
# ```Python
# while n > 0:
# 	n -= 1
# ```
# Man beachte, dass es in C zwei Arten von While-Schleifen gibt.
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
# <code>break</code> beendet manuell die aktuelle Schleife. Bei einer Infinite loop ist <code>break</code> die einzige Option, die Schleife zu beenden.
# 
# ```Python
# while True: # Infinite loop
# 	if not bedingung:
# 		break
# 	<Codeblock>
# ```
# Do-while-Schleifen werden eher seltener benutzt, deshalb wird man ihr Fehlen in Python eher weniger spüren, vor allem da es wie gezeigt, auch einen Workaround gibt. Dieser Workaround muss in der AlgDat Veranstaltung meines Wissens nach, ein mal angewandt werden bei dem source code vom Quicksort mit Hoare Partition.

# # Aufgabe

# Jemand hat ein Programm in C geschrieben und offenbar ist etwas schief gelaufen. Die Indentierung wurde gelöscht. Ihre Aufgabe war es, das Programm in Python umzuschreiben, damit man einen Performancevergleich der beiden Programme durchführen kann. Dass die Indentierung verschwunden ist, macht Ihr Leben sicherlich nicht einfacher.

# ```C
# int result = 0;
# for (int i = 0; i < 3; i++) {
# result = result + i * 3;
# for (int j = 3; j > 1; j--) {
# result -= j;    
# int k = 5;
# while (k > i) {
# result += j;
# k = k / 2;
# }
# }
# }    
# printf("%d", result);
# ```

# Jemand hat für Sie schon Vorarbeit geleistet und hat den Großteil des Programms bereits in Python geschrieben. Es fehlen nur noch die Schleifen, wessen Stellen diese Person mit der Markierung <code>&lt;Loop&gt;</code> angegeben hat. Die Indentierung für die hinzuzufügenden Schleifen wurde ebenfalls gelöscht. Die Person hat den Großteil des Programms auskommentiert. Ihre Aufgabe ist es nun, das Auskommentieren rückgängig zu machen und die passende Schleifen an die korrekte Stellen einzufügen. Für das Rückgängig machen des Auskommentierens, sollen Sie die triple-quotes(<code>"""</code>) entfernen. Achten Sie ebenfalls auf korrekte Indentierung. Die Funktionsweise der Schleifen können Sie im obigen C Code nachgucken.

# In[1]:


# Ersetzen Sie "<Loop>" durch die jeweils korrekten Schleifen.
# Achten Sie auf korrekte Indentierung.
result = 0
"""
<Loop>
result = result + i * 3 
<Loop>
result -= j
k = 5
<Loop>
result += j
k = k // 2
"""
print(result)


# :::{admonition} Korrekt indentierten C-Code anzeigen
# :class: dropdown
# 
# ```C
# int result = 0;
# for (int i = 0; i < 3; i++) {
#     result = result + i * 3;
#     for (int j = 3; j > 1; j--) {
#         result -= j;    
#         int k = 5;
#         while (k > i) {
#             result += j;
#             k = k / 2;
#         }
#     }
# }    
# printf("%d", result);
# // 24 
# ```
# 
# :::

# :::{admonition} Show solution
# :class: dropdown
# 
# ```Python
# result = 0
# for i in range(0, 3):
#     result = result + i * 3 
#     for j in range(3, 1, -1):
#         result -= j
#         k = 5
#         while k > i:
#             result += j
#             k = k // 2
# print(result)
# # 24
# ```
# 
# :::

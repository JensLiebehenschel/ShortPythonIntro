#!/usr/bin/env python
# coding: utf-8

# # Schleifen

# Gängige Schleifen gibt es in Python ebenfalls mit den aus anderen Programmiersprachen bekannten Keywords <code>for</code> und <code>while</code>.
# 
# Hier unterscheidet Python sich jedoch syntaktisch von den C-ähnlichen Programmiersprachen.
# 
# 
# ## For-Schleife
# 
# In C wird ein Codeblock in einer for-Schleife ausgeführt solange eine Bedingung erfüllt ist.
# Im Modul AlgDat werden üblicherweise einbuchstabige Namen für die Zählvariablen gewählt, die meist einfach inkrementiert oder dekrementiert werden. Größtenteils werden <code>i</code> und <code>j</code> verwendet.
# 
# Python geht bei Schleifen anders vor:
# Die Anzahl der Wiederholungen einer Schleife basieren nicht auf Formeln und Bedingungen zu Zählvariablen, 
# sondern übergibt man ein "iterable" Objekt.
# Das ist ein Objekt, welches Werte zurück gibt, die beispielsweise als Indizes verwendet werden können.
# 
# In C würde man eine <code>For-Schleife</code> startend bei <code>0</code> mit Schrittweite <code>1</code> so erstellen:
# ```C
# for (int i = 0; i < wert_für_i_welcher_nicht_mehr_dazugehören_soll; i++) {
#     <Codeblock>
# }
# ```
# Die einzelnen Werte für <code>i</code> werden wie folgt berechnet.
# Man fängt bei <code>i = 0</code> an und inkrementiert bis der Wert erreicht ist, bei dem die Bedingung nicht mehrerfüllt ist.
# 
# 
# In Python übergibt man hingegen die Werte <code>0</code> bis zum Grenzwert in Form einer Liste.
# 
# Folgendes Beispiel in C
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
# Man möchte natürlich nicht jeden Index einzeln schreiben, deshalb gibt es die sogenannte <code>range()</code>-Funktion.
# Diese erhält unter anderem zwei Zahlen als Parameter.
# Die erste ist der Startwert.
# Die zweite ist die erste Zahl, welche nicht mehr dazugehört - wie beim Slicing.
# 
# Standardmäßig beträgt die Schrittweite <code>1</code>.
# Man kann jedoch auch als dritten Parameter die Schrittweite angeben. 
# Die kann sowohl positiv als auch negativ sein, bei negativen Schrittweiten muss man jedoch darauf aufpassen, dass das erste Argument größer ist als das zweite Argument.
# 
# ```Python
# range(0, n)
# ```
# gibt also eine Datenstruktur mit den Zahlen <code>0</code> bis <code>n-1</code> zurück.
# Technisch gesehen ist es was anderes als eine Liste von <code>0</code> bis <code>n-1</code>.
# Man kann es aber mit <code>list(range(0, n))</code> zu eben einer Liste von <code>0</code> bis <code>n-1</code> casten.
# Für die For-Schleife ist dieser Cast jedoch nicht nötig.
# 
# Eine praktischere Variante des oberen Python-Codes wäre also
# ```Python
# for i in range(0, 5):
# 	<Codeblock, ausgeführt für i=0, i=1, ..., i=4>
# ```
# 
# Sofern der Startwert Null ist, kann dieser auch weggelassen werden.
# ```Python
# l = [1,2,3,4,5]
# for i in range(len(l)):
# 	<Codeblock>
# ```
# Hiermit wird der Codeblock für alle erlaubten Indizes der Liste <code>l</code> einmal ausgeführt, nämlich von <code>0</code> bis <code>len(l)-1</code>.
# 
# Möchte man nun eine absteigende For-Schleife von <code>10</code> bis inklusive <code>3</code> mit Schrittweite <code>1</code>, dann kann man dies so machen:
# 
# ```Python
# for i in range(10, 2, -1):
#     <Mache etwas mit i>
# ```
# Die For-Schleife startet bei <code>10</code> und geht bis exklusiv <code>2</code>.
# Da wird die Schleife bis inklusiv <code>3</code> haben wollen, geben wir den ersten Wert an, der **nicht** mehr dazu gehören soll, also die Zahl <code>2</code>.
# Die <code>-1</code> als drittes Argument gibt an, dass die Schrittweite <code>-1</code> betragen soll.
# 
# Alternativ kann man die range von <code>3</code> bis inklusiv <code>10</code> (bis exklusiv <code>11</code>) nehmen und diese mit der <code>reversed()</code> Funktion umdrehen:
# ```Python
# for i in reversed(range(3, 11)):
#     <Mache etwas mit i>
# ```
# 
# ### Iterieren durch ein iterierbares Objekt
# 
# Jetzt kommt man zu dem sehr angenehmen Teil von Python, wenn es darum geht, über eine Liste zu iterieren.
# Beim Iterieren möchte man meistens den Codeblock für jeden Eintrag in einer Liste ausführen.
# Anstatt dabei jetzt mit Indizes zu arbeiten, kann man auch direkt durch die Liste iterieren, ganz intuitiv.
# 
# Aussehen würde es so:
# ```Python
# for person in personen:
#     <Mache etwas mit person>
# ```
# Man kann es sich so vorstellen, als ob <code>person</code> ein Shortcut wäre für <code>personen[i]</code>, wobei <code>i</code> der jeweils aktuelle Index des Objekts ist.
# 
# Wenn man aber explizit mit Indizes arbeiten möchte, lässt Python dies zu.
# Das würde dann so aussehen:
# ```Python
# for i in range(len(personen)):
#     <Mache etwas mit personen[i]>
# ```
# Da in <code>range(len(personen))</code>, die Werte von <code>0</code> bis <code>len(personen)-1</code> vertreten sind, werden alle Indizes der Liste <code>personen</code> abgedeckt.
# 
# 
# ## While-Schleife
# 
# Hier wird ein Codeblock so oft ausgeführt, bis die Bedingung nicht mehr gilt.
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
# Die normale While-Schleife
# ```C
# while(bedingung) {
# 	<Codeblock>
# }
# ```
# und die Do-While-Schleife
# ```C
# do {
# 	<Codeblock>
# } 
# while(bedingung)
# ```
# 
# Bei letzterem wird die Bedingung erst nach Ausführen des Codeblocks überprüft.
# Diese Option gibt es nicht in Python.
# Möchte man dieses Verhalten in Python imitieren, so kann man zum Beispiel mit einer Endlosschleife und bedingtem <code>break</code> arbeiten.
# 
# <code>break</code> beendet manuell die aktuelle Schleife. Bei einer Endlosschleife ist <code>break</code> die einzige Möglichkeit, die Schleife zu beenden.
# 
# ```Python
# while True: # Endlosschleife
# 	<Codeblock>
# 	if not bedingung:
# 		break
# ```
# Do-While-Schleifen werden eher seltener benutzt, deshalb wird man ihr Fehlen in Python eher weniger spüren, vor allem, da es einen Workaround gibt.

# ## Aufgabe

# Jemand hat ein Programm in C geschrieben und offenbar ist etwas schief gelaufen. Die Einrückung wurde gelöscht. Ihre Aufgabe ist, das Programm in Python umzuschreiben, damit man einen Performancevergleich der beiden Programme durchführen kann. Dass die Einrückung verschwunden ist, macht Ihr Leben sicherlich nicht einfacher.

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

# Jemand hat für Sie schon Vorarbeit geleistet und hat den Großteil des Programms bereits in Python geschrieben. Es fehlen nur noch die Schleifen, dort steht <code>&lt;Loop&gt;</code>. Die Einrückung für die hinzuzufügenden Schleifen wurde ebenfalls gelöscht. Die Person hat den Großteil des Programms auskommentiert. Ihre Aufgabe ist es nun, das Auskommentieren rückgängig zu machen und die passenden Schleifen an die korrekten Stellen einzufügen. Für das Rückgängigmachen des Auskommentierens, können Sie die triple-quotes(<code>"""</code>) entfernen. Die gewünschte Funktionsweise der Schleifen ist im obigen C-Code ersichtlich.

# In[1]:


# Ersetzen Sie "<Loop>" durch die jeweils korrekten Schleifen.
# Achten Sie auf korrekte Einrückung.
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


# :::{admonition} Korrekt eingerückten C-Code anzeigen
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

# :::{admonition} Lösung
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
